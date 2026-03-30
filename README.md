# ASHUO Claude Skills

> 个人 Claude Code 技能库，用于增强 Claude 在特定领域的专业能力

## 📦 仓库简介

本仓库包含多个自定义 Claude Code 技能（Skills），每个技能都是针对特定工作流设计的专业模块。通过 `@技能名` 的方式可在 Claude Code 中调用。

## 🗂️ 技能清单

| 技能名 | 类型 | 功能描述 |
|--------|------|----------|
| `historian-storyteller` | 研究+创作 | 历史人物/事件深度研究，输出编剧视角的戏剧素材 |
| `research-assistant` | 信息搜集 | 智能联网搜索、多源交叉验证、定时监控任务 |
| `screenwriting-master` | 创作 | 专业编剧辅助，剧本结构分析与创作指导 |
| `seedance-director` | 视频生成 | 电影级分镜提示词生成器，专为 Seedance 2.x 优化 |
| `skill-creator` | 开发工具 | Claude 官方技能创建模板与规范 |
| `socratic-screenwriter` | 创作 | 苏格拉底式编剧对话，通过提问深化剧本 |
| `video-content-analyst` | 分析 | 视频内容深度分析与解构 |

## 🚀 快速开始

### 安装技能

1. 克隆本仓库到本地：
```bash
git clone https://github.com/GAGAA-HUE/ASHUO-claude-skills.git
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

**触发方式**：
```
@seedance-director 生成一段15秒的武侠对决分镜
```

**参考文档**：
- `references/动作戏摄影指导.md` - 动作戏创作框架
- `references/焦距情绪映射完整表.md` - 镜头心理学参数
- `references/拉班动作词汇库.md` - 动作描述规范

---

### screenwriting-master（编剧大师）

**适用场景**：剧本创作、故事结构分析

**核心能力**：
- 三幕结构分析与设计
- 角色弧光构建
- 对白优化
- 类型片剧本规范

---

### socratic-screenwriter（苏格拉底编剧）

**适用场景**：剧本深度打磨、创意探索

**核心能力**：
- 苏格拉底式提问引导
- 通过对话深化角色
- 发现故事盲点
- 主题挖掘

---

### video-content-analyst（视频内容分析）

**适用场景**：视频分析、竞品研究

**核心能力**：
- 视频结构解构
- 视听语言分析
- 节奏与情绪曲线
- 可复用技法提取

---

### skill-creator（技能创建器）

**适用场景**：开发新的 Claude Code 技能

**核心能力**：
- 官方技能规范模板
- SKILL.md 结构指导
- 技能调试与优化

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
└── examples/             # 示例目录（可选）
    └── example1.txt
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

## 📄 许可证

个人使用，技能内容归原作者所有。

## 🤝 贡献

本仓库为个人技能库，如有建议或改进，欢迎提交 Issue。

---

> **提示**：本仓库 skills 需要 Claude Code 环境才能正常使用。
