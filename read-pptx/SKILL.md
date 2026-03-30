---
name: read-pptx
slash_command: read-pptx
description: |
  读取 Microsoft PowerPoint (.pptx) 演示文稿的文本内容，并按幻灯片结构返回。
  当用户需要总结、分析或提取 PPT 中的文字信息时使用。
usage: |
  /read-pptx <演示文稿路径>
---

# read-pptx Skill

## 触发条件

用户输入 `/read-pptx <路径>` 时，本 skill 生效。

## 执行流程

1. **检查依赖**：使用 Bash 检查 `python` 或 `python3` 是否可用，以及 `python-pptx` 库是否已安装。
   - 若未安装，自动运行：
     ```bash
     pip install python-pptx
     ```

2. **验证文件**：确认路径存在且以 `.pptx` 结尾。

3. **提取内容**：运行以下 Python 脚本：
   ```python
   from pptx import Presentation
   prs = Presentation("<路径>")
   for i, slide in enumerate(prs.slides, 1):
       print(f"--- 幻灯片 {i} ---")
       for shape in slide.shapes:
           if hasattr(shape, "text") and shape.text.strip():
               print(shape.text.strip())
   ```

4. **结构化输出**：
   - 按幻灯片顺序组织内容。
   - 识别标题和正文层级。
   - 如果幻灯片数量较多（> 20 页），先输出目录概览和前几页详情，询问是否需要继续。

5. **备注**：
   - PPT 中的图片、图表、SmartArt 的纯文本可能无法完全提取。
   - 若遇到复杂布局，告知用户哪些内容可能被遗漏。

## 输出要求

- 始终使用中文回复用户。
- 每页幻灯片的内容用清晰的标题分隔。
- 保留文本的层级和列表结构。
- 若提取失败，给出具体错误原因和修复建议。
