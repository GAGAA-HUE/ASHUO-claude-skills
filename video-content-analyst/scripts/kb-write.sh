#!/bin/bash
# kb-write.sh v3 — 写入知识库条目并维护三维索引
# 用法：bash kb-write.sh \
#         --title "xxx" \
#         --tags "#时事评论 #拟人化" \
#         --hook-type "金句前置" \
#         --structure "矛盾建立→冲突激化→收口" \
#         --visual "AI高拟真" \
#         --tone "古白话+口语混搭" \
#         --hook-score 5 \
#         --density-score 3 \
#         --virality-score 5 \
#         --hypothesis "xxx" \
#         --content-file /path/to/content.md

set -e

KB_DIR="$HOME/.claude/kb/video-methodology"
ENTRIES_DIR="$KB_DIR/entries"
INDEX_FILE="$KB_DIR/index.json"
HYP_FILE="$KB_DIR/hypotheses.json"

mkdir -p "$ENTRIES_DIR" "$KB_DIR/notes"

# --- 参数解析 ---
TITLE="" TAGS="" HOOK_TYPE="" STRUCTURE="" VISUAL="" TONE=""
HOOK_SCORE=3 DENSITY_SCORE=3 VIRALITY_SCORE=3
HYPOTHESIS="" CONTENT_FILE="" SOURCE_PLATFORM="" DURATION=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --title)           TITLE="$2";           shift 2 ;;
    --tags)            TAGS="$2";            shift 2 ;;
    --hook-type)       HOOK_TYPE="$2";       shift 2 ;;
    --structure)       STRUCTURE="$2";       shift 2 ;;
    --visual)          VISUAL="$2";          shift 2 ;;
    --tone)            TONE="$2";            shift 2 ;;
    --hook-score)      HOOK_SCORE="$2";      shift 2 ;;
    --density-score)   DENSITY_SCORE="$2";   shift 2 ;;
    --virality-score)  VIRALITY_SCORE="$2";  shift 2 ;;
    --hypothesis)      HYPOTHESIS="$2";      shift 2 ;;
    --content-file)    CONTENT_FILE="$2";    shift 2 ;;
    --source)          SOURCE_PLATFORM="$2"; shift 2 ;;
    --duration)        DURATION="$2";        shift 2 ;;
    *) echo "未知参数: $1"; exit 1 ;;
  esac
done

if [[ -z "$TITLE" ]]; then
  echo "❌ 必须提供 --title 参数"
  exit 1
fi

# --- 生成条目ID和文件名 ---
DATE=$(date '+%Y-%m-%d')
TIMESTAMP=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
SLUG=$(python3 -c "
import re, sys
s = sys.argv[1].lower()
s = re.sub(r'[^\w\s-]', '', s)
s = re.sub(r'[\s_]+', '-', s).strip('-')
print(s[:40])
" "$TITLE")
ENTRY_ID="${DATE}_${SLUG}"
ENTRY_FILE="$ENTRIES_DIR/${ENTRY_ID}.md"

# --- 写入条目文件 ---
cat > "$ENTRY_FILE" <<ENTRY
---
id: $ENTRY_ID
title: $TITLE
date: $DATE
source_platform: $SOURCE_PLATFORM
tags: $TAGS
hook_type: $HOOK_TYPE
structure_model: $STRUCTURE
visual_style: $VISUAL
language_tone: $TONE
hook_strength: $HOOK_SCORE
information_density: $DENSITY_SCORE
virality_potential: $VIRALITY_SCORE
---

$([ -n "$CONTENT_FILE" ] && cat "$CONTENT_FILE" || echo "（内容待补充）")

ENTRY

echo "✅ 条目文件已写入：$ENTRY_FILE"

# --- 更新 index.json ---
python3 - <<PYEOF
import json, os
from datetime import datetime

index_file = "$INDEX_FILE"
entry_id = "$ENTRY_ID"
entry_file = "$ENTRY_FILE"

# 初始化或读取
if os.path.exists(index_file):
    with open(index_file) as f:
        data = json.load(f)
else:
    data = {"entries": [], "tag_index": {}, "methodology_index": {
        "hook_type": {}, "structure_model": {}, "visual_style": {}
    }}

# 构建新条目
new_entry = {
    "id": entry_id,
    "file": f"entries/{os.path.basename(entry_file)}",
    "meta": {
        "title": "$TITLE",
        "date": "$DATE",
        "source_platform": "$SOURCE_PLATFORM",
        "duration_seconds": $DURATION
    },
    "tags": [t.strip() for t in "$TAGS".split() if t.strip()],
    "methodology": {
        "hook_type": "$HOOK_TYPE",
        "structure_model": "$STRUCTURE",
        "visual_style": "$VISUAL",
        "language_tone": "$TONE"
    },
    "effectiveness": {
        "hook_strength": $HOOK_SCORE,
        "information_density": $DENSITY_SCORE,
        "virality_potential": $VIRALITY_SCORE,
        "notes": ""
    },
    "reuse_count": 0,
    "hypotheses": ["$HYPOTHESIS"] if "$HYPOTHESIS" else [],
    "created_at": "$TIMESTAMP",
    "last_cited": None
}

# 防重复
data["entries"] = [e for e in data["entries"] if e["id"] != entry_id]
data["entries"].append(new_entry)

# 更新 tag_index
for tag in new_entry["tags"]:
    data["tag_index"].setdefault(tag, [])
    if entry_id not in data["tag_index"][tag]:
        data["tag_index"][tag].append(entry_id)

# 更新 methodology_index
mi = data.setdefault("methodology_index", {})
for dim, val in [("hook_type", "$HOOK_TYPE"), ("structure_model", "$STRUCTURE"), ("visual_style", "$VISUAL")]:
    mi.setdefault(dim, {})
    mi[dim].setdefault(val, [])
    if entry_id not in mi[dim][val]:
        mi[dim][val].append(entry_id)

with open(index_file, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ index.json 已更新，当前共 {len(data['entries'])} 条条目")
PYEOF

# --- 写入待验证假设 ---
if [[ -n "$HYPOTHESIS" ]]; then
  python3 - <<PYEOF2
import json, os
hyp_file = "$HYP_FILE"
data = json.load(open(hyp_file)) if os.path.exists(hyp_file) else {"hypotheses": []}
data["hypotheses"].append({
    "id": "${ENTRY_ID}_h1",
    "text": "$HYPOTHESIS",
    "status": "pending",
    "source_entry": "$ENTRY_ID",
    "created_at": "$TIMESTAMP",
    "verified_at": None,
    "conclusion": None
})
with open(hyp_file, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✅ 假设已记录到 hypotheses.json")
PYEOF2
fi

echo ""
echo "📚 知识库状态："
echo "   条目：$ENTRIES_DIR"
echo "   索引：$INDEX_FILE"
[[ -n "$HYPOTHESIS" ]] && echo "   假设：$HYP_FILE"
