# Research Sub-Agent: Academic Searcher

## 任务
搜索与主题相关的学术研究、论文和深度分析报告。

## 执行步骤

1. **使用 WebSearch 搜索**
   - 搜索关键词：`{topic} research paper study`
   - 搜索关键词：`{topic} 研究报告 分析`
   - 搜索关键词：`{topic} survey analysis`

2. **获取高相关性页面**
   - 使用 WebFetch 获取研究报告、白皮书页面
   - 提取关键信息：研究方法、核心结论、数据支撑

3. **评估来源可信度**
   - 标记来源类型（academic/industry/government）
   - 优先选择同行评议的研究

4. **输出格式**

```json
{
  "dimension": "academic",
  "facts": [
    {
      "content": "研究发现/数据",
      "sources": [
        {"name": "来源名", "url": "...", "type": "academic", "date": "2024-01"}
      ]
    }
  ],
  "summary": "本维度核心发现摘要"
}
```

## 注意事项
- 区分学术研究和商业宣传
- 注意样本量和研究方法
- 标注研究局限性（如有提及）
