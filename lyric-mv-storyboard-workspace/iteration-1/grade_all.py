#!/usr/bin/env python3
"""Grade all lyric-mv-storyboard eval runs programmatically."""

import json
import os

EVAL_DIR = "C:/Users/vip/.claude/skills/lyric-mv-storyboard-workspace/iteration-1"

def grade_file(result_path, is_haidi=False):
    """Grade a single result.md file against assertions."""
    if not os.path.exists(result_path):
        return None, f"File not found: {result_path}"

    with open(result_path, "r", encoding="utf-8") as f:
        text = f.read()

    text_lower = text.lower()

    expectations = []

    # 1. has_lyric_analysis
    analysis_keywords = ["故事内核", "情绪弧线", "角色设定", "核心意象", "场景设定",
                         "story kernel", "emotional arc", "character", "imagery", "scene"]
    matched = sum(1 for k in analysis_keywords if k in text_lower)
    has_analysis = matched >= 3
    expectations.append({
        "text": "输出包含歌词深度分析部分（故事内核、情绪弧线、角色设定、意象符号、场景设定中的至少3项）",
        "passed": has_analysis,
        "evidence": f"找到 {matched}/10 个分析关键词" if has_analysis else f"仅找到 {matched} 个分析关键词"
    })

    # 2. has_storyboard
    storyboard_keywords = ["分镜", "镜头", "shot", "storyboard"]
    has_storyboard = any(k in text_lower for k in storyboard_keywords)
    expectations.append({
        "text": "输出包含MV分镜脚本部分",
        "passed": has_storyboard,
        "evidence": "找到分镜相关关键词" if has_storyboard else "未找到分镜相关关键词"
    })

    # 3. shot_elements_complete
    shot_elements = ["景别", "运镜", "时长", "画面"]
    shot_en = ["shot size", "camera", "duration", "frame"]
    matched_elements = sum(1 for k in shot_elements if k in text_lower)
    matched_en = sum(1 for k in shot_en if k in text_lower)
    has_elements = matched_elements >= 3 or matched_en >= 3
    expectations.append({
        "text": "分镜包含景别、运镜、时长、画面描述四项基本要素",
        "passed": has_elements,
        "evidence": f"中文要素: {matched_elements}/4, 英文要素: {matched_en}/4" if has_elements else f"要素不足: 中文{matched_elements}, 英文{matched_en}"
    })

    # 4. segmented_by_lyric_parts
    segment_keywords = ["verse", "chorus", "bridge", "intro", "outro", "主歌", "副歌", "间奏", "序幕", "尾奏"]
    matched_segments = sum(1 for k in segment_keywords if k in text_lower)
    has_segments = matched_segments >= 2
    expectations.append({
        "text": "分镜按歌词段落（如Verse/Chorus/Bridge）组织",
        "passed": has_segments,
        "evidence": f"找到 {matched_segments} 个段落标记关键词" if has_segments else f"仅找到 {matched_segments} 个段落标记"
    })

    # 5. has_visual_style
    style_keywords = ["色彩", "摄影", "剪辑", "色调", "color", "cinematography", "editing"]
    matched_style = sum(1 for k in style_keywords if k in text_lower)
    has_style = matched_style >= 2
    expectations.append({
        "text": "包含整体视觉风格建议（色彩、摄影、剪辑等）",
        "passed": has_style,
        "evidence": f"找到 {matched_style} 个视觉风格关键词" if has_style else f"仅找到 {matched_style} 个视觉风格关键词"
    })

    # 6. has_character_setting
    char_keywords = ["角色", "主角", "人物", "character", "protagonist"]
    has_char = any(k in text_lower for k in char_keywords)
    expectations.append({
        "text": "明确提及角色设定",
        "passed": has_char,
        "evidence": "找到角色相关关键词" if has_char else "未找到角色相关关键词"
    })

    # 7. has_scene_setting
    scene_keywords = ["场景", "设定", "scene", "setting", "地点"]
    has_scene = any(k in text_lower for k in scene_keywords)
    expectations.append({
        "text": "明确提及场景设定",
        "passed": has_scene,
        "evidence": "找到场景相关关键词" if has_scene else "未找到场景相关关键词"
    })

    # 8. ocean_imagery_visualized (only for eval-3)
    if is_haidi:
        ocean_keywords = ["海", "浪", "月光", "沙滩", "水", "海底", "潮汐", "sea", "ocean", "wave", "moon", "beach", "underwater"]
        matched_ocean = sum(1 for k in ocean_keywords if k in text_lower)
        has_ocean = matched_ocean >= 3
        expectations.append({
            "text": "海洋意象（月光、海浪、海底、沙滩等）在分镜中有具体视觉呈现",
            "passed": has_ocean,
            "evidence": f"找到 {matched_ocean} 个海洋意象关键词" if has_ocean else f"仅找到 {matched_ocean} 个海洋意象关键词"
        })

    passed = sum(1 for e in expectations if e["passed"])
    total = len(expectations)

    grading = {
        "expectations": expectations,
        "summary": {
            "passed": passed,
            "failed": total - passed,
            "total": total,
            "pass_rate": round(passed / total, 2) if total > 0 else 0
        }
    }

    return grading, None


def main():
    evals = [
        ("eval-1-xiaochou", "with_skill", False),
        ("eval-1-xiaochou", "without_skill", False),
        ("eval-2-someone-like-you", "with_skill", False),
        ("eval-2-someone-like-you", "without_skill", False),
        ("eval-3-haidi", "with_skill", True),
        ("eval-3-haidi", "without_skill", True),
    ]

    for eval_name, config, is_haidi in evals:
        result_path = os.path.join(EVAL_DIR, eval_name, config, "outputs", "result.md")
        grading, error = grade_file(result_path, is_haidi)

        if error:
            print(f"[{eval_name}/{config}] ERROR: {error}")
            continue

        out_path = os.path.join(EVAL_DIR, eval_name, config, "outputs", "grading.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(grading, f, ensure_ascii=False, indent=2)

        print(f"[{eval_name}/{config}] {grading['summary']['passed']}/{grading['summary']['total']} passed ({grading['summary']['pass_rate']:.0%})")


if __name__ == "__main__":
    main()
