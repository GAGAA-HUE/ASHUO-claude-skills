---
name: extract-video
slash_command: extract-video
description: |
  提取视频文件的基本信息、音频轨道、关键帧截图，或将其转换为可分析的格式。
  当用户提供视频路径并需要了解内容、提取字幕、获取关键帧时使用。
usage: |
  /extract-video <视频路径> [操作类型]

  操作类型（可选，默认为 info）：
  - info      显示视频基本信息（分辨率、时长、码率、编码格式等）
  - frames    提取关键帧截图到临时目录
  - audio     提取音频为 WAV/MP3
  - subtitle  尝试提取内嵌字幕或生成音频转文字（需要 Whisper）
---

# extract-video Skill

## 触发条件

用户输入 `/extract-video <路径>` 时，本 skill 生效。

## 执行流程

### Step 1: 自动检测 FFmpeg 路径

在 Windows 系统上，按以下优先级自动检测 FFmpeg：

1. **Winget 安装路径**（默认）：
   ```
   %LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_*
   ```

2. **Chocolatey 安装路径**：
   ```
   C:\ProgramData\chocolatey\bin\ffmpeg.exe
   ```

3. **官方安装程序路径**：
   ```
   C:\Program Files\FFmpeg\bin\ffmpeg.exe
   C:\ffmpeg\bin\ffmpeg.exe
   ```

4. **系统 PATH**：直接调用 `ffmpeg` / `ffprobe`

检测逻辑（Bash）：
```bash
# 尝试找到 ffmpeg
FFMPEG_PATH=""
PROBE_PATHS=(
  "$LOCALAPPDATA/Microsoft/WinGet/Packages/Gyan.FFmpeg_*/ffmpeg-*/bin/ffmpeg.exe"
  "/c/ProgramData/chocolatey/bin/ffmpeg.exe"
  "/c/Program Files/FFmpeg/bin/ffmpeg.exe"
  "/c/ffmpeg/bin/ffmpeg.exe"
)

for path in "${PROBE_PATHS[@]}"; do
  found=$(ls $path 2>/dev/null | head -1)
  if [ -n "$found" ]; then
    FFMPEG_PATH="$found"
    FFPROBE_PATH="${found/ffmpeg/ffprobe}"
    break
  fi
done

# 如果都没找到，尝试系统 PATH
if [ -z "$FFMPEG_PATH" ]; then
  if command -v ffmpeg &> /dev/null; then
    FFMPEG_PATH="ffmpeg"
    FFPROBE_PATH="ffprobe"
  fi
fi

if [ -z "$FFMPEG_PATH" ]; then
  echo "❌ FFmpeg 未找到。请安装："
  echo "   winget install Gyan.FFmpeg"
  echo "   或: choco install ffmpeg"
  exit 1
fi
```

### Step 2: 验证文件

确认路径存在且为视频文件：
```bash
if [ ! -f "$VIDEO_PATH" ]; then
  echo "❌ 文件不存在: $VIDEO_PATH"
  exit 1
fi
```

### Step 3: 根据操作类型执行

#### info（默认）
运行：
```bash
"$FFPROBE_PATH" -v quiet -print_format json -show_streams -show_format "$VIDEO_PATH"
```
将 JSON 结果整理为易读的摘要（分辨率、时长、帧率、编码器、音频轨道数等）。

#### frames
运行：
```bash
# 创建输出目录
OUTPUT_DIR="${TEMP:-/tmp}/extract-video-frames-$(date +%s)"
mkdir -p "$OUTPUT_DIR"

# 按时间间隔提取（每2秒一帧，480px宽度）
"$FFMPEG_PATH" -i "$VIDEO_PATH" -vf "fps=1/2,scale=480:-1" -q:v 2 "$OUTPUT_DIR/frame_%04d.jpg"

# 或按场景变化提取（需要更多计算）
# "$FFMPEG_PATH" -i "$VIDEO_PATH" -vf "select='gt(scene,0.3)',showinfo" -vsync vfr -q:v 2 -f image2 "$OUTPUT_DIR/scene_%04d.jpg"
```

生成完成后，列出提取的帧文件路径，供后续分析使用。

#### audio
运行：
```bash
OUTPUT_AUDIO="${VIDEO_PATH%.*}.mp3"
"$FFMPEG_PATH" -i "$VIDEO_PATH" -vn -acodec libmp3lame -q:a 2 "$OUTPUT_AUDIO"
```
输出音频文件路径。

#### subtitle
- 先尝试提取内嵌字幕流：
  ```bash
  "$FFMPEG_PATH" -i "$VIDEO_PATH" -map 0:s:0 "${VIDEO_PATH%.*}.srt" 2>/dev/null
  ```
- 若无内嵌字幕，提取音频后使用 Whisper 进行转写（如果 Whisper 可用）。
- 将字幕/转写文本内容返回给用户。

---

## 完整执行脚本模板

```bash
#!/bin/bash
VIDEO_PATH="$1"
ACTION="${2:-info}"

# 自动检测 FFmpeg
find_ffmpeg() {
  local paths=(
    "$LOCALAPPDATA/Microsoft/WinGet/Packages/Gyan.FFmpeg_*/ffmpeg-*/bin/ffmpeg.exe"
    "/c/ProgramData/chocolatey/bin/ffmpeg.exe"
    "/c/Program Files/FFmpeg/bin/ffmpeg.exe"
    "/c/ffmpeg/bin/ffmpeg.exe"
  )

  for pattern in "${paths[@]}"; do
    local found=$(ls $pattern 2>/dev/null | head -1)
    if [ -n "$found" ] && [ -f "$found" ]; then
      echo "$found"
      return 0
    fi
  done

  # 尝试 PATH
  if command -v ffmpeg &> /dev/null; then
    echo "ffmpeg"
    return 0
  fi

  return 1
}

FFMPEG=$(find_ffmpeg)
if [ -z "$FFMPEG" ]; then
  echo "❌ FFmpeg 未找到"
  echo "请安装: winget install Gyan.FFmpeg"
  exit 1
fi

FFPROBE="${FFMPEG/ffmpeg/ffprobe}"

# 验证文件
if [ ! -f "$VIDEO_PATH" ]; then
  echo "❌ 文件不存在: $VIDEO_PATH"
  exit 1
fi

# 执行操作
case "$ACTION" in
  info)
    "$FFPROBE" -v quiet -print_format json -show_streams -show_format "$VIDEO_PATH" | \
    python3 -c "
import sys, json
d = json.load(sys.stdin)
fmt = d.get('format', {})
streams = d.get('streams', [])
video = next((s for s in streams if s.get('codec_type') == 'video'), {})
audio = next((s for s in streams if s.get('codec_type') == 'audio'), {})

print('📹 视频信息')
print('=' * 40)
print(f'时长: {float(fmt.get(\"duration\", 0)):.2f} 秒')
print(f'大小: {int(fmt.get(\"size\", 0)) / 1024 / 1024:.2f} MB')
print(f'码率: {int(fmt.get(\"bit_rate\", 0)) / 1000:.0f} kbps')
print(f'格式: {fmt.get(\"format_name\", \"unknown\")}')
if video:
  print(f'分辨率: {video.get(\"width\", \"?\")}x{video.get(\"height\", \"?\")}')
  print(f'帧率: {eval(video.get(\"r_frame_rate\", \"0/1\")):.2f} fps')
  print(f'编码: {video.get(\"codec_name\", \"unknown\")}')
if audio:
  print(f'音频: {audio.get(\"codec_name\", \"unknown\")}, {audio.get(\"sample_rate\", \"?\")} Hz')
"
    ;;

  frames)
    OUTPUT_DIR="${TEMP:-/tmp}/extract-video-frames-$(date +%s)"
    mkdir -p "$OUTPUT_DIR"
    echo "🎬 正在提取关键帧..."
    "$FFMPEG" -i "$VIDEO_PATH" -vf "fps=1/2,scale=480:-1" -q:v 2 "$OUTPUT_DIR/frame_%04d.jpg" 2>/dev/null
    echo "✅ 已提取到: $OUTPUT_DIR"
    ls -la "$OUTPUT_DIR"
    ;;

  audio)
    OUTPUT="${VIDEO_PATH%.*}.mp3"
    echo "🎵 正在提取音频..."
    "$FFMPEG" -i "$VIDEO_PATH" -vn -acodec libmp3lame -q:a 2 "$OUTPUT" 2>/dev/null
    echo "✅ 已保存: $OUTPUT"
    ;;

  subtitle)
    OUTPUT="${VIDEO_PATH%.*}.srt"
    if "$FFMPEG" -i "$VIDEO_PATH" -map 0:s:0 "$OUTPUT" 2>/dev/null; then
      echo "✅ 字幕已提取: $OUTPUT"
    else
      echo "⚠️ 未找到内嵌字幕，尝试音频转写需要 Whisper"
    fi
    ;;

  *)
    echo "未知操作: $ACTION"
    echo "可用: info, frames, audio, subtitle"
    exit 1
    ;;
esac
```

---

## 输出要求

- 始终使用中文回复用户。
- 对于 `info` 操作，输出结构化的视频参数摘要。
- 对于 `frames/audio/subtitle` 操作，明确告知输出文件的路径，并总结内容。
- 如果过程中遇到依赖缺失，清晰告知用户需要安装什么，并提供安装命令。
