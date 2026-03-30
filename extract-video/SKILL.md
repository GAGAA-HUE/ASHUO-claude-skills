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

1. **检查依赖**：使用 Bash 检查 `ffmpeg` 和 `ffprobe` 是否已安装。
   - 若未安装，尝试通过系统包管理器安装（Windows 下提示用户手动安装，或尝试 `winget install ffmpeg`）。

2. **验证文件**：确认路径存在且为视频文件。

3. **根据操作类型执行**：

### info（默认）
运行：
```bash
ffprobe -v quiet -print_format json -show_streams -show_format "<视频路径>"
```
将 JSON 结果整理为易读的摘要（分辨率、时长、帧率、编码器、音频轨道数等）。

### frames
运行：
```bash
ffmpeg -i "<视频路径>" -vf "select='gt(scene,0.3)',showinfo" -vsync vfr -q:v 2 -f image2 "/tmp/extract-video-frames/frame_%04d.jpg"
```
或按时间间隔提取：
```bash
ffmpeg -i "<视频路径>" -vf "fps=1/5,scale=480:-1" -q:v 2 "/tmp/extract-video-frames/frame_%04d.jpg"
```
生成完成后，列出提取的帧文件路径，供后续分析使用。

### audio
运行：
```bash
ffmpeg -i "<视频路径>" -vn -acodec libmp3lame -q:a 2 "<输出路径.mp3>"
```
输出音频文件路径。

### subtitle
- 先尝试提取内嵌字幕流：
  ```bash
  ffmpeg -i "<视频路径>" -map 0:s:0 "<输出路径.srt>"
  ```
- 若无内嵌字幕，提取音频后使用 Whisper 进行转写（如果 Whisper 可用）。
- 将字幕/转写文本内容返回给用户。

## 输出要求

- 始终使用中文回复用户。
- 对于 `info` 操作，输出结构化的视频参数摘要。
- 对于 `frames/audio/subtitle` 操作，明确告知输出文件的路径，并总结内容。
- 如果过程中遇到依赖缺失，清晰告知用户需要安装什么，并提供安装命令。
