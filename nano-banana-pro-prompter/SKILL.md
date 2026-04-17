---
name: nano-banana-pro-prompter
description: >
  Nano Banana Pro（Google Gemini 3 Pro Image）图像生成专家提示词框架设计师。
  当用户想为 Nano Banana Pro 生成、优化或改进图像提示词时，立即使用此 skill。
  触发场景：用户描述想要的图像效果、场景、产品摄影、UI设计、信息图表等；
  用户说"帮我写 Nano Banana 提示词"、"用 Nano Banana 生成图"、"Gemini image 提示词"；
  用户提供已有提示词希望优化；用户询问 Nano Banana Pro 的最佳范式；
  用户需要 JSON 格式的结构化提示词输出；任何需要 Nano Banana Pro 图像生成的场景。
  即使用户只是模糊描述了图像想法，也应主动启用此 skill 并生成完整结构化 JSON 提示词。
---

# Nano Banana Pro 图像生成提示词框架

## 模型简介

Nano Banana Pro 是 Google Gemini 3 Pro Image 模型的社区昵称，是目前最精准、可控性最强的图像生成模型之一。核心能力：

- **Thinking 推理模式**：生成前先推理理解意图、物理规律和构图逻辑
- **精准文字渲染**：支持 30+ 语言精准文字，含中文、日文、阿拉伯文等
- **Search Grounding**：接入 Google Search，生成基于真实数据的可视化图像
- **多图参考输入**：最多支持 14 张参考图，实现角色/品牌高度一致性
- **高分辨率**：支持 1K、2K、4K 输出
- **精准区域编辑**：Annotation 编辑，仅修改指定区域，其他部分保持不变

---

## 提示词 JSON 输出格式（标准框架）

每次生成提示词时，**必须以 JSON 格式输出**，结构如下：

```json
{
  "元信息": {
    "用途分类": "产品摄影 | 艺术插画 | 信息图表 | UI设计 | 图像编辑 | 多语言文字 | 创意合成",
    "生成模式": "普通生成 | 图像编辑 | 推理思考 | 实时搜索",
    "语言设置": "中文 | 英文 | 多语言混排",
    "启用推理": true
  },
  "提示词要素": {
    "主体": "谁/什么在画面中，描述人物、物品或场景的核心内容",
    "动作": "正在发生什么，动作、状态或事件",
    "环境": "场景发生的地点、背景、时间",
    "构图": "镜头角度和景别，如低角度仰拍、特写、宽幅电影感",
    "光线": "光线类型、氛围和色调",
    "风格": "艺术风格、媒介或质感",
    "文字渲染": {
      "是否包含文字": false,
      "文字内容": "「画面中需要出现的精确文字」",
      "文字位置": "位于画面的哪个区域",
      "字体风格": "粗体无衬线 | 优雅衬线 | 手写 | 霓虹发光"
    },
    "技术参数": {
      "画面比例": "16:9 | 9:16 | 1:1 | 3:4 | 4:3 | 21:9",
      "输出分辨率": "1K | 2K | 4K",
      "镜头参数": "如 f/1.8、微距、85mm 人像镜头",
      "负向约束": "明确禁止出现的元素或错误"
    },
    "参考图设置": [
      {
        "参考图角色": "角色外貌 | 风格参考 | 环境参考 | 背景参考 | 产品参考",
        "用途说明": "这张参考图的具体作用"
      }
    ]
  },
  "完整提示词（英文）": "整合所有要素后的完整英文提示词，可直接粘贴进 Nano Banana Pro 使用",
  "完整提示词（中文）": "与英文版对应的中文版本，便于理解和校对",
  "编辑指令": "仅图像编辑任务填写：针对特定区域的精确修改说明",
  "使用建议": ["针对本次提示词的补充技巧和注意事项"]
}
```

---

## 六大基础要素（必填）

| 字段名 | 说明 | 示例 |
|------|------|------|
| **主体** | 谁/什么在画面中 | 一位三十多岁的女调酒师 |
| **构图** | 镜头角度与景别 | 低角度仰拍特写、宽幅电影感全景 |
| **动作** | 发生什么 | 调制鸡尾酒、奔跑、展示产品 |
| **环境** | 地点/背景/时间 | 黄金时段的屋顶酒吧、未来感实验室 |
| **风格** | 艺术风格/媒介 | 超写实摄影、油画、漫画、产品棚拍 |
| **编辑指令** | 图像编辑任务专用 | 替换背景、将颜色改为海军蓝 |

---

## 高级要素（进阶增强）

- **画面比例**：9:16 竖版短视频封面、16:9 横版影视、1:1 社交方图、21:9 超宽电影
- **镜头参数**：f/1.8 浅景深、微距特写、50mm 人像、广角 24mm
- **光线**：自然日光、电影感青橙色调、霓虹轮廓光、柔和棚拍光
- **文字渲染**：用「书名号」或双引号包裹精确文字，说明位置和字体风格
- **事实细节**：科学/地理/品牌等真实细节，配合「实时搜索」模式使用
- **参考图设置**：每张参考图指定用途（角色外貌/风格参考/环境参考/产品参考）
- **负向约束**：明确写出禁止出现的错误，如"禁止几何变形"、"禁止文字拼写错误"

---

## 用途分类与最佳实践

### 📦 产品摄影 (Product Photography)
- 明确材质：不要说"外套"，要说"navy blue tweed jacket"
- 指定表面：ceramic mug、reflective black background、marble countertop
- 添加光线细节：soft studio lighting、caustic light reflections、golden-hour

### 🎨 艺术风格生成 (Art & Illustration)
- 指定媒介：oil painting、watercolor、ink line art、vector flat design
- 说明时代感：1980s color film slightly grainy、Art Nouveau、Bauhaus
- 漫画/Manga：使用 "manga panel layout"、"comic book art style"、"high contrast ink"

### 📊 信息图表 (Infographics & Data Viz)
- 说明图表类型：pie chart、timeline、flowchart、bar graph
- 使用负约束：No geometric distortion、Logically consistent labels
- 文字精确：所有标签文字用双引号包裹
- 启用 Search 模式配合实时数据

### 🏪 UI/UX 设计 (UI & Web Design)
- 明确平台：mobile app screen、desktop dashboard、landing page
- 指定风格：minimalist、glassmorphism、dark mode、brutalist
- 文字布局：指定字体层级和精确文案

### 📸 图像编辑 (Photo Editing)
- 描述保留内容："maintain the exact pose and lighting of the subject"
- 一次只改一处："change only the background"
- 区域编辑：使用 Annotation 功能标记目标区域

### 🌐 多语言文字渲染 (Multilingual Text)
- 明确目标语言和原文
- 说明字体要求：bold sans-serif、calligraphic、neon sign font
- 指定文字在画面中的位置和层次

---

## 推理思考模式使用建议

以下场景将 `"启用推理": true` 设为开启：
- 复杂多主体构图（多人场景、多物体交互）
- 物理/光学逻辑复杂（如火与冰的光影交互）
- 信息图表和数据可视化（确保图表逻辑一致）
- 角色一致性要求高的系列图

**在"完整提示词（英文）"末尾追加**：
> "Reason through the lighting interactions before generating."
> "Think step by step about the composition before rendering."

---

## 角色一致性工作流

1. **建立角色参考表（360° Character Sheet）**：先生成 2-3 张同角色不同角度图
2. **锁定锚定描述（Anchor String）**：固定外貌关键词组合
3. **多图输入**：后续生成上传参考图，指定 role 为 `character`
4. **迭代编辑**：图像 80% 正确时，用对话式编辑修改局部，不重新生成

---

## 输出流程

1. 分析用户意图，填写「元信息」中的用途分类和生成模式
2. 补全「提示词要素」六大基础字段（若用户未提供，根据上下文合理推断填写）
3. 按场景补充高级要素（光线、镜头、负向约束等）
4. 输出「完整提示词（英文）」（可直接粘贴使用）和「完整提示词（中文）」（便于校对）
5. 附上「使用建议」，说明注意事项和迭代技巧

> 📖 详细用例和示例提示词见 `references/prompt-examples.md`
> 📐 技术规格参数见 `references/tech-specs.md`
