# ASHUO Claude Skills

> 个人 Claude Code 技能库，用于增强 Claude 在特定领域的专业能力

## 📦 仓库简介

本仓库包含多个自定义 Claude Code 技能（Skills），每个技能都是针对特定工作流设计的专业模块。通过 `@技能名` 的方式可在 Claude Code 中调用。

## 🗂️ 技能清单

| 技能名 | 类型 | 功能描述 |
|--------|------|----------|
| `extract-video` | 文件解析 | 提取视频信息、关键帧、音频、字幕 |
| `historian-storyteller` | 研究+创作 | 历史人物/事件深度研究，输出编剧视角的戏剧素材 |
| `image-prompt-engineer` | AI 绘画 | 图像提示词工程师：为 Seedream、Nano Banana、即梦、可灵等中文 AI 绘画模型生成精准提示词 |
| `nano-banana-pro-prompter` | AI 绘画 | Nano Banana Pro（Google Gemini 3 Pro Image）结构化 JSON 提示词框架 |
| `novel-crawler` | 网络爬取 | 爬取网络小说并保存为本地 txt 文件，支持通用网站适配 |
| `paiwotscdashi` | 视频生成 | 拍我视频大师：时间轴驱动的 AI 视频提示词生成器，音画同步专家 |
| `promo-film-creative` | 创作 | 国际级宣传片创意启发大师：城市/品牌/产品/公益宣传片创意开发，融合戛纳/D&AD 等国际奖项获奖逻辑 |
| `read-docx` | 文件解析 | 读取 Microsoft Word 文档内容并转为纯文本/Markdown |
| `read-pptx` | 文件解析 | 读取 Microsoft PowerPoint 演示文稿文本内容 |
| `read-xlsx` | 文件解析 | 读取 Microsoft Excel 电子表格内容并结构化输出 |
| `research-assistant` | 信息搜集 | 智能联网搜索、多源交叉验证、定时监控任务 |
| `screenwriting-master` | 创作 | 专业编剧辅助，剧本结构分析与创作指导 |
| `seedance-director` | 视频生成 | 电影级分镜提示词生成器，专为 Seedance 2.x 优化 |
| `shanyin-director-master-main` | 视频生成 | 山音导演大师：专业AI视频生成提示词系统 |
| `short-drama-writer` | 创作 | 短剧编剧大师：小说/IP 改编、市场分析、原创短剧、分集剧本与分镜，覆盖国内抖快微短剧与海外 Reelshort/DramaBox 出海赛道 |
| `wan27-image-prompter` | AI 绘画 | Wan 2.7 图像提示词生成专家（阿里万象） |
| `skill-creator` | 开发工具 | Claude 官方技能创建模板与规范 |
| `socratic-screenwriter` | 创作 | 苏格拉底式编剧对话，通过提问深化剧本 |
| `video-content-analyst` | 分析+创作 | 视频创作知识大脑：分析视频→沉淀知识库→生成创意与分镜脚本 |
| `video-style-prompt-advisor` | AI 绘画 | 视频视觉风格定调顾问：为视频项目推荐视觉风格方向，输出纯风格层、可复用的 GPT image2 中文自然语言风格预设提示词 |

## 🚀 快速开始

### 安装技能

1. 克隆本仓库到本地：
```bash
git clone https://github.com/GAGAA-HUE/ASHUO-claude-skills.git ~/.claude/skills
```

2. 将技能文件夹复制到 Claude Code 技能目录：
```bash
# Windows
cp -r historian-storyteller %USERPROFILE%\.claude\skills\
cp -r seedance-director %USERPROFILE%\.claude\skills\
# ... 其他技能
```

3. 在 Claude Code 中使用：
```
@historian-storyteller 帮我研究拿破仑的生平
```

## 📖 技能详解

### historian-storyteller（历史洞察家）

**适用场景**：历史题材内容创作

**核心能力**：
- 历史人物/事件深度研究
- 动态时间线构建（带标签系统）
- 编剧视角的戏剧素材提炼
- 叙事钩子与人物弧光分析

**触发方式**：
```
@historian-storyteller 我想做一期关于诸葛亮的视频
```

---

### image-prompt-engineer（图像提示词工程师）

**适用场景**：AI 绘画提示词生成、文生图、图生图、风格迁移

**核心能力**：
- 支持主流中文 AI 绘画模型（Seedream、Nano Banana、即梦、可灵等）
- 精准提示词结构：主体 > 动作 > 场景 > 风格 > 质量 > 技术参数
- 模型特性适配（写实人像、东方美学、商业摄影、插画风格等）
- 负面提示词优化
- 比例参数支持（如 `--ar 16:9`）

**触发方式**：
```
@image-prompt-engineer 画一张古风女子在樱花树下的图
@image-prompt-engineer 生成一张赛博朋克风格的城市夜景
```

**支持模型**：
- **Seedream**（字节跳动/即梦）：写实人像、东方美学、商业摄影
- **Nano Banana**（美团）：插画风格、动漫人物、场景渲染
- **可灵 AI**（快手）：视频生成、动态场景、电影感画面

---

### paiwotscdashi（拍我视频大师）

**适用场景**：AI 视频生成、多镜头叙事、音画同步设计

**核心能力**：
- 时间轴驱动的提示词生成（自然语言解析）
- 音画精确同步（硬同步/节拍同步/提前同步/延迟同步）
- 多镜头叙事拆分与连贯性保证
- 焦距情绪映射（14mm-400mm+ 心理学效应）
- 三层音频结构设计（环境/音乐/音效）

**触发方式**：
```
@paiwotscdashi 我想做一个15秒的治愈系视频，有海浪声和夕阳
```

**参考文档**：
- `references/time-axis-templates.md` - 常见视频类型时间轴模板
- `references/audio-sync-guide.md` - 音画同步技术指南
- `references/lens-emotion-mapping.md` - 焦距情绪映射表

---

### research-assistant（研究助手）

**适用场景**：信息搜集、新闻监控、数据验证

**核心能力**：
- 深度多源搜索
- 交叉验证引擎（可信度评分）
- 定时监控任务（Cron 定时）
- 结构化报告（Markdown + HTML）

**触发方式**：
```
@research-assistant 搜集关于AI Agent最新发展的资料
@research-assistant 每天早上10点推送AI新闻简报
```

---

### seedance-director（Seedance 分镜导演）

**适用场景**：AI 视频生成、分镜脚本制作

**核心能力**：
- 电影级分镜提示词生成
- 专业摄影参数控制（5C原则、动机光、焦点调度）
- 拉班动作分析系统
- 音效三层结构设计
- **专业打斗场景支持**（武侠、格斗、特效战斗）
- **Shot 级美术设定隔离**：每个 Shot 拥有独立的【风格与美术设定】与【素材约束】声明

**近期更新**（2025-03-31）：
- **架构重构**：输出结构从"单元(Unit)"改为"镜头(Shot)"，每个 Shot 独立生成
- **自然语言化**：提示词正文以流畅自然语言呈现，整合场景/摄影机/焦点/构图/光影等要素，不再使用分段标签
- **字符限制**：单个 Shot 提示词长度上限 2000 字符（含空格与格式标记）
- **时间轴**：Shot 内时间从 0s 重新计算

**触发方式**：
```
@seedance-director 生成一段15秒的武侠对决分镜
```

**参考文档**：
- `references/动作戏摄影指导.md` - 动作戏创作框架
- `references/焦距情绪映射完整表.md` - 镜头心理学参数
- `references/拉班动作词汇库.md` - 动作描述规范

---

### screenwriting-master（山音超级编剧大师）

**适用场景**：全格式影视剧本创作（概念超短片 / 5-10 分钟叙事短片 / 90 分钟长片 / 多集剧集）

**核心能力**：
- 四种格式全覆盖：概念超短片、叙事短片、长片（商业/文艺）、多集剧集
- 人物设计、叙事结构、对白创作
- 类型片模板与节拍表
- 与 `shanyin-director-master-main` 联动输出导演分镜

---

### short-drama-writer（短剧编剧大师）

**适用场景**：小说/IP 改编短剧、爆款市场分析、原创短剧、分集剧本与分镜，覆盖国内抖音/快手/微短剧与海外 Reelshort/DramaBox/ShortMax 出海赛道

**核心能力**：
- `/adapt-novel`：小说/IP 改编为标准分集剧本（爽点提炼、删繁就简、节奏重构、对白现代化、钩子重分布）
- `/market-analysis`：国内外爆款规律、赛道热度、题材公式、选题评估（霸总/战神/穿越 vs Alpha/Werewolf/Revenge）
- `/original-drama`：从零原创短剧（题材→人物→大纲→分集剧本）
- `/shot-script`：在标准分集基础上叠加分镜视听语言
- `/diagnose`：剧本五维诊断（节奏/钩子/情绪弧线/对白效率/角色动机）
- `/episode-outline`：快速集数大纲与钩子节拍表

**参考文档**：
- `references/novel-adaptation.md` — 小说改编方法论
- `references/market-intelligence.md` — 国内外短剧市场情报
- `references/original-drama-workflow.md` — 原创短剧工作流
- `references/shot-script-guide.md` — 分镜视听指南

**触发方式**：
```
@short-drama-writer 这本小说能改短剧吗
@short-drama-writer 现在出海什么短剧好卖
```

---

### promo-film-creative（国际级宣传片创意大师）

**适用场景**：城市/国家形象片、品牌宣传片、产品发布片、公益/社会议题片创意开发

**核心能力**：
- 融合 Cannes Lions、D&AD、One Show、Clio Awards、Sundance 等国际奖项获奖逻辑
- 创意概念（Big Idea）开发与差异化策略
- 叙事结构与视听语言设计
- 文化洞察与情感共鸣点挖掘

**触发方式**：
```
@promo-film-creative 帮我做一个城市形象片的创意方案
```

---

### socratic-screenwriter（苏格拉底编剧导师）

**适用场景**：剧本深度打磨、创意探索、编剧学习

**核心能力**：
- 苏格拉底式提问引导
- 通过对话深化角色
- 发现故事盲点
- 主题挖掘

---

### video-content-analyst（视频创作知识大脑）

**适用场景**：视频分析、竞品研究、创意生成、分镜脚本创作

**核心能力**：
- `/analyze-video`：分析视频并沉淀到知识库
- `/generate-idea`：基于知识库生成选题创意
- `/write-script`：从选题到完整分镜脚本全流程生成
- `/kb-add` / `/kb-summary`：手动追加笔记、AI 梳理规律

**知识库现状**：
- 22 部短片分析条目（13 部奥斯卡获奖短片 + 4 部 B 站全站前 5 爆款 + 5 部 AI 短片）
- 18 种高频钩子类型、16 种可靠结构模型
- 自动生成 `patterns.md` 规律总结

**触发方式**：
```
@video-content-analyst /analyze-video <视频路径>
@video-content-analyst /generate-idea 我想做一个关于亲情的短片
@video-content-analyst /write-script 一个关于重逢的故事
```

---

### shanyin-director-master-main（山音导演大师）

**适用场景**：AI 视频生成、专业分镜脚本、电影级提示词

**核心能力**：
- 专业AI视频生成提示词系统
- 电影级分镜设计与镜头语言
- 场景构建与视觉叙事
- 动作设计与表演指导

**触发方式**：
```
@shanyin-director-master-main 生成一段古风武侠对决的分镜
```

---

### nano-banana-pro-prompter（Nano Banana Pro 提示词专家）

**适用场景**：Google Gemini 3 Pro Image（社区昵称 Nano Banana Pro）提示词生成

**核心能力**：
- 结构化 JSON 输出（元信息、提示词要素、完整提示词、使用建议）
- 支持推理思考模式、实时搜索模式、图像编辑模式
- 精准文字渲染（30+ 语言，含中文、日文、阿拉伯文）
- 多图参考输入（最多 14 张）、区域 Annotation 编辑
- 用途分类：产品摄影、艺术插画、信息图表、UI 设计、多语言文字、创意合成

**触发方式**：
```
@nano-banana-pro-prompter 帮我写一个产品摄影提示词
@nano-banana-pro-prompter 生成一张带中文文字的电商海报
```

---

### wan27-image-prompter（Wan 2.7 图像提示词专家）

**适用场景**：阿里 Wan 2.7（万象）图像模型提示词生成

**核心能力**：
- 基于阿里巴巴官方《Wan 2.7-Image 图像生产力指南》
- 千人千面：人物五官、表情、妆容细粒度控制
- 调色盘：参考图色彩提取与迁移
- 复杂图文渲染：支持4000字符图文混排
- 组图生成：最高12张连续组图，保持一致性
- 支持 `wan2.7-image-pro`（4K+Thinking Mode）和 `wan2.7-image`（快速版）

**触发方式**：
```
@wan27-image-prompter 生成一张赛博朋克风格的街头场景
@wan27-image-prompter 为这个产品生成电商主图提示词
```

---

### video-style-prompt-advisor（视频视觉风格定调顾问）

**适用场景**：视频项目前期视觉定调、风格参考图生成、mood board 制作

**核心能力**：
- 针对宣传片、短片、广告、MV、纪录片、动画、短视频、综艺片头等视频类型推荐视觉风格方向
- 输出纯风格层、可复用的 GPT image2 中文自然语言风格预设提示词
- 风格预设只描述"怎么拍"（色彩/光线/构图/质感/对比饱和度），不包含具体人物/场景/物品
- 用户可将风格预设与任意内容描述自由组合，生成风格统一的参考图
- 内置 7 大视频类型风格谱系库，支持风格混搭组合

**触发方式**：
```
@video-style-prompt-advisor 帮我定个综艺片头的视觉调性
@video-style-prompt-advisor 这个MV适合什么风格，出GPT image2提示词
```

**参考文档**：
- `references/style-library.md` — 视频风格谱系库（7 大类型 30+ 风格方向）

---

### skill-creator（技能创建器）

**适用场景**：开发新的 Claude Code 技能

**核心能力**：
- 官方技能规范模板
- SKILL.md 结构指导
- 技能调试与优化
- 支持 eval 测试与 benchmark 评估

**相关目录**：
- `research-assistant-workspace/` — `research-assistant` 的 benchmark 测试数据与评估报告

---

### novel-crawler（小说爬虫）

**适用场景**：下载网络小说、保存在线小说到本地

**核心能力**：
- 通用小说网站适配（自动识别章节结构）
- 单线程稳定爬取（防封策略）
- 智能内容清理（移除广告、导航）
- 自动编码检测（UTF-8、GBK、GB2312）
- 合并输出为单个 txt 文件

**触发方式**：
```
@novel-crawler 帮我下载这个小说 https://example.com/novel/123/
```

**使用说明**：
1. 提供小说目录页或第一章 URL
2. Claude 自动分析页面结构，识别章节列表
3. 确认爬取范围（起始/结束章节）
4. 单线程顺序爬取，每章间隔 1-2 秒
5. 保存为格式化的 txt 文件

---

### extract-video（视频解析）

**适用场景**：视频文件分析、内容提取、转码处理

**核心能力**：
- 提取视频基本信息（分辨率、时长、码率、编码格式）
- 提取关键帧截图
- 提取音频轨道
- 提取/生成字幕（支持内嵌字幕和 Whisper 转写）

**触发方式**：
```
/extract-video <视频路径> [info|frames|audio|subtitle]
```

---

### read-docx（Word 文档读取）

**适用场景**：分析、搜索、总结 Microsoft Word 文档

**核心能力**：
- 提取 `.docx` 文档纯文本内容
- 转换为 Markdown 格式保留层级结构
- 提取表格内容（Markdown 表格形式）
- 自动检查和安装 `python-docx` 依赖

**触发方式**：
```
/read-docx <文档路径>
```

---

### read-pptx（PPT 演示文稿读取）

**适用场景**：总结、分析、提取 PowerPoint 文字信息

**核心能力**：
- 按幻灯片顺序提取文本内容
- 保留标题和正文层级结构
- 自动检查和安装 `python-pptx` 依赖

**触发方式**：
```
/read-pptx <演示文稿路径>
```

---

### read-xlsx（Excel 表格读取）

**适用场景**：查看表格数据、分析特定 Sheet、提取单元格内容

**核心能力**：
- 列出所有工作表（Sheet）
- 读取指定 Sheet 的单元格数据
- 以 Markdown 表格形式结构化输出
- 支持 `.xlsx` 和 `.xls` 格式
- 自动检查和安装 `openpyxl` / `xlrd` 依赖

**触发方式**：
```
/read-xlsx <表格路径> [Sheet名或索引]
```

## 🔄 同步与更新

### 添加新技能

1. 创建新的技能文件夹
2. 编写 `SKILL.md` 文件
3. 提交到本仓库
4. 在其他设备上 `git pull` 同步

### 多设备同步

```bash
# 设备A：推送更新
git add .
git commit -m "添加新技能 xxx"
git push origin main

# 设备B：拉取更新
git pull origin main
```

## 📝 技能开发规范

### 文件结构

```
skill-name/
├── SKILL.md              # 技能定义文件（必需）
├── references/           # 参考资料目录
│   ├── 参考文档1.md
│   └── 参考文档2.md
├── scripts/              # 辅助脚本目录（可选）
│   └── extract.sh
├── examples/             # 示例目录（可选）
│   └── example1.txt
└── knowledge-base/       # 知识库目录（部分技能使用）
    ├── entries/
    ├── patterns.md
    └── index.json
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
...

## 工作流程
...

## 输出规范
...
```

## ⚠️ 使用注意

1. **技能调用**：使用 `@技能名` 格式触发
2. **参考文件**：部分技能会自动加载 `references/` 目录下的文档
3. **网络依赖**：`historian-storyteller` 和 `research-assistant` 需要联网
4. **定时任务**：`research-assistant` 的定时功能依赖系统 Cron
5. **工作目录**：`video-content-analyst` 会在 `work/` 目录下生成视频提取文件

## 📄 许可证

个人使用，技能内容归原作者所有。

## 🤝 贡献

本仓库为个人技能库，如有建议或改进，欢迎提交 Issue。

---

> **提示**：本仓库 skills 需要 Claude Code 环境才能正常使用。
