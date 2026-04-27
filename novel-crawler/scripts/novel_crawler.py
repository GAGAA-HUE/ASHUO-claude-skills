#!/usr/bin/env python3
"""
小说爬虫脚本 - 通用小说网站爬取工具
"""

import json
import sys
import time
import re
from urllib.parse import urljoin, urlparse
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("请先安装依赖: pip install requests beautifulsoup4")
    sys.exit(1)


class NovelCrawler:
    def __init__(self, config):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.chapters = []
        self.failed_chapters = []
        self.empty_chapters = []

    def detect_encoding(self, response):
        """检测响应编码"""
        for encoding in [response.encoding, response.apparent_encoding]:
            if encoding:
                normalized = encoding.lower().replace('_', '-')
                if normalized in ('utf-8-sig', 'utf-8'):
                    return 'utf-8'
                if normalized != 'iso-8859-1':
                    return encoding

        content_type = response.headers.get('content-type', '')
        match = re.search(r'charset=([^;\s]+)', content_type, re.I)
        if match:
            charset = match.group(1).strip().strip('"\'').lower().replace('_', '-')
            return 'utf-8' if charset == 'utf-8-sig' else charset

        html_head = response.content[:4096].decode('ascii', errors='ignore')
        match = re.search(r'<meta[^>]+charset=["\']?([^"\'\s>/]+)', html_head, re.I)
        if match:
            charset = match.group(1).strip().lower().replace('_', '-')
            return 'utf-8' if charset == 'utf-8-sig' else charset

        return 'utf-8'

    def fetch_page(self, url, retries=3):
        """获取页面内容"""
        for i in range(retries):
            try:
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                response.encoding = self.detect_encoding(response)
                return response.text
            except Exception as e:
                if i == retries - 1:
                    print(f"  获取失败: {url} - {e}")
                    return None
                time.sleep(2 ** i)
        return None

    def parse_chapter_number(self, title):
        """从章节标题中提取章节号"""
        if not title:
            return None
        match = re.match(r'^第(\d+)章', title.strip())
        return int(match.group(1)) if match else None

    def extract_chapters(self, html, base_url):
        """提取通用章节列表"""
        soup = BeautifulSoup(html, 'html.parser')

        selectors = [
            '.catalog li a', '.chapter-list a', '.listmain dd a',
            '#list dl a', 'ul.chapters a', '.mulu li a',
            '.catalogue a', '#catalog a', '.chapter-item a',
            'a[href*="read"]', 'a[href*="chapter"]', 'a[href*="book"]'
        ]

        chapters = []
        for selector in selectors:
            links = soup.select(selector)
            if len(links) >= 5:
                for link in links:
                    href = link.get('href', '')
                    title = link.get_text(strip=True)
                    if href and title and len(title) < 100:
                        full_url = urljoin(base_url, href)
                        chapter_number = self.parse_chapter_number(title)
                        chapters.append({
                            'title': title,
                            'url': full_url,
                            'chapter_number': chapter_number,
                        })
                if len(chapters) >= 5:
                    break

        return self.deduplicate_and_sort_chapters(chapters)

    def extract_biquge_paginated_chapters(self, base_url):
        """针对 22biqu 站点提取分页目录"""
        collected = []
        visited_pages = set()
        next_url = base_url

        while next_url and next_url not in visited_pages:
            visited_pages.add(next_url)
            html = self.fetch_page(next_url)
            if not html:
                break

            soup = BeautifulSoup(html, 'html.parser')
            page_chapters = []
            for link in soup.find_all('a', href=True):
                title = link.get_text(' ', strip=True)
                chapter_number = self.parse_chapter_number(title)
                if chapter_number is None:
                    continue

                full_url = urljoin(next_url, link['href'])
                if '/biqu' not in full_url or not full_url.endswith('.html'):
                    continue

                page_chapters.append({
                    'title': title,
                    'url': full_url,
                    'chapter_number': chapter_number,
                })

            collected.extend(page_chapters)

            next_link = soup.find('a', string=lambda s: s and '下一页' in s)
            if not next_link:
                break
            next_url = urljoin(next_url, next_link.get('href', ''))

        return self.deduplicate_and_sort_chapters(collected)

    def deduplicate_and_sort_chapters(self, chapters):
        """去重并按章节号排序"""
        by_number = {}
        without_number = []
        seen_urls = set()

        for chapter in chapters:
            url = chapter['url']
            if url in seen_urls:
                continue
            seen_urls.add(url)

            number = chapter.get('chapter_number')
            if number is None:
                without_number.append(chapter)
                continue

            existing = by_number.get(number)
            if not existing or len(chapter['title']) > len(existing['title']):
                by_number[number] = chapter

        ordered = [by_number[number] for number in sorted(by_number)]
        ordered.extend(without_number)
        return ordered

    def extract_content(self, html, fallback_title=''):
        """提取正文内容"""
        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup(['script', 'style', 'iframe', 'nav', 'header', 'footer']):
            tag.decompose()

        content_selectors = [
            '#chaptercontent', '#content', '.content', '.chapter-content',
            '.read-content', '.text', '#booktext', '.novel-content',
            '.chapter-body', '.article-content', '#txtcontent',
            '.showtxt', '#htmlContent'
        ]

        content_elem = None
        for selector in content_selectors:
            elem = soup.select_one(selector)
            if elem and len(elem.get_text(strip=True)) > 200:
                content_elem = elem
                break

        if not content_elem:
            paragraphs = soup.find_all('p')
            if len(paragraphs) > 5:
                candidates = {}
                for p in paragraphs[:50]:
                    parent = p.find_parent(['div', 'article', 'section'])
                    if parent:
                        pid = id(parent)
                        candidates[pid] = candidates.get(pid, 0) + 1

                if candidates:
                    best_pid = max(candidates, key=candidates.get)
                    for p in paragraphs[:50]:
                        parent = p.find_parent(['div', 'article', 'section'])
                        if parent and id(parent) == best_pid:
                            content_elem = parent
                            break

        if not content_elem:
            return None

        title = ''
        title_selectors = [
            '.bookname h1', '.content h1', '.chaptertitle', '.chapter-title',
            '#chaptertitle', '#title', 'h1', 'h2', 'h3'
        ]
        for selector in title_selectors:
            title_elem = soup.select_one(selector)
            if not title_elem:
                continue
            candidate = title_elem.get_text(strip=True)
            if candidate and len(candidate) < 100 and candidate != '笔趣阁':
                title = candidate
                break

        if not title:
            title = fallback_title

        text = content_elem.get_text('\n', strip=True)

        ad_patterns = [
            r'本章由.*赞助', r'请记住本书首发域名', r'笔趣阁',
            r'阅读最新章节', r'手机阅读', r'天才壹秒記住',
            r'上一章', r'下一章', r'返回目录', r'加入书签',
            r'\(\)', r'【】', r'&nbsp;', r'\s+\n', r'\n\s+'
        ]
        for pattern in ad_patterns:
            text = re.sub(pattern, '', text)

        lines = [line.strip() for line in text.split('\n') if line.strip()]
        text = '\n\n'.join(lines)

        return {'title': title, 'content': text}

    def find_missing_ranges(self, chapter_numbers):
        """查找缺失的章节号区间"""
        if not chapter_numbers:
            return []

        missing = []
        expected = set(range(min(chapter_numbers), max(chapter_numbers) + 1))
        absent = sorted(expected - set(chapter_numbers))
        if not absent:
            return []

        start = prev = absent[0]
        for number in absent[1:]:
            if number == prev + 1:
                prev = number
                continue
            missing.append((start, prev))
            start = prev = number
        missing.append((start, prev))
        return missing

    def crawl(self):
        """执行爬取"""
        base_url = self.config['base_url']
        output_path = self.config.get('output_path', './novel.txt')
        delay = self.config.get('delay', 1.0)

        if 'chapter_links' in self.config and self.config['chapter_links']:
            chapter_links = self.config['chapter_links']
            if isinstance(chapter_links[0], str):
                self.chapters = [{'title': f'第{i+1}章', 'url': url, 'chapter_number': i + 1}
                                 for i, url in enumerate(chapter_links)]
            else:
                self.chapters = chapter_links
        else:
            print(f"正在分析目录页: {base_url}")
            parsed = urlparse(base_url)
            if '22biqu.' in parsed.netloc and re.search(r'/biqu\d+/?$', parsed.path):
                self.chapters = self.extract_biquge_paginated_chapters(base_url)
            else:
                html = self.fetch_page(base_url)
                if not html:
                    print("获取目录页失败")
                    return False
                self.chapters = self.extract_chapters(html, base_url)

            if not self.chapters:
                print("未能提取到章节列表，请检查页面结构")
                return False

        total = len(self.chapters)
        print(f"找到 {total} 个章节")

        start = self.config.get('start_chapter', 0)
        end = self.config.get('end_chapter', -1)
        if end < 0:
            end = total
        self.chapters = self.chapters[start:end]
        print(f"将爬取第 {start + 1} 章到第 {end} 章，共 {len(self.chapters)} 章")

        results = []
        for i, chapter in enumerate(self.chapters):
            title = chapter.get('title', f'第{i + 1}章')
            print(f"进度: [{i + 1}/{len(self.chapters)}] {title[:30]}...", end=' ')

            html = self.fetch_page(chapter['url'])
            if html:
                content = self.extract_content(html, fallback_title=title)
                if content and content['content']:
                    results.append({
                        'title': content['title'] or title,
                        'content': content['content'],
                        'chapter_number': chapter.get('chapter_number'),
                    })
                    print("[OK]")
                else:
                    self.empty_chapters.append(chapter)
                    print("[EMPTY]")
            else:
                self.failed_chapters.append(chapter)
                print("[FAIL]")

            if i < len(self.chapters) - 1:
                time.sleep(delay)

        if not results:
            print("没有成功获取任何章节")
            return False

        self.save_to_file(results, output_path)

        chapter_numbers = [c['chapter_number'] for c in self.chapters if c.get('chapter_number') is not None]
        missing_ranges = self.find_missing_ranges(chapter_numbers)
        print(f"成功章节: {len(results)}")
        print(f"抓取失败章节: {len(self.failed_chapters)}")
        print(f"空内容章节: {len(self.empty_chapters)}")
        if missing_ranges:
            missing_text = ', '.join(
                f"{start}-{end}" if start != end else str(start)
                for start, end in missing_ranges
            )
            print(f"目录缺失章节号: {missing_text}")
        else:
            print("目录缺失章节号: 无")

        if self.failed_chapters:
            print("失败章节列表:")
            for chapter in self.failed_chapters:
                print(f"  - {chapter.get('title', chapter['url'])}: {chapter['url']}")

        if self.empty_chapters:
            print("空内容章节列表:")
            for chapter in self.empty_chapters:
                print(f"  - {chapter.get('title', chapter['url'])}: {chapter['url']}")

        return True

    def save_to_file(self, chapters, output_path):
        """保存到文件"""
        novel_title = self.config.get('title', '未知小说')
        author = self.config.get('author', '未知作者')

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, 'w', encoding='utf-8-sig') as f:
            f.write(f"《{novel_title}》\n")
            f.write(f"作者：{author}\n\n")
            f.write("=" * 50 + "\n\n")

            for chapter in chapters:
                f.write(f"{chapter['title']}\n\n")
                f.write(chapter['content'])
                f.write("\n\n" + "=" * 50 + "\n\n")

        file_size = output.stat().st_size
        print(f"\n已完成！共保存 {len(chapters)} 章")
        print(f"文件路径: {output.absolute()}")
        print(f"文件大小: {file_size / 1024 / 1024:.2f} MB")


def main():
    if len(sys.argv) < 2:
        print("用法: python novel_crawler.py <config.json>")
        sys.exit(1)

    config_path = sys.argv[1]
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    crawler = NovelCrawler(config)
    success = crawler.crawl()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
