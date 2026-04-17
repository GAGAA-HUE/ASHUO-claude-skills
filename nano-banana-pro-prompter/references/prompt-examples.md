# Nano Banana Pro 提示词示例库

## 示例一：产品摄影（香水广告）

```json
{
  "元信息": {
    "用途分类": "产品摄影",
    "生成模式": "普通生成",
    "语言设置": "英文",
    "启用推理": false
  },
  "提示词要素": {
    "主体": "一瓶带金色装饰的精致玻璃香水瓶",
    "动作": "静置展示",
    "环境": "反光黑色台面，细小烟雾缓缓升起",
    "构图": "低角度正面居中取景",
    "光线": "顶部戏剧性聚光灯，瓶身表面高光闪耀",
    "风格": "奢侈品化妆品广告，超写实摄影",
    "文字渲染": {
      "是否包含文字": false
    },
    "技术参数": {
      "画面比例": "4:5",
      "输出分辨率": "4K",
      "镜头参数": "微距 f/2.8",
      "负向约束": "禁止出现摄影棚设备反光，禁止多余道具入镜"
    },
    "参考图设置": []
  },
  "完整提示词（英文）": "A sleek glass perfume bottle with gold accents placed elegantly on a reflective black surface with soft smoke tendrils rising. Low angle shot, centered framing. Dramatic spotlight from above, glossy highlights on the bottle surface. Luxury cosmetics advertisement, photorealistic. f/2.8 macro. 4K. No reflections of studio equipment, no visible props.",
  "完整提示词（中文）": "一瓶带金色装饰的精致玻璃香水瓶，优雅地放置在反光黑色台面上，细小烟雾缓缓升起。低角度正面取景，顶部戏剧性聚光灯打亮，瓶身高光闪耀。奢侈品化妆品广告风格，超写实摄影。微距镜头 f/2.8，4K 画质。禁止摄影棚设备反光。",
  "编辑指令": "",
  "使用建议": [
    "可上传真实产品图作为参考图，角色设为「产品参考」",
    "如需加品牌名称，在「文字渲染」中填写精确文字内容"
  ]
}
```

---

## 示例二：信息图表（实时数据可视化）

```json
{
  "元信息": {
    "用途分类": "信息图表",
    "生成模式": "实时搜索",
    "语言设置": "中文",
    "启用推理": true
  },
  "提示词要素": {
    "主体": "全球平均气温变化趋势折线图",
    "动作": "数据可视化展示",
    "环境": "干净白色背景，现代数据设计风格",
    "构图": "居中横幅布局",
    "光线": "均匀平光，无阴影",
    "风格": "现代数据可视化，扁平设计，编辑风",
    "文字渲染": {
      "是否包含文字": true,
      "文字内容": "「全球气温上升趋势 1975–2025」",
      "文字位置": "顶部居中作为标题",
      "字体风格": "粗体无衬线字体，深炭灰色"
    },
    "技术参数": {
      "画面比例": "16:9",
      "输出分辨率": "2K",
      "镜头参数": "",
      "负向约束": "禁止几何变形，禁止图表标签错误，禁止装饰性杂乱元素"
    },
    "参考图设置": []
  },
  "完整提示词（英文）": "Search for accurate global average temperature data from 1975 to 2025. Create a clean modern data infographic visualizing this trend as a line chart on a white background. Title: \"Global Temperature Rise 1975-2025\" in bold sans-serif at the top center. Include labeled axes (Year / Temperature °C), data source note at bottom. Flat editorial design, 16:9, 2K. Reason through chart logic before generating. No geometric distortion, no inaccurate labels.",
  "完整提示词（中文）": "搜索1975至2025年全球平均气温真实数据，创建一张现代风格折线图信息图表，白色背景。顶部居中标题：全球气温上升趋势 1975–2025，粗体无衬线字体，深灰色。包含横轴（年份）和纵轴（温度°C）标签，底部注明数据来源。扁平编辑设计风格，16:9，2K。生成前先推理图表逻辑。禁止几何变形，禁止标签错误。",
  "编辑指令": "",
  "使用建议": [
    "实时搜索模式确保数据真实准确，务必开启",
    "必须启用推理模式，保证图表逻辑一致性",
    "如需中英双语标签，在文字渲染中同时列出两种语言"
  ]
}
```

---

## 示例三：图像编辑（背景替换保留主体）

```json
{
  "元信息": {
    "用途分类": "图像编辑",
    "生成模式": "图像编辑",
    "语言设置": "英文",
    "启用推理": false
  },
  "提示词要素": {
    "主体": "上传图像中的原始主体（人物或物品）",
    "动作": "保持主体完全不变",
    "环境": "替换背景为夜晚东京霓虹街道，雨湿路面倒映霓虹灯光",
    "构图": "保持原图主体的位置和比例不变",
    "光线": "新背景霓虹灯光与主体边缘自然融合",
    "风格": "电影感，超写实摄影",
    "文字渲染": {
      "是否包含文字": false
    },
    "技术参数": {
      "画面比例": "16:9",
      "输出分辨率": "2K",
      "镜头参数": "",
      "负向约束": "禁止改变主体的服装、面孔或姿势"
    },
    "参考图设置": [
      {
        "参考图角色": "角色外貌",
        "用途说明": "原始主体参考，保持外貌一致"
      }
    ]
  },
  "完整提示词（英文）": "Replace the background of the uploaded image with a realistic Tokyo neon street at night, rain-soaked pavement reflecting neon signs. Maintain the exact position and scale of the subject. Match the neon lighting to interact naturally with the subject's edges. Cinematic, photorealistic. Do not alter the subject's clothing, face, or pose.",
  "完整提示词（中文）": "将上传图像的背景替换为夜晚东京霓虹街道，雨湿路面倒映霓虹灯光。保持主体原有位置和比例不变。霓虹光照与主体边缘自然融合。电影感，超写实。禁止改变主体的服装、面孔或姿势。",
  "编辑指令": "仅替换背景区域。主体轮廓必须保持像素级准确。优化主体与新环境之间的边缘光线融合。",
  "使用建议": [
    "上传原图后，建议使用 Annotation 功能手动框选背景区域，精准度更高",
    "若边缘融合不自然，追加提示：改善主体与背景之间的边缘融合",
    "一次只修改一处，不要同时要求换背景又换服装"
  ]
}
```

---

## 示例四：推理思考模式（复杂物理交互）

```json
{
  "元信息": {
    "用途分类": "创意合成",
    "生成模式": "推理思考",
    "语言设置": "英文",
    "启用推理": true
  },
  "提示词要素": {
    "主体": "一套水晶冰雕国际象棋棋子，棋盘由燃烧的熔岩构成",
    "动作": "冰棋子在接触熔岩棋盘处轻微融化，产生蒸汽",
    "环境": "戏剧性黑色虚空背景",
    "构图": "3/4角度眼平面，微距摄影视角",
    "光线": "双光源：冰块散发冷蓝色荧光，熔岩散发橙红色光，接触点升起蒸汽",
    "风格": "超写实微距摄影",
    "文字渲染": {
      "是否包含文字": false
    },
    "技术参数": {
      "画面比例": "16:9",
      "输出分辨率": "4K",
      "镜头参数": "微距 f/4",
      "负向约束": "禁止物理上不可能的光线方向，禁止卡通化处理"
    },
    "参考图设置": []
  },
  "完整提示词（英文）": "A crystalline chess set where pieces are sculpted from freezing water and the board is made of burning lava. The ice pieces melt slightly where they touch the board. Reason through the complex lighting interactions between fire and ice before generating. 3/4 angle, eye-level macro photography. Dual-source lighting: cold blue bioluminescence from ice, orange-red glow from lava, steam rising at contact points. Hyper-realistic macro photography, f/4, 4K. No physically impossible lighting, no cartoon style.",
  "完整提示词（中文）": "水晶冰雕棋子与熔岩棋盘构成的国际象棋，棋子接触棋盘处轻微融化并升起蒸汽。生成前先推理火与冰的复杂光影交互。3/4角度眼平面微距摄影。双光源：冰块散发冷蓝色生物荧光，熔岩散发橙红色光，接触点蒸汽升腾。超写实微距摄影，f/4，4K。禁止物理上不可能的光线，禁止卡通化。",
  "编辑指令": "",
  "使用建议": [
    "必须启用推理思考模式，处理复杂物理光学交互",
    "若蒸汽效果不明显，追加提示：接触点的蒸汽应更加明显和立体",
    "图像80%满意时直接对话修改局部，不要重新生成整张图"
  ]
}
```

---

## 示例五：多语言文字渲染（餐厅菜单国际化）

```json
{
  "元信息": {
    "用途分类": "多语言文字",
    "生成模式": "普通生成",
    "语言设置": "多语言混排",
    "启用推理": false
  },
  "提示词要素": {
    "主体": "一张高档餐厅菜单卡",
    "动作": "平铺展示",
    "环境": "深色胡桃木桌面，烛光氛围",
    "构图": "正上方俯视平铺，居中构图",
    "光线": "右侧温暖烛光，柔和阴影",
    "风格": "奢华精品餐饮印刷设计",
    "文字渲染": {
      "是否包含文字": true,
      "文字内容": "Chef's Tasting Menu / 主厨品鉴菜单 / Menu Dégustation",
      "文字位置": "菜单卡顶部居中，作为三语标题",
      "字体风格": "优雅衬线字体，奶油色纸张上金色文字"
    },
    "技术参数": {
      "画面比例": "3:4",
      "输出分辨率": "2K",
      "镜头参数": "",
      "负向约束": "禁止文字拼写错误，禁止字符混乱"
    },
    "参考图设置": []
  },
  "完整提示词（英文）": "An elegant restaurant menu card on a dark walnut wooden table with candlelight ambiance. Top-down flat lay, centered. Warm candlelight from the right with soft shadows. Luxury fine dining premium print design. Display trilingual header: \"Chef's Tasting Menu\" / \"主厨品鉴菜单\" / \"Menu Dégustation\" in elegant serif font, gold lettering on cream paper. 3:4, 2K. No spelling errors, no character corruption.",
  "完整提示词（中文）": "深色胡桃木桌上的高档餐厅菜单卡，烛光氛围。正上方俯视平铺，居中构图。右侧温暖烛光打出柔和阴影。奢华精品餐饮印刷设计。三语居中标题：英文/中文/法文，优雅衬线字体，奶油色纸张上金色文字。3:4，2K画质。禁止文字拼写错误。",
  "编辑指令": "",
  "使用建议": [
    "三语混排是 Nano Banana Pro 的特色强项，中文和法文可同时精准渲染",
    "可上传品牌 Logo 作为参考图，角色设为「风格参考」，保持品牌一致性"
  ]
}
```
