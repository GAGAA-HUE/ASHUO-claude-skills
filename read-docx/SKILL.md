---
name: read-docx
slash_command: read-docx
description: |
  读取 Microsoft Word (.docx) 文档的内容，并将其转换为纯文本或 Markdown 格式返回。
  当用户需要分析、搜索或总结 Word 文档时使用。
usage: |
  /read-docx <文档路径>
---

# read-docx Skill

## 触发条件

用户输入 `/read-docx <路径>` 时，本 skill 生效。

## 执行流程

1. **检查依赖**：使用 Bash 检查 `python` 或 `python3` 是否可用，以及 `python-docx` 库是否已安装。
   - 若未安装，自动运行：
     ```bash
     pip install python-docx
     ```

2. **验证文件**：确认路径存在且以 `.docx` 结尾。

3. **提取内容**：运行以下 Python 脚本：
   ```python
   from docx import Document
   doc = Document("<路径>")
   for para in doc.paragraphs:
       print(para.text)
   ```

4. **处理表格（如有）**：
   - 遍历文档中的所有表格，将表格内容以 Markdown 表格格式输出。

5. **返回内容**：
   - 若文档较长，先返回前 3000 字，并询问是否需要继续。
   - 若包含图片，告知用户文档中有图片但无法直接提取（可提供替代方案如转为 PDF 后提取）。

## 输出要求

- 始终使用中文回复用户。
- 保留文档的层级结构（标题、正文、列表等）。
- 对于表格，尽量用 Markdown 表格呈现。
- 若提取失败，给出具体错误原因和修复建议。
