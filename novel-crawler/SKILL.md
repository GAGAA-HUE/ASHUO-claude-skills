---
name: novel-crawler
description: 爬取网络小说并保存为本地 txt 文件。当用户想要下载小说、抓取网页小说、保存在线小说到本地、从小说网站提取内容时触发。支持通用小说网站适配，自动分析章节结构，单线程稳定爬取，合并输出为单个 txt 文件。
---

# 小说爬虫 (Novel Crawler)

帮助用户从网页下载小说并保存为本地 txt 文件。

## 使用流程

1. **获取小说 URL** — 询问用户提供小说目录页或第一章的 URL
2. **分析网站结构** — 使用 WebFetch 工具查看页面，识别章节列表和内容区域
3. **配置爬取参数** — 确定起始章节、结束章节（可选）
4. **执行爬取** — 单线程顺序获取各章节内容
5. **保存文件** — 合并所有章节为单个 txt 文件

## 爬取策略

### 第一步：分析页面结构

使用 WebFetch 获取页面内容，重点关注：
- 章节列表的 CSS 选择器（通常在 `<ul>`、`<dl>`、`.catalog`、`.chapter-list` 等容器中）
- 章节链接的格式（相对路径或绝对 URL）
- 正文内容的容器（通常是 `.content`、`.chapter-content`、`#content`、`<article>` 等）

### 第二步：提取章节列表

```python
# 常见的章节列表选择器模式
chapter_selectors = [
    '.catalog li a',
    '.chapter-list a',
    '.listmain dd a',
    '#list dl a',
    'ul.chapters a',
    '.mulu li a',
    'a[href*="read"]',
    'a[href*="chapter"]',
]
```

### 第三步：内容提取

正文内容通常需要：
- 移除广告元素（`.ad`、`.ads`、`.script`）
- 移除导航链接（"上一章"、"下一章"、"返回目录"）
- 清理多余空白行
- 保留段落结构

```python
# 常见正文选择器
content_selectors = [
    '.content',
    '.chapter-content',
    '#content',
    '.read-content',
    '.text',
    '#booktext',
    '.novel-content',
    'article',
]
```

## 实现脚本

使用 `scripts/novel_crawler.py` 脚本执行实际爬取任务：

```bash
python scripts/novel_crawler.py <config_json>
```

配置文件格式：
```json
{
  "base_url": "https://example.com/novel/123/",
  "chapter_links": ["/novel/123/1.html", "/novel/123/2.html", ...],
  "title": "小说标题",
  "author": "作者名（可选）",
  "start_chapter": 0,
  "end_chapter": -1,
  "output_path": "./小说标题.txt",
  "content_selector": ".content",
  "title_selector": "h1, .chapter-title",
  "delay": 1.0
}
```

## 爬取规范

### 反爬与礼仪
- **请求延迟**：每章之间至少延迟 1-2 秒
- **User-Agent**：使用常见的浏览器 User-Agent
- **失败重试**：单章失败时重试 3 次，然后跳过继续
- **并发控制**：单线程顺序爬取，避免对服务器造成压力

### 内容清理
- 移除脚本标签和样式标签
- 移除明显的广告文本（"本章由XX赞助"、"点击收藏"等）
- 保留章节标题和正文段落
- 统一换行格式（\n\n 分隔段落）

### 文件输出格式
```
《小说标题》
作者：XXX

==================

第一章 标题

正文内容...

==================

第二章 标题

正文内容...
```

## 边界情况处理

| 情况 | 处理方式 |
|------|----------|
| 章节列表分页 | 先获取所有分页链接，合并章节列表 |
| 内容需要 JS 渲染 | 提示用户该网站暂不支持 |
| 需要登录/付费 | 检测登录提示，跳过受限章节并告知用户 |
| 编码问题 | 自动检测编码（UTF-8、GBK、GB2312） |
| 反爬拦截 | 检测到验证码或封禁提示时暂停并告知用户 |

## 示例对话

**用户**: 帮我下载这个小说 https://www.example.com/novel/12345/

**Claude**: 我来帮你爬取这本小说。让我先分析页面结构...

[分析页面，识别章节列表和内容区域]

找到了 150 章内容。是否从第一章开始爬取全部？或者你只想爬取特定范围？

[用户确认后开始爬取]

正在爬取，每章间隔 1 秒以避免对网站造成压力...
进度: 15/150 章

[完成后]

已完成！小说《XXX》已保存到 `./《XXX》.txt`，共 150 章，约 2.3 MB。
