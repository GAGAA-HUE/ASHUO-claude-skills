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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0'
        })
        self.chapters = []

    def detect_encoding(self, response):
        """检测响应编码"""
        # 从响应头检测
        encoding = response.encoding
        if encoding and encoding.lower() != 'iso-8859-1':
            return encoding

        # 从 HTML meta 标签检测
        content_type = response.headers.get('content-type', '')
        if 'charset=' in content_type:
            return content_type.split('charset=')[-1].split(';')[0].strip()

        # 尝试从内容检测
        content = response.content
        for enc in ['utf-8', 'gbk', 'gb2312', 'gb18030']:
            try:
                decoded = content.decode(enc)
                if 'charset=' in decoded:
                    match = re.search(r'charset=["\']?([^"\'>]+)', decoded)
                    if match:
                        return match.group(1).lower()
                return enc
            except:
                continue
        return 'utf-8'

    def fetch_page(self, url, retries=3):
        """获取页面内容"""
        for i in range(retries):
            try:
                response = self.session.get(url, timeout=30)
                encoding = self.detect_encoding(response)
                response.encoding = encoding
                return response.text
            except Exception as e:
                if i == retries - 1:
                    print(f"  获取失败: {url} - {e}")
                    return None
                time.sleep(2 ** i)
        return None

    def extract_chapters(self, html, base_url):
        """提取章节列表"""
        soup = BeautifulSoup(html, 'html.parser')

        # 尝试多种章节列表选择器
        selectors = [
            '.catalog li a', '.chapter-list a', '.listmain dd a',
            '#list dl a', 'ul.chapters a', '.mulu li a',
            '.catalogue a', '#catalog a', '.chapter-item a',
            'a[href*="read"]', 'a[href*="chapter"]', 'a[href*="book"]'
        ]

        chapters = []
        for selector in selectors:
            links = soup.select(selector)
            if len(links) >= 5:  # 至少要有5个链接才算有效
                for link in links:
                    href = link.get('href', '')
                    title = link.get_text(strip=True)
                    if href and title and len(title) < 100:
                        full_url = urljoin(base_url, href)
                        chapters.append({
                            'title': title,
                            'url': full_url
                        })
                if len(chapters) >= 5:
                    break

        # 去重并保持顺序
        seen = set()
        unique_chapters = []
        for ch in chapters:
            if ch['url'] not in seen:
                seen.add(ch['url'])
                unique_chapters.append(ch)

        return unique_chapters

    def extract_content(self, html):
        """提取正文内容"""
        soup = BeautifulSoup(html, 'html.parser')

        # 移除脚本和样式
        for tag in soup(['script', 'style', 'iframe', 'nav', 'header', 'footer']):
            tag.decompose()

        # 尝试多种正文选择器
        content_selectors = [
            '.content', '.chapter-content', '#content',
            '.read-content', '.text', '#booktext',
            '.novel-content', '.chapter-body', '.article-content',
            '#txtcontent', '.showtxt', '#htmlContent'
        ]

        content_elem = None
        for selector in content_selectors:
            elem = soup.select_one(selector)
            if elem and len(elem.get_text(strip=True)) > 200:
                content_elem = elem
                break

        if not content_elem:
            # 回退：找最长的文本段落
            paragraphs = soup.find_all('p')
            if len(paragraphs) > 5:
                # 找包含最多段落的容器
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

        # 提取章节标题
        title = ''
        title_selectors = ['h1', '.chapter-title', '.title', '#title', 'h2', 'h3']
        for selector in title_selectors:
            title_elem = soup.select_one(selector)
            if title_elem:
                title = title_elem.get_text(strip=True)
                if title and len(title) < 100:
                    break

        # 清理内容
        text = content_elem.get_text('\n', strip=True)

        # 移除常见广告文本
        ad_patterns = [
            r'本章由.*赞助', r'请记住本书首发域名', r'笔趣阁',
            r'阅读最新章节', r'手机阅读', r'天才壹秒記住',
            r'上一章', r'下一章', r'返回目录', r'加入书签',
            r'\(\)', r'【】', r'&nbsp;', r'\s+\n', r'\n\s+'
        ]
        for pattern in ad_patterns:
            text = re.sub(pattern, '', text)

        # 清理多余空行
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        text = '\n\n'.join(lines)

        return {'title': title, 'content': text}

    def crawl(self):
        """执行爬取"""
        base_url = self.config['base_url']
        output_path = self.config.get('output_path', './novel.txt')
        delay = self.config.get('delay', 1.0)

        # 如果提供了章节链接列表，直接使用
        if 'chapter_links' in self.config and self.config['chapter_links']:
            chapter_links = self.config['chapter_links']
            if isinstance(chapter_links[0], str):
                self.chapters = [{'title': f'第{i+1}章', 'url': url}
                                for i, url in enumerate(chapter_links)]
            else:
                self.chapters = chapter_links
        else:
            # 否则从目录页提取
            print(f"正在分析目录页: {base_url}")
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

        # 应用章节范围
        start = self.config.get('start_chapter', 0)
        end = self.config.get('end_chapter', -1)
        if end < 0:
            end = total
        self.chapters = self.chapters[start:end]
        print(f"将爬取第 {start+1} 章到第 {end} 章，共 {len(self.chapters)} 章")

        # 爬取各章节
        results = []
        for i, chapter in enumerate(self.chapters):
            print(f"进度: [{i+1}/{len(self.chapters)}] {chapter['title'][:30]}...", end=' ')

            html = self.fetch_page(chapter['url'])
            if html:
                content = self.extract_content(html)
                if content and content['content']:
                    results.append({
                        'title': content['title'] or chapter['title'],
                        'content': content['content']
                    })
                    print("✓")
                else:
                    print("× (未提取到内容)")
            else:
                print("× (获取失败)")

            if i < len(self.chapters) - 1:
                time.sleep(delay)

        # 保存文件
        if not results:
            print("没有成功获取任何章节")
            return False

        self.save_to_file(results, output_path)
        return True

    def save_to_file(self, chapters, output_path):
        """保存到文件"""
        novel_title = self.config.get('title', '未知小说')
        author = self.config.get('author', '未知作者')

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, 'w', encoding='utf-8') as f:
            # 写入标题和作者
            f.write(f"《{novel_title}》\n")
            f.write(f"作者：{author}\n\n")
            f.write("=" * 50 + "\n\n")

            # 写入各章节
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
