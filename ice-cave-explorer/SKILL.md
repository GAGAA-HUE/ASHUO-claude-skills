---
name: ice-cave-explorer
description: 冰洞探险视频剧本 skill —— 为 AI 视频生成工作流产出剧本层资产（亮点设计、场景设定、分镜脚本）。每个产出物对应 120 秒横屏冰洞探险短片的一个环节。不产 AI 工具提示词、不产操作手册。触发词：冰洞、探险视频、冰洞剧本、ice cave。
---

# 冰洞探险视频剧本 Skill

## 这是什么

为 AI 视频生成工作流提供**剧本层资产**的工作 skill。每一集产出一份可执行的 120 秒横屏短片剧本，覆盖亮点设计、场景设定、分镜脚本三个环节。

## 不产出什么

- 不产 Seedance 2.5 / 图生视频 / Suno 的具体提示词
- 不产剪辑软件操作手册
- 不产最终成片

下游 AI 工具调用和剪辑执行，由你或别的 skill 完成。

## 怎么用

按以下 3 步顺序执行，**每步完成后等待你过目**。前一步未通过不进入下一步。

1. **亮点设计**（读 `workflow/step-1-hook.md` + `rules/topic-transformation.md` + `config/l1-prototypes.md`）
2. **场景设定**（读 `workflow/step-2-worldbuilding.md` + `config/l1-prototypes.md`）
3. **分镜脚本**（读 `workflow/step-3-storyboard.md` + `config/explorer-profile.md` + `rules/timing-template.md` + `rules/narration-voice.md` + `rules/arsm-tags.md`）

完成第 1 集后，把完整剧本回填到 `examples/episode-01.md` 作为后续集数的模板标杆。

## 文件导航

- 决策摘要：`config/decisions.md`
- 探险者人设档：`config/explorer-profile.md`
- 冰洞原型库：`config/l1-prototypes.md`
- 节奏模板：`rules/timing-template.md`
- 母题派生规则：`rules/l2-derivation.md`
- 衍生选题三步法：`rules/topic-transformation.md`
- 旁白语感指南：`rules/narration-voice.md`
- 音效标签表：`rules/arsm-tags.md`
- 质量检查表：`workflow/quality-checklist.md`

## 质量门

完成每步后，跑 `workflow/quality-checklist.md` 自检，未过项必须修订后才能进入下一步。
