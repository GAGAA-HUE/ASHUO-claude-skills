#!/bin/bash
# extract.sh — 视频提取工具
# 用法：bash extract.sh <视频路径> <输出目录>

VIDEO_PATH="$1"
WORK_DIR="${2:-$(mktemp -d)}"
mkdir -p "$WORK_DIR/frames"

echo "📹 开始处理视频：$VIDEO_PATH"
echo "📂 工作目录：$WORK_DIR"

# 检查 ffmpeg
if ! command -v ffmpeg &>/dev/null; then
  echo "❌ 未找到 ffmpeg。请安装：brew install ffmpeg 或 sudo apt install ffmpeg"
  exit 1
fi

# 元数据
echo "🔍 提取元数据..."
ffprobe -v quiet -print_format json -show_format -show_streams "$VIDEO_PATH" > "$WORK_DIR/meta.json"
DURATION=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO_PATH")
echo "   时长：${DURATION}秒"

# 关键帧截取
echo "🖼  截取关键帧..."
ffmpeg -i "$VIDEO_PATH" \
  -ss 0   -frames:v 1 "$WORK_DIR/frames/t000.jpg" \
  -ss 5   -frames:v 1 "$WORK_DIR/frames/t005.jpg" \
  -ss 15  -frames:v 1 "$WORK_DIR/frames/t015.jpg" \
  -ss 30  -frames:v 1 "$WORK_DIR/frames/t030.jpg" \
  -y 2>/dev/null
ffmpeg -i "$VIDEO_PATH" -vf "fps=1/60" "$WORK_DIR/frames/seg_%04d.jpg" -y 2>/dev/null
echo "   帧已保存至 $WORK_DIR/frames/"

# 音频提取与转录
echo "🎙  提取音频..."
ffmpeg -i "$VIDEO_PATH" -vn -acodec pcm_s16le -ar 16000 -ac 1 "$WORK_DIR/audio.wav" -y 2>/dev/null

if command -v whisper &>/dev/null; then
  echo "📝 转录音频（whisper）..."
  whisper "$WORK_DIR/audio.wav" --language zh --output_dir "$WORK_DIR" --output_format txt
  echo "   转录完成：$WORK_DIR/audio.txt"
else
  echo "⚠️  whisper 未安装，跳过转录。"
  echo "   安装方式：pip install openai-whisper"
  echo "   [视觉分析基于有限信息]" > "$WORK_DIR/audio.txt"
fi

echo ""
echo "✅ 提取完成"
echo "   元数据：$WORK_DIR/meta.json"
echo "   关键帧：$WORK_DIR/frames/"
echo "   转录：  $WORK_DIR/audio.txt"
echo "WORK_DIR=$WORK_DIR"
