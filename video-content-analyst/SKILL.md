---
name: video-content-analyst
slash_command: analyze-video
description: >
  视频创作全流程助手：分析视频→沉淀方法论知识库→依据知识库生成创意与剧本。
  当用户上传视频要求分析、或要求生成视频创意、或要求写脚本/剧本时触发。
  支持五种模式：
  (1) /analyze-video  分析视频，审核后写入知识库
  (2) /generate-idea  基于知识库生成选题创意
  (3) /write-script   从选题到完整分镜脚本全流程生成
  (4) /kb-add         手动追加文字笔记到知识库
  (5) /kb-summary     AI主动梳理知识库并更新规律总结
  知识库路径：~/.claude/skills/video-content-analyst/knowledge-base/
usage: |
  /analyze-video <视频路径>
  /generate-idea [主题关键词]
  /write-script [选题描述或创意编号]
  /kb-add <笔记内容>
  /kb-summary
---

# Video Content Analyst v3 — 创作知识大脑

## 架构总览

```
video-content-analyst/          ← skill 安装目录
├── SKILL.md                    ← 本文件，主控逻辑
├── references/
│   ├── content-frameworks.md  ← 叙事框架速查
│   └── platform-context.md    ← 各平台规律
├── scripts/
│   ├── extract.sh              ← 视频提取（ffmpeg）
│   └── kb-write.sh             ← 知识库写入工具
└── kb-template/
    ├── entry-template.md       ← 分析条目模板
    └── index-schema.json       ← 索引结构定义（文档用）

└── knowledge-base/             ← 视频分析知识库（运行时自动创建）
    ├── index.json              ← 综合索引（三维：标签/时间/方法论类型）
    ├── patterns.md             ← AI归纳规律（/kb-summary 更新，生成时自动读取）
    ├── hypotheses.json         ← 待验证假设追踪
    ├── entries/                ← 每次分析沉淀的条目
    └── README.md               ← 知识库说明
```

---

## 知识库索引结构（index.json）

每个条目在 index.json 中的完整记录格式如下。
写入时由 `scripts/kb-write.sh` 自动填充，无需手动编辑。

```json
{
  "entries": [
    {
      "id": "2026-03-20_ai-qitan",
      "file": "entries/2026-03-20_ai-qitan.md",
      "meta": {
        "title": "AI奇谈·止戈为武·流金",
        "date": "2026-03-20",
        "source_platform": "CCTV/微信视频号",
        "duration_seconds": 322
      },
      "tags": ["#时事评论", "#拟人化叙事", "#AI生成画面", "#地缘政治"],
      "methodology": {
        "hook_type": "金句前置",
        "structure_model": "矛盾建立→势力登场→冲突激化→多极化收口",
        "visual_style": "AI高拟真+拟人动物",
        "language_tone": "古白话+现代口语混搭"
      },
      "effectiveness": {
        "hook_strength": 5,
        "information_density": 3,
        "virality_potential": 5,
        "notes": "截图传播性极强，表情包素材丰富"
      },
      "reuse_count": 0,
      "hypotheses": ["金句前置比悬念型开场留存率更高（待验证）"],
      "created_at": "2026-03-20T11:04:08Z",
      "last_cited": null
    }
  ],
  "tag_index": {
    "#时事评论": ["2026-03-20_ai-qitan"],
    "#拟人化叙事": ["2026-03-20_ai-qitan"]
  },
  "methodology_index": {
    "hook_type": {
      "金句前置": ["2026-03-20_ai-qitan"],
      "悬念型": [],
      "痛点共鸣": [],
      "反常识": []
    },
    "structure_model": {
      "AIDA": [],
      "PAS": [],
      "故事弧": [],
      "自定义": ["2026-03-20_ai-qitan"]
    },
    "visual_style": {
      "真人出镜": [],
      "AI生成": ["2026-03-20_ai-qitan"],
      "混合": [],
      "动画": []
    }
  }
}
```

**三维检索说明**：
- `tag_index`：按内容标签反查条目列表（如 `#时事评论` → 所有时事类条目）
- `methodology_index.hook_type`：按钩子类型聚合，用于生成创意时调取最佳开场策略
- `methodology_index.visual_style`：按视觉风格聚合，用于脚本生成时匹配画面策略
- `effectiveness.reuse_count`：每次 /generate-idea 或 /write-script 引用该条目时自动+1，积累后可识别"高价值条目"

---

## 模式一：/analyze-video — 分析视频并沉淀知识库

### Step 1：提取视频信息
```bash
bash scripts/extract.sh "$VIDEO_PATH"
# 输出：WORK_DIR 路径，含 meta.json / frames/ / audio.txt
```

### Step 2：四维分析
见本文件底部「四维分析框架」章节。

### Step 3：生成草稿，等待审核

```
📋 分析完成，以下是准备写入知识库的草稿：

【标题】xxx
【标签】#xxx #xxx #xxx
【钩子类型】xxx
【结构模型】xxx
【视觉风格】xxx
【语言调性】xxx
【核心可复用原则】
  1. xxx
  2. xxx
  3. xxx
【效能评分】
  钩子强度：⭐x/5
  信息密度：⭐x/5
  传播势能：⭐x/5
【待验证假设】
  - xxx

是否写入知识库？
  [Y] 写入   [E] 编辑后写入   [N] 不写入
```

---

## 模式二：/generate-idea — 基于知识库生成创意

### 执行流程

1. **读取知识库状态**：
```bash
KB_DIR="$HOME/.claude/skills/video-content-analyst/knowledge-base"
cat "$KB_DIR/patterns.md"          # 已归纳规律
cat "$KB_DIR/index.json"           # 方法论分布
# 按 reuse_count 降序读取前5条高价值条目
python3 -c "
import json
with open('$KB_DIR/index.json') as f:
    data = json.load(f)
top = sorted(data['entries'], key=lambda x: x['effectiveness']['virality_potential'], reverse=True)[:5]
for e in top:
    print(e['id'], e['file'])
"
```

2. **生成10条创意**，每条格式：

```
【创意 #N】
选题：xxx
核心角度：xxx
开场钩子策略：xxx
  └ 知识库依据：「条目名」的「钩子类型」，传播势能评分 ⭐x/5，已被引用 N 次
目标受众：xxx
平台适配：xxx（预计时长 x:xx）
传播势能预判：⭐x/5（理由：xxx）
```

3. 询问用户选择或重新生成，选定后进入 /write-script 流程。

---

## 模式三：/write-script — 全流程脚本生成

三阶段交互，逐阶段确认，不跳步。

---

### 阶段一：策略书

```
## 选题策略书

选题：xxx
核心角度：xxx（一句话）
目标受众：xxx
平台：xxx → 预计时长：x:xx
结构模型：xxx

📚 知识库调用说明：
  开头钩子 → 「条目」·「策略名」（引用后该条目 reuse_count +1）
  叙事结构 → 「条目」·「结构模型」
  语言风格 → 「条目」·「调性描述」
  ⚠️ 知识库空白维度：xxx（将从 references/ 通用框架推导）

[1] ✅ 确认，进入大纲
[2] ✏️ 调整平台/时长
[3] ✏️ 调整结构模型
[4] ✏️ 调整受众定位
```

---

### 阶段二：节拍表

```
## 视频节拍表（共 N 段，总时长 x:xx）

| # | 时间段 | 段落名 | 核心任务 | 情绪节拍 | 留存风险 |
|---|--------|--------|---------|---------|---------|
| 1 | 00:00–00:15 | 开场钩子 | 制造认知冲突 | 🔴 高张力 | 低 |
| 2 | 00:15–01:00 | 背景建立 | 交代核心矛盾 | 🟡 中张力 | ⚠️ 易拖沓 |
| … | … | … | … | … | … |

结构诊断：
  前15秒钩子强度：⭐x/5
  最高风险段：第 N 段（建议：xxx）
  整体情绪曲线：xxx → xxx → xxx

[1] ✅ 确认，生成完整脚本
[2] ✏️ 调整第 N 段
[3] ✏️ 整体重排
```

---

### 阶段三：完整分镜脚本

脚本头部：
```
# 《xxx》完整分镜脚本
> 平台：xxx ｜ 目标时长：x:xx ｜ 结构：xxx
> 生成依据：知识库 N 条条目，patterns.md 更新于 YYYY-MM-DD
```

**每个分镜块包含六层，对应不同下游消费者**：

```
### § N · [段落名]｜[时间段]｜[情绪节拍]

━━ 🎬 画面指令（→ AI生图/视频工具）━━━━━━━━━━━
景别：特写 / 中景 / 全景 / 航拍
运动：静止 / 缓推 / 横摇 / 环绕
色调：xxx（明确说明色温与饱和度倾向）
AI生图提示词：
  正向：[主体], [环境], [风格], [光线], [构图], cinematic, high detail, 8k
  负向：blurry, watermark, text, low quality

━━ 🎙 台词 / 旁白（→ AI配音工具）━━━━━━━━━━━
旁白：（每句≤12字，句末标注语气：[平稳/上扬/停顿/加重]）
  > xxx [平稳]
  > xxx [停顿3秒]
  > xxx [加重]
对话（如有）：
  角色A：xxx
  角色B：xxx
情绪标注（供AI配音参考）：[冷静叙述 / 紧张急促 / 低沉有力 / 轻松幽默]

━━ 📝 字幕设计（→ 剪辑师）━━━━━━━━━━━━━━━
显示文字：xxx
出现时机：第 x 秒 / 与台词同步 / 台词后 x 秒
视觉处理：普通字幕 / 关键词放大 / 逐字出现 / 动态强调
字幕备注：xxx（如需特殊处理）

━━ ✂️ 剪辑指令（→ 剪辑师）━━━━━━━━━━━━━━━
本段时长：xx 秒
镜头数量：x 个（平均 x 秒/镜头）
切点节奏：[硬切 / 叠化 / 音效切点]
转场方式：[直接切 / 推进转场 / 叠化 x 帧]
剪辑重点：xxx

━━ 📚 知识库依据━━━━━━━━━━━━━━━━━━━━━
本段来源：「条目名」→「规律描述」

━━ ⚠️ 创作警示━━━━━━━━━━━━━━━━━━━━━━━
xxx（此段最易犯的错误，或来自知识库的反面案例）
```

脚本结尾附自检清单：
```
## 交付前自检

□ 前15秒有明确钩子，且≥⭐4/5强度？
□ 每段情绪目标清晰，不存在连续2段以上低张力？
□ 台词每句≤12字？
□ AI生图提示词包含正向+负向？
□ 每段剪辑指令中有明确的切点依据？
□ 至少一处知识库规律被显式引用？
□ 结尾有明确的情绪收口或行动召唤？
```

脚本完成后询问：
```
📄 脚本已完成（N 段，约 x:xx）

是否将本次「选题策略 + 结构逻辑」写入知识库？
  [Y] 写入草稿进入审核
  [E] 只写入选题策略，不含脚本细节
  [N] 不写入
```

---

## 模式四：/kb-add — 手动追加笔记

```bash
KB_NOTES="$HOME/.claude/skills/video-content-analyst/knowledge-base/notes/manual-notes.md"
mkdir -p "$(dirname $KB_NOTES)"
echo "\n---\n$(date '+%Y-%m-%d %H:%M') 手动笔记\n$*" >> "$KB_NOTES"
echo "✅ 已追加"
```

---

## 模式五：/kb-summary — 规律梳理与 patterns.md 更新

读取所有 entries + notes，输出：

```
## 知识库规律总结（基于 N 条条目，更新于 YYYY-MM-DD）

### 高频钩子类型（按使用次数）
1. xxx（N 次，平均传播势能 ⭐x/5）
2. xxx

### 最可靠的结构模型
1. xxx（出现于 N 条，平均完播风险最低）

### 视觉策略规律
...

### 语言风格规律
...

### 高价值条目 TOP 3（reuse_count 最高）
1. 「xxx」— 被引用 N 次，核心贡献：xxx

### 待验证假设（共 N 条）
- [🕐 待验证] xxx（首次记录：YYYY-MM-DD，相关条目：N 个）
- [✅ 已验证] xxx（验证于 YYYY-MM-DD，结论：xxx）
- [❌ 已推翻] xxx

### 知识库盲区（建议补充的内容类型）
- xxx（当前 0 个样本）
```

询问是否覆盖 `patterns.md`，确认后写入。

---

## 四维分析框架（/analyze-video 时执行）

### 维度一：创意与选题策略
- 选题切入角（反常识 / 情绪共鸣 / 利益相关 / 新奇感）
- 受众锁定与前5秒筛选机制
- 竞争差异化：不可替代性
- 选题公式：`[触发点] + [受众痛点/好奇心] + [独特视角]`

### 维度二：脚本结构与叙事
- 时间轴结构（段落名 / 功能 / 手法）
- 前15秒钩子设计（类型+强度评分）
- 节奏控制与情绪曲线
- 转折设计与结尾策略

### 维度三：视觉与剪辑风格
- 画面构成与视觉节奏（平均镜头时长）
- 信息密度层（字幕 / 标注 / 贴纸逻辑）
- 注意力引导策略
- AI生图风格（如适用）：提示词规律提炼

### 维度四：文案与语言风格
- 语言调性与一致性
- 句式特征（标志性结构，字数规律）
- 信息包装方式（类比 / 举例 / 可视化）
- 品牌语言识别（口头禅 / 开场白 / 收尾语）

---

## 分析质量标准（所有模式通用）

每条输出必须通过：
1. **可操作性**：能直接指导具体创作动作？
2. **特异性**：说的是这个视频/这个创意独有的特征，不是通用废话？
3. **知识库关联**：生成模式下，每条策略是否显式标注了来源条目？

不符合标准替换为 `[待补充：需要更多信息]`，严禁编造。

---

## 参考资料
- `references/content-frameworks.md`：AIDA / PAS / StoryBrand 等叙事框架
- `references/platform-context.md`：抖音 / B站 / 视频号 / YouTube 平台规律
