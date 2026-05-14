# ASHUO Claude Skills

> 个人 Claude Code 技能库，用于增强 Claude 在特定领域的专业能力。

## 📦 仓库简介

本目录包含一组自定义 Claude Code 技能（Skills），每个技能都是围绕特定工作流设计的专业模块。通常通过 `@技能名` 或对应 slash command 在 Claude Code 中触发。

## 🗂️ 当前技能总览

### 独立技能（按目录扫描）

| 技能名 | 类型 | 功能描述 |
|--------|------|----------|
| `art-asset-designer` | AI 绘画 / 资产设计 | 从剧本、故事、脚本中拆解角色与场景美术资产，并生成可直接用于 AI 出图工具的分类提示词 |
| `dual-core-advisor` | 对话顾问 | 结构化思考 × 同理心引擎，适合个人困惑、决策难题、情绪支持、创意讨论 |
| `extract-video` | 视频解析 | 提取视频基础信息、关键帧截图、音频轨道与字幕，支持转为可分析格式 |
| `historian-storyteller` | 历史研究 / 内容创作 | 深度研究历史人物与事件，并从编剧视角提炼戏剧素材 |
| `image-prompt-engineer` | AI 绘画 | 为 Seedream、Nano Banana、即梦、可灵等中文 AI 绘画模型生成精准提示词 |
| `lyric-mv-storyboard` | MV 分镜 | 根据歌词分析故事内核、情绪弧线、角色关系与意象，输出完整 MV 分镜脚本 |
| `nano-banana-pro-prompter` | AI 绘画 | 为 Nano Banana Pro / Gemini 3 Pro Image 生成结构化 JSON 提示词 |
| `novel-crawler` | 网络爬取 | 爬取网络小说并保存为本地 txt 文件，自动分析章节结构并合并输出 |
| `paiwotscdashi` | AI 视频 | 面向 AI 视频生成的时间轴/分镜提示词生成与音画同步设计 |
| `promo-film-creative` | 创意策划 | 城市、品牌、产品、公益等宣传片创意开发与概念深化 |
| `read-docx` | 文件解析 | 读取 Microsoft Word（.docx）文档内容并转换为纯文本或 Markdown |
| `read-pptx` | 文件解析 | 读取 Microsoft PowerPoint（.pptx）演示文稿中的文字内容 |
| `read-xlsx` | 文件解析 | 读取 Microsoft Excel（.xlsx / .xls）表格内容并结构化输出 |
| `research-assistant` | 联网研究 | 深度搜索、交叉验证、来源评分、矛盾检测与定时信息监控 |
| `screenwriting-master` | 编剧创作 | 全格式影视编剧技能，覆盖概念短片、短片、长片、多集剧集创作流程 |
| `seedance-director` | AI 视频 | 专为 Seedance 2.x 设计的电影级视频分镜与提示词生成器 |
| `shanyin-director-master-main` | 导演分镜 | 从剧本到导演定调、镜头语言、分镜拆解与可执行拍摄方案输出 |
| `short-drama-writer` | 短剧创作 / 市场分析 | 小说/IP 改编短剧、短剧市场分析、原创短剧、分集剧本与分镜设计 |
| `skill-creator` | 开发工具 | 创建、修改、优化 Claude Code 技能，并进行评测与 benchmark |
| `socratic-screenwriter` | 编剧辅导 | 通过苏格拉底式提问帮助用户发展故事、打磨剧本与角色 |
| `video-content-analyst` | 视频分析 / 创作 | 分析视频、沉淀知识库，并基于知识库生成选题创意与分镜脚本 |
| `wan27-image-prompter` | AI 绘画 | 面向阿里 Wan 2.7 图像模型的结构化提示词生成专家 |

### 非独立技能目录

| 目录名 | 类型 | 说明 |
|--------|------|------|
| `lyric-mv-storyboard-workspace` | 工作目录 | `lyric-mv-storyboard` 相关工作区或临时产物目录，不是独立技能 |
| `research-assistant-workspace` | 工作目录 | `research-assistant` 的 benchmark / 测试工作区，不是独立技能 |
| `work` | 工作目录 | 运行期产物目录，供部分技能保存中间文件或输出 |
| `版本存档` | 存档目录 | 历史版本或备份资料目录，不是独立技能 |

## 🚀 快速开始

### 使用方式

在 Claude Code 中可直接通过技能名调用，例如：

```text
@historian-storyteller 帮我研究拿破仑一生中最戏剧性的几个转折点
@image-prompt-engineer 画一张古风女子站在樱花树下的图
@short-drama-writer 这本小说能改成短剧吗
```

部分技能也支持 slash command，例如：

```text
/read-docx C:\path\to\file.docx
/read-xlsx C:\path\to\table.xlsx
/analyze-video C:\path\to\video.mp4
```

## 📖 技能说明（简版）

### `art-asset-designer`
- 适用：剧本/故事/分镜的角色与场景资产拆解
- 输出：角色设计提示词、三视图提示词、纯场景提示词
- 特点：出图前必须先确认统一视觉风格

### `dual-core-advisor`
- 适用：个人困惑、决策分析、工作问题、情绪困扰、创意探讨
- 输出：兼顾共情与结构化分析的建议
- 特点：自动判断先共情还是先分析

### `extract-video`
- 适用：视频内容理解、关键帧提取、音频/字幕提取
- 输出：视频基础信息、截图、音频文件、字幕文本等

### `historian-storyteller`
- 适用：历史人物、历史事件、历史题材内容创作
- 输出：史实梳理、时间线、戏剧冲突、人物弧光与叙事切入点

### `image-prompt-engineer`
- 适用：中文 AI 绘画模型提示词生成
- 输出：可直接用于文生图/图生图/风格迁移的中文提示词

### `lyric-mv-storyboard`
- 适用：根据歌词生成音乐 MV 分镜脚本
- 输出：歌词分析、段落情绪弧线、逐段分镜、整体视觉风格建议

### `nano-banana-pro-prompter`
- 适用：Nano Banana Pro / Gemini 3 Pro Image 图像生成
- 输出：结构化 JSON 提示词、用途分类、使用建议

### `novel-crawler`
- 适用：下载网络小说并保存为本地 txt
- 输出：按章节清洗并合并后的小说文本文件

### `paiwotscdashi`
- 适用：AI 视频提示词生成、时间轴叙事、音画同步设计
- 输出：适配视频模型的时间轴化提示词和镜头方案

### `promo-film-creative`
- 适用：宣传片创意开发、概念提案、Big Idea 延展
- 输出：创意方向、叙事结构、视听风格建议

### `read-docx`
- 适用：读取与分析 Word 文档
- 输出：纯文本、Markdown、表格内容

### `read-pptx`
- 适用：读取与分析 PPT 文本内容
- 输出：按幻灯片结构整理的文本内容

### `read-xlsx`
- 适用：查看和分析 Excel 数据
- 输出：Sheet 列表、指定 Sheet 内容、结构化表格

### `research-assistant`
- 适用：联网资料搜集、事实验证、定时监控任务
- 输出：多源验证结果、可靠性评分、Markdown / HTML 报告

### `screenwriting-master`
- 适用：影视剧本创作、结构设计、角色与场景打磨
- 输出：从概念到完整剧本的分步创作结果
- 特点：强调按步骤推进，不一次性生成全部内容

### `seedance-director`
- 适用：Seedance 2.x 视频提示词、电影级镜头设计、动作戏长镜头
- 输出：适合直接投喂模型的轻量分镜提示词或完整结构化版本

### `shanyin-director-master-main`
- 适用：剧本转导演方案、镜头语言设计、分镜表拆解
- 输出：导演定调、节奏规划、分镜方案、可执行拍摄设计

### `short-drama-writer`
- 适用：短剧改编、短剧市场分析、原创短剧开发
- 输出：分集剧本、钩子节拍表、市场赛道判断、视听化短剧方案

### `skill-creator`
- 适用：新建技能、修改技能、优化技能触发描述、做评测
- 输出：技能模板、修改建议、benchmark / eval 支持

### `socratic-screenwriter`
- 适用：通过问答方式发展故事与剧本
- 输出：帮助用户逐步明确人物、冲突、主题和结构

### `video-content-analyst`
- 适用：分析视频、沉淀知识库、生成视频创意与分镜脚本
- 输出：视频分析条目、规律总结、创意方向、完整脚本方案

### `wan27-image-prompter`
- 适用：Wan 2.7 图像模型提示词生成
- 输出：结构化中文提示词，适合人物、电商、海报、场景等多种需求

## 📝 技能目录约定

推荐技能目录结构如下：

```text
skill-name/
├── SKILL.md              # 技能定义文件（必需）
├── references/           # 参考资料目录（可选）
├── scripts/              # 辅助脚本目录（可选）
├── examples/             # 示例目录（可选）
└── knowledge-base/       # 知识库目录（部分技能使用）
```

### `SKILL.md` 建议结构

```markdown
---
name: skill-name
description: |
  技能描述，说明触发条件和功能
---

# 技能标题

## 角色定位
...

## 工作流程
...

## 输出规范
...
```

## ⚠️ 使用注意

1. **技能触发**：通常使用 `@技能名`，部分技能使用 slash command。
2. **参考资料**：不少技能依赖 `references/` 目录中的方法论或模板文件。
3. **联网能力**：如 `historian-storyteller`、`research-assistant` 等技能可能依赖联网检索。
4. **定时任务**：`research-assistant` 等涉及监控任务的技能会用到定时能力。
5. **运行时产物**：部分技能会在工作目录中生成缓存、中间文件或输出结果。

## 📁 目录说明

| 目录 | 说明 |
|------|------|
| `*/`（含 `SKILL.md` 的目录） | 独立技能模块 |
| `*-workspace/` | 某个技能的工作区或测试目录，通常不是独立技能 |
| `work/` | 通用运行时工作目录 |
| `版本存档/` | 历史版本或备份存档 |

## 🔄 更新维护建议

当新增、删除或重命名技能目录后，建议同步更新本 README 的以下内容：

1. `当前技能总览` 表格
2. `非独立技能目录` 表格
3. `技能说明（简版）` 中对应条目
4. 任何与实际目录不一致的示例或说明

---

> 提示：本目录中的 skills 需要在 Claude Code 环境中使用。
