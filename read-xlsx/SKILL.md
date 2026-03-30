---
name: read-xlsx
slash_command: read-xlsx
description: |
  读取 Microsoft Excel (.xlsx / .xls) 电子表格的内容，并以结构化方式（Markdown 表格/CSV/摘要）返回。
  当用户需要查看表格数据、分析特定 Sheet 或提取单元格内容时使用。
usage: |
  /read-xlsx <表格路径> [Sheet名或索引]
---

# read-xlsx Skill

## 触发条件

用户输入 `/read-xlsx <路径>` 时，本 skill 生效。

## 执行流程

1. **检查依赖**：使用 Bash 检查 `python` 或 `python3` 是否可用，以及 `openpyxl` 库是否已安装。
   - 若未安装，自动运行：
     ```bash
     pip install openpyxl
     ```

2. **验证文件**：确认路径存在且以 `.xlsx` 或 `.xls` 结尾。

3. **提取内容**：运行以下 Python 脚本获取工作表列表和指定 Sheet 的数据：
   ```python
   import openpyxl
   wb = openpyxl.load_workbook("<路径>")
   print("Sheets:", wb.sheetnames)
   ws = wb["<Sheet名>"]
   for row in ws.iter_rows(values_only=True):
       print(row)
   ```

4. **数据呈现**：
   - 如果表格较小（< 50 行），直接输出完整的 Markdown 表格。
   - 如果表格较大，输出前 20 行 + 表头，并告知总行数和总列数，询问用户是否需要查看更多或筛选特定内容。

5. **支持 .xls 格式**：
   - 如果是 `.xls` 文件且 `openpyxl` 无法打开，自动安装 `xlrd` 并使用其读取。

## 输出要求

- 始终使用中文回复用户。
- 先列出所有可用的 Sheet 名称。
- 用 Markdown 表格展示数据，保持对齐。
- 若用户未指定 Sheet，默认读取第一个 Sheet。
- 若提取失败，给出具体错误原因。
