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
| `cinedance-higgsfield` | **CINEDANCE V4** - Seedance 2.0 电影提示词导演系统（4D方法论） |
| `acting` | **角色表演系统** - AI视频角色行为/表演指导（目标-障碍-策略） |
| `shanyin-director-master-main` | 山音导演大师：专业 AI 视频生成提示词系统 |
| `hailuo-h3-director` | H3 多模态视频提示词生成器，专为 Hailuo H3（MiniMax）设计 |

### 🖼️ AI 绘画与图像

| 技能名 | 功能描述 |
|--------|----------|
| `lira` | **Lira** - AI图像提示词优化专家（Soul 2.0/Cinema/NBP/Seedream/GPT Image 2） |
| `art-asset-designer` | 美术资产设计师：从剧本拆解人物/场景资产，生成 AI 图像生成提示词 |
| `image-prompt` | 图像提示词生成器：为 AI 绘画工具生成高质量图像提示词 |
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

### 🎥 cinedance-higgsfield（CINEDANCE V4 - Seedance 2.0 提示词导演系统）

**核心理念**：4D 方法论（Deconstruct → Diagnose → Develop → Deliver）

**专业能力**：
- **空间布局控制**：角色位置锚定、视线锁定、身体朝向、地标接近度精确定义
- **光学设计系统**：用视场角度数（FOV°）控制镜头，而非焦距毫米数
  - 47° 标准视角、84° 经典广角、107° 超广角、29° 短焦人像、18° 经典长焦、8° 超长焦观察
- **多镜头剪辑**：支持单镜头长镜头或多镜头 HARD CUT 序列，精确控制每个镜头的时长、空间关系、连续性
- **物理真实性**：重力、质量、惯性、布料延迟、液体流动、粒子运动全面锁定
- **光影优先级**：背光逆光、侧光、关键光比控制，防止平面照明
- **角色/场景参考管理**：@tag 系统精确管理多角色、多道具、多场景引用

**输出格式**：结构化提示词（场景上下文 → 活动引用 → 位置地图 → 首帧空间布局 → 格式模式 → 光学 → 镜头 → 动作时序 → 物理 → 光影 → 音频 → 正向约束）

**适用场景**：电影级视频生成、多镜头叙事、复杂运动控制、专业影视制作

---

### 🎭 acting（角色表演系统 - AI 视频角色行为指导）

**核心公理**：表演是压力下的行为，而非情绪展示

**五大支柱**：
1. **目标（Objective）**：角色在当前场景中想从特定对象那里得到什么（动词化，可执行）
2. **障碍与赌注（Obstacle & Stakes）**：什么阻止他们达成目标？失败的代价是什么？
3. **策略（Tactics）**：具体执行方法（施压、魅力、羞辱、恳求、激怒、讨价还价、威胁、拖延）
4. **节拍（Beats）**：动作最小单位，每个节拍变化必须在行为中可见（停顿、姿势变化、语速变化、视线转移）
5. **潜台词（Subtext）**：角色真正的想法 vs 说出口的话

**专业技术**：
- **倾听与反应**：反应先于台词结束、思考先于言语、评估时刻、从对手传染节奏
- **身体生活**：重心位置、动作质感、手部习惯、物理状态先于心理
- **眼部生命**：微扫视、视线瞄准、真实眨眼率、活跃捕光、眼睛引导思考
- **声音锁定**：每个角色固定的声音身份（年龄/口音/音色/节奏/情感特征）
- **状态链接**：描述"已在状态中"而非"过渡到状态"（AI 模型擅长状态，不擅长转场）

**输出规范**：主档案（角色身份） → 场景改写（当前时刻的具体行为）

**适用场景**：需要真实表演的角色视频、对话场景、情感张力设计、演员指导

---

### 🖼️ lira（AI 图像提示词优化专家）

**核心方法**：4D 方法论（Deconstruct → Diagnose → Develop → Deliver）

**模型路由矩阵**：
| 任务类型 | 首选模型 | 原因 |
|---------|---------|------|
| 角色/选角表 | Higgsfield Soul 2.0 / Cinema Studio AI Cast | Soul ID 锁定同一张脸，AI Cast 自动生成参考表 |
| 场景/电影静帧 | Higgsfield Soul Cinema | 电影级纹理、自然颗粒、21:9 宽银幕支持 |
| 道具/产品 | NBP / GPT Image 2 | 真实产品质感 + 精确文字渲染 |
| 图像编辑（首选） | Nano Banana Pro (NBP) | 基于原图后期处理，最小改动，最大保留 |
| 纹理修复 | Seedream 4.5 | 修复 AI 生成的糟糕纹理（皮肤/布料/表面），不做点编辑 |
| 最精细局部编辑 | GPT Image 2 | 最后手段，全局脏但局部强；也擅长场景视角切换 |

**关键技术**：
- **防崩溃规则**：自然散文而非关键词堆砌、精简胜于冗余、正向描述优于负向、技术光影优于抽象情绪
- **调色板控制**：百分比语法（60% 暖赭石 + 30% 深炭灰 + 10% 锈红）
- **角色一致性**：Soul ID（平台参数）+ 身份锚点（散文）
- **编辑纪律**：最小 CHANGE 块 + 详尽 PRESERVE EXACTLY 块
- **插画漂移防御**：避免触发词（"character reference sheet"、"painterly"），强化写实锚点

**操作模式**：
- **DETAIL 模式**（默认）：收集上下文 → 提问 2-3 个澄清问题 → 优化
- **BASIC 模式**（快速）：修复关键问题 → 应用核心技术 → 立即交付

**适用场景**：角色设计、场景概念图、道具表、精确图像编辑、跨平台提示词迁移

---

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
5. **AI 视频生成**：
   - `cinedance-higgsfield`：输出结构化 Seedance 2.0 提示词，支持多镜头序列
   - `seedance-director`：轻量化提示词，适合快速生成
   - `hailuo-h3-director`：专为 H3 多模态优化
6. **AI 图像生成**：
   - `lira`：支持 Soul 2.0/Cinema、NBP、Seedream 4.5、GPT Image 2 全平台
   - 角色一致性依赖 Soul ID（平台参数），不能仅靠提示词
   - 编辑任务固定顺序：NBP（首选） → Seedream（纹理） → GPT Image 2（精细局部）
7. **角色表演**：`acting` 输出的表演指导需嵌入到视频提示词的"角色行为"部分
8. **系统工具**：`update-config`、`keybindings-help`、`loop` 等系统技能直接修改 Claude Code 配置

---

## 🆕 三大新技能核心差异

| 维度 | cinedance-higgsfield | acting | lira |
|------|---------------------|--------|------|
| **作用对象** | 整个视频镜头（空间+光学+时序） | 镜头内角色的行为/表演 | 单帧图像生成/编辑 |
| **输出格式** | 结构化多段落提示词 | 角色表演段落（嵌入视频提示词） | 自然散文提示词 |
| **核心方法论** | 4D：解构-诊断-开发-交付 | 5柱：目标-障碍-策略-节拍-潜台词 | 4D + 模型路由 |
| **技术特色** | FOV度数光学系统、空间锚定 | 状态链、眼部生命、身体物理 | Soul ID、编辑纪律、防崩溃规则 |
| **适用平台** | Seedance 2.0 | Seedance 2.0（嵌入） | Soul 2.0/Cinema/NBP/Seedream/GPT Image 2 |
| **组合使用** | 作为提示词框架 | 填充框架中的角色表演部分 | 生成参考图供视频引用 |

**协作示例**：
```
1. lira 生成角色参考图（Soul 2.0，Soul ID: @HERO1）
2. acting 设计角色表演档案（目标：说服对方，策略：先施压后恳求）
3. cinedance-higgsfield 生成完整提示词，其中：
   - ACTIVE REFERENCES 引用 @HERO1
   - ACTION TIMING 嵌入 acting 的表演描述
   - OPTICS 选择 29° 短焦人像
   - LIGHTING 锁定背光逆光
```

---

## 📚 推荐技能组合

### 🎬 电影级视频制作完整流程（Seedance 2.0）
1. `/lira` - 生成角色/场景参考图（Soul 2.0/Soul Cinema）
2. `/acting` - 设计角色表演细节（目标-障碍-策略-节拍-潜台词）
3. `/cinedance-higgsfield` - 生成多镜头电影分镜提示词（4D 方法论 + 光学设计）
4. 平台生成 → 如需编辑：`/lira` + NBP/Seedream/GPT Image 2

### 📜 历史题材视频创作流程
1. `/historian-storyteller` - 深度研究历史人物/事件
2. `/historical-vlog-creator` - 生成第一视角 Vlog 脚本
3. `/lira` - 生成历史人物角色图像参考（Soul 2.0）
4. `/acting` - 设计历史人物表演风格
5. `/cinedance-higgsfield` 或 `/seedance-director` - 生成视频分镜提示词

### 🎭 短剧创作完整流程
1. `/short-drama-writer` - 剧本创作与改编
2. `/lira` - 角色选角表 + 场景概念图
3. `/acting` - 每场戏的角色表演设计
4. `/cinedance-higgsfield` - 分镜头提示词生成

### 🎵 音乐 MV 制作流程
1. `/suno-prompter` - 音乐创作与歌词生成
2. `/lyric-mv-storyboard` - 根据歌词生成 MV 分镜
3. `/lira` - MV 场景与视觉资产设计（Soul Cinema）
4. `/acting` - 歌手/演员表演设计
5. `/hailuo-h3-director` - 生成音画同步的视频提示词

### 🎨 图像资产生产线
1. `/lira` - 角色选角（Soul 2.0 或 AI Cast）
2. `/lira` - 场景/环境设计（Soul Cinema，支持 21:9）
3. `/lira` - 道具/产品表（NBP/GPT Image 2）
4. 如需编辑：`/lira` - NBP（首选） → Seedream 4.5（纹理） → GPT Image 2（精细局部）

### 🔧 新技能开发
- `/skill-creator` - 创建、修改、优化新技能

---

个人使用，技能内容归原作者所有。

---

> **提示**：本仓库 skills 需要 Claude Code 环境才能正常使用。
