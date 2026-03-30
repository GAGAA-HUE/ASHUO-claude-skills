# index.json 结构说明

## 设计原则

三维并存，互不替代：
- **tag_index**：内容维度检索（这是什么类型的内容？）
- **methodology_index**：方法论维度检索（用了什么创作策略？）
- **entries[].meta.date** + 文件名前缀：时间维度检索（什么时候学到的？）

`reuse_count` 是隐性质量信号：被创意生成和脚本生成引用越多，说明这条规律越具普适性。

---

## 字段说明

### entries[] 每条条目

| 字段 | 类型 | 说明 |
|------|------|------|
| id | string | `YYYY-MM-DD_slug` 格式，全局唯一 |
| file | string | 相对于 kb 根目录的文件路径 |
| meta.title | string | 视频标题或自定义名称 |
| meta.source_platform | string | 来源平台（抖音/B站/CCTV等） |
| meta.duration_seconds | number | 视频时长（秒） |
| tags | string[] | 内容标签，以 # 开头 |
| methodology.hook_type | string | 钩子类型（金句前置/悬念型/痛点共鸣/反常识） |
| methodology.structure_model | string | 叙事结构描述 |
| methodology.visual_style | string | 视觉风格（AI生成/真人/混合/动画） |
| methodology.language_tone | string | 语言调性描述 |
| effectiveness.hook_strength | 1-5 | 钩子强度评分 |
| effectiveness.information_density | 1-5 | 信息密度评分 |
| effectiveness.virality_potential | 1-5 | 传播势能评分 |
| reuse_count | number | 被 generate-idea / write-script 引用次数 |
| hypotheses | string[] | 本条目产生的待验证假设 |
| last_cited | string\|null | 最后一次被引用的 ISO 时间戳 |

### tag_index

反向索引：标签 → 条目ID列表。
用途：`/generate-idea 时事评论` 时快速找到所有 `#时事评论` 条目。

### methodology_index

三个子维度：
- `hook_type`：钩子类型 → 条目ID列表
- `structure_model`：结构模型关键词 → 条目ID列表
- `visual_style`：视觉风格 → 条目ID列表

用途：`/write-script` 生成脚本时，按需检索最佳匹配的历史规律。

---

## 扩展建议

当条目数量超过50条后，建议为 `effectiveness` 字段增加：
- `actual_performance`：记录实际发布后的数据（播放量区间/完播率/互动率）
- `performance_source`：数据来源说明

这样 `virality_potential`（预判）和 `actual_performance`（实测）形成闭环，
可以反向验证 AI 的预判准确性，进而优化评分标准。
