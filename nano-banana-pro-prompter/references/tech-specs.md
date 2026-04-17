# Nano Banana Pro 技术规格参考

## 模型版本对照

| 特性 | Nano Banana Pro (Gemini 3 Pro Image) | Nano Banana 2 (Gemini 3.1 Flash Image) |
|------|------|------|
| 推理/Thinking | ✅ 完整推理 | ⚡ 快速推理 |
| 最大参考图数量 | 14张 | 4张 |
| 分辨率 | 1K / 2K / 4K | 0.5K / 1K / 2K |
| Search Grounding | ✅ | ✅ |
| 文字渲染质量 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 适合场景 | 专业级创作、复杂构图 | 快速迭代、批量生成 |

## 支持的宽高比

`1:1` `3:2` `2:3` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9`

（Nano Banana 2 额外支持 `2:1`）

## 支持的分辨率

- **0.5K (512px)**：仅 Nano Banana 2 Flash
- **1K**：两款模型均支持
- **2K**：两款模型均支持  
- **4K**：仅 Nano Banana Pro 支持

## 文字渲染支持的语言

30+ 语言，包括：中文（简/繁）、日文、韩文、阿拉伯文、法文、德文、西班牙文、葡萄牙文、俄文、印地文等

## 参考图输入 Role 类型

| Role | 用途 |
|------|------|
| `character` | 角色外貌一致性参考 |
| `style` | 艺术风格参考 |
| `environment` | 环境/场景参考 |
| `background` | 背景参考 |
| `product` | 产品外观参考 |

## API 接入

- **平台**：Google AI Studio、Vertex AI、Gemini App
- **模型 ID**：`gemini-3-pro-image`（Pro）、`gemini-3.1-flash-image-preview`（Flash）
- **文档**：https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro-image

## 常见相机镜头参数参考

| 效果 | 参数写法 |
|------|------|
| 浅景深人像 | f/1.8, 85mm portrait lens |
| 微距特写 | f/2.8 macro, extreme close-up |
| 广角环境 | f/11, 24mm wide angle |
| 电影感 | anamorphic lens, slight lens flare |
| 产品精细 | f/8, 100mm tilt-shift |
