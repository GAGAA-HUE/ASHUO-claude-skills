# ASHUO Claude Skills

> 个人 Claude Code 技能库，用于增强 Claude 在特定领域的专业能力

## 📦 仓库简介

本仓库包含多个自定义 Claude Code 技能（Skills），每个技能都是针对特定工作流设计的专业模块。

## 🗂️ 技能清单

### 🎬 视频创作与生成

| 技能名 | 功能描述 |
|--------|----------|
| `extract-video` | 提取视频信息、关键帧、音频、字幕 |
| `lyric-mv-storyboard` | 根据歌词深度分析，生成完整音乐 MV 分镜脚本 |
| `seedance-director` | 电影级分镜提示词生成器，专为 Seedance 2.x 优化 |
| `shanyin-director-master-main` | 山音导演大师：专业 AI 视频生成提示词系统 |
| `hailuo-h3-director` | H3 多模态视频提示词生成器，专为 Hailuo H3（MiniMax）设计 |

### 🖼️ AI 绘画与图像

| 技能名 | 功能描述 |
|--------|----------|
| `art-asset-designer` | 美术资产设计师：从剧本拆解人物/场景资产，生成 AI 图像生成提示词 |
| `video-style-prompt-advisor` | 视频视觉风格定调顾问：输出可复用的 GPT image2 风格预设提示词 |

### ✍️ 创作与编剧

| 技能名 | 功能描述 |
|--------|----------|
| `historian-storyteller` | 历史洞察家：历史人物/事件深度研究，输出编剧视角戏剧素材 |
| `historical-vlog-creator` | 历史名人第一视角 Vlog 脚本：用现代网络语言自述真实生平 |
| `screenwriting-master` | 山音专业编剧辅助：剧本结构分析与创作指导，全格式影视剧本 |
| `short-drama-writer` | 短剧编剧大师：小说改编、市场分析、原创短剧、分集剧本与分镜 |
| `suno-prompter` | Suno v5.5 Pro 音乐提示词+歌词生成专家 |

### 💻 软件开发

| 技能名 | 功能描述 |
|--------|----------|
| `code-review` | 代码审查：对比固定基准点，从规范/需求双轴并行审查变更 |
| `codebase-design` | 深度模块设计词汇表：设计/改进模块接口，找到深化机会 |
| `design-an-interface` | 并行生成多种截然不同的接口设计方案 |
| `diagnosing-bugs` | 疑难 bug 与性能回归诊断循环 |
| `domain-modeling` | 领域建模：构建与打磨项目领域模型，维护统一语言 |
| `git-guardrails-claude-code` | 设置 Claude Code 钩子，阻止危险 git 操作 |
| `migrate-to-shoehorn` | 将测试文件中的 `as` 类型断言迁移到 @total-typescript/shoehorn |
| `prototype` | 构建一次性原型，回答设计问题 |
| `qa` | 交互式 QA：用户口述 bug，自动提交 GitHub Issue |
| `request-refactor-plan` | 通过用户访谈创建详细重构计划，提交为 GitHub Issue |
| `resolving-merge-conflicts` | 解决进行中的 git merge/rebase 冲突 |
| `scaffold-exercises` | 创建练习目录结构，含题目、解答和解析 |
| `setup-pre-commit` | 配置 Husky pre-commit 钩子（Prettier + 类型检查 + 测试） |
| `tdd` | 测试驱动开发：红→绿循环，含测试规范与反模式指导 |
| `simplify` | 代码简化：审查变更后的代码，应用复用、简化、效率和高度清理 |
| `security-review` | 安全审查：扫描安全漏洞和潜在风险 |

### 📋 项目管理与规划

| 技能名 | 功能描述 |
|--------|----------|
| `grilling` | 压力测试：就方案/决策/想法进行无情追问 |
| `department-report` | 部门报告生成：将工作日志转化为结构化部门报告 |

### 🔧 工具与辅助

| 技能名 | 功能描述 |
|--------|----------|
| `obsidian-vault` | Obsidian 笔记搜索、创建与管理（含 wikilinks） |
| `research` | 调研问题并将发现保存为仓库内 Markdown 文件 |
| `research-assistant` | 智能联网搜索、多源交叉验证、定时监控任务 |

### 📁 文件解析

| 技能名 | 功能描述 |
|--------|----------|
| `read-docx` | 读取 Microsoft Word 文档，转为纯文本/Markdown |
| `read-pptx` | 读取 Microsoft PowerPoint 演示文稿文字内容 |
| `read-xlsx` | 读取 Microsoft Excel 电子表格，结构化输出 |

### 🛠️ Claude Code 系统工具

| 技能名 | 功能描述 |
|--------|----------|
| `skill-creator` | 技能创建器：创建、修改、优化和测试 Claude 技能 |
| `init` | 初始化项目 CLAUDE.md 文档 |
| `review` | 代码审查（系统内置） |
| `dataviz` | 数据可视化：创建图表、仪表板和可视化 |
| `update-config` | 配置 settings.json，设置权限、钩子和环境变量 |
| `keybindings-help` | 自定义键盘快捷键配置 |
| `fewer-permission-prompts` | 减少权限提示：自动添加常用命令到白名单 |
| `loop` | 循环执行：按时间间隔重复运行命令或技能 |
| `claude-api` | Claude API / Anthropic SDK 参考文档 |
| `run` | 启动和驱动项目应用，确认变更生效 |

---

## 🚀 安装技能

### 从本仓库克隆

```bash
git clone https://github.com/GAGAA-HUE/ASHUO-claude-skills.git ~/.claude/skills
```

### 安装 Matt Pocock 技能包

```bash
npx skills@latest add mattpocock/skills
```

---

## 📖 重点技能详解

### art-asset-designer（美术资产设计师）

从剧本/脚本中拆解所有需要视觉化的人物与场景资产，生成可直接用于 Midjourney、SD、DALL-E、Flux 等工具的提示词。流程：剧本解析 → 资产清单 → 风格确认 → 分类提示词生成。

---

### historical-vlog-creator（历史名人第一视角 Vlog）

历史人物用第一人称自述真实生平，用现代网络语言（打工人/直播/朋友圈梗）讲历史。两阶段输出：先出创意框架→确认后生成完整台词+分镜。台词节奏对齐抖音爆款格式（60-90秒）。

---

### historian-storyteller（历史洞察家）

历史人物/事件深度研究，动态时间线构建（带标签系统），编剧视角戏剧素材提炼，叙事钩子与人物弧光分析。

---

### short-drama-writer（短剧编剧大师）

- `/adapt-novel`：小说/IP 改编为标准分集剧本
- `/market-analysis`：国内外爆款规律与赛道热度分析
- `/original-drama`：从零原创短剧
- `/shot-script`：在分集基础上叠加分镜视听语言
- `/diagnose`：剧本五维诊断

覆盖国内抖快微短剧与海外 Reelshort/DramaBox/ShortMax 出海赛道。

---

### seedance-director（Seedance 分镜导演）

电影级分镜提示词生成，专为 Seedance 2.x 优化。专业打斗场景支持，Shot 级美术设定隔离，单个 Shot 提示词限制 2000 字符，自然语言化提示词正文。默认输出适合直接复制的轻量成品提示词，优先贴近长镜头、多分镜、蒙太奇三类实用模板。

---

### hailuo-h3-director（Hailuo H3 多模态视频提示词生成器）

H3 多模态视频提示词生成器，专为 Hailuo H3（MiniMax）设计。核心场景：AE 片头、MG 动画、产品广告、游戏界面、UI 动效、MV 视觉、网页展示。支持文生视频、图生视频、视频生视频、音频驱动、多模态编辑。强项：文案准确性（包装/UI 文字逐字还原）、运动设计、音画同步、多模态素材融合。

---

### grilling（压力测试）

就方案/决策/想法进行无情追问，逐一处理决策树的每个分支，每次只问一个问题并附上推荐答案。适用于技术决策、架构设计、产品规划等需要深度思考的场景。

---

### department-report（部门报告生成器）

将工作日志、会议记录、项目进展等信息转化为结构化的部门报告，支持自定义模板和格式。

---

### research（调研代理）

启动后台 Agent 对主要信息源（官方文档、源代码、规格文档）进行调研，将发现保存为仓库内 Markdown 文件。适合深度技术调研和文档整理。

---

## 📝 技能开发规范

### 文件结构

```
skill-name/
├── SKILL.md              # 技能定义文件（必需）
├── references/           # 参考资料目录
├── scripts/              # 辅助脚本目录（可选）
├── examples/             # 示例目录（可选）
└── knowledge-base/       # 知识库目录（部分技能使用）
```

### SKILL.md 基本结构

```markdown
---
name: skill-name
description: |
  技能描述，说明触发条件和功能
---

# 技能标题

## 角色定位
## 工作流程
## 输出规范
```

---

## ⚠️ 使用注意

1. **网络依赖**：`historian-storyteller`、`research-assistant`、`research` 需要联网
2. **定时任务**：`research-assistant` 的定时功能依赖系统 Cron
3. **Git 操作**：`git-guardrails-claude-code` 需先运行安装才能生效
4. **Obsidian**：`obsidian-vault` 的保险库路径需在技能配置中设置
5. **AI 视频生成**：`seedance-director`、`hailuo-h3-director` 输出的提示词需复制到对应平台使用
6. **系统工具**：`update-config`、`keybindings-help`、`loop` 等系统技能直接修改 Claude Code 配置

## 📚 推荐技能组合

### 历史题材视频创作流程
1. `/historian-storyteller` - 深度研究历史人物/事件
2. `/historical-vlog-creator` - 生成第一视角 Vlog 脚本
3. `/art-asset-designer` - 拆解场景与人物美术资产
4. `/seedance-director` 或 `/hailuo-h3-director` - 生成视频分镜提示词

### 短剧创作完整流程
1. `/short-drama-writer` - 剧本创作与改编
2. `/art-asset-designer` - 人物与场景设计
3. `/seedance-director` - 分镜头提示词生成

### 音乐 MV 制作流程
1. `/suno-prompter` - 音乐创作与歌词生成
2. `/lyric-mv-storyboard` - 根据歌词生成 MV 分镜
3. `/art-asset-designer` - MV 场景与视觉资产设计
4. `/hailuo-h3-director` - 生成音画同步的视频提示词

## 📄 许可证

个人使用，技能内容归原作者所有。

---

> **提示**：本仓库 skills 需要 Claude Code 环境才能正常使用。
