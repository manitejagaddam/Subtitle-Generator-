# Subtile Generator

Subtile Generator is a Python-based tool that automatically extracts audio from videos and generates accurate subtitles using OpenAI’s Whisper model.  
It provides an easy way to create `.srt` subtitle files for your videos with minimal setup.

---

## 🧠 Introduction

Creating subtitles manually can be time-consuming.  
**Subtile Generator** simplifies this process by leveraging **FFmpeg** for audio extraction and **Whisper**, OpenAI’s speech recognition model, for automatic subtitle generation.

The tool processes any video file, extracts its audio track, transcribes the speech, and outputs a synchronized `.srt` subtitle file.

---

## 📑 Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Example](#example)
6. [Output](#output)
7. [Troubleshooting](#troubleshooting)
8. [Contributors](#contributors)
9. [License](#license)

---

## 🚀 Features

- Extracts audio directly from video files using **FFmpeg**
- Transcribes speech to text using **Whisper**
- Outputs standard `.srt` subtitle files
- Supports multiple video formats (e.g., `.mp4`, `.mkv`, `.mov`)
- Lightweight and simple to use

---

## ⚙️ Installation

### Prerequisites

Make sure you have:
- **Python 3.8+**
- **FFmpeg** installed on your system
- Access to the **Whisper** model (via OpenAI or the `openai-whisper` library)

### Install Dependencies

```bash
pip install ffmpeg-python openai-whisper
```

If you don’t have FFmpeg installed:
- On macOS: `brew install ffmpeg`
- On Ubuntu/Debian: `sudo apt install ffmpeg`
- On Windows: [Download FFmpeg](https://ffmpeg.org/download.html)

---

## 💻 Usage

### Step 1 — Extract Audio and Generate Subtitles

Run the script:

```bash
python subtile_generator.py --input path/to/video.mp4 --output subtitles.srt
```

### Example Command Breakdown

| Argument | Description |
|-----------|--------------|
| `--input` | Path to the input video file |
| `--output` | Path where the `.srt` file will be saved |

---

## 🔧 Configuration

Optional parameters you can include:

| Option | Description | Default |
|---------|--------------|----------|
| `--model` | Whisper model to use (`tiny`, `base`, `small`, `medium`, `large`) | `base` |
| `--language` | Language code (e.g., `en`, `es`, `fr`) | Auto-detect |
| `--verbose` | Display detailed processing logs | `False` |

---

## 🧩 Example

```bash
python subtile_generator.py --input sample_video.mp4 --output sample_subtitles.srt --model small
```

**Output:**
```
Extracting audio from sample_video.mp4...
Running Whisper transcription...
Subtitles generated successfully: sample_subtitles.srt
```

---

## 🗂️ Output

Generated subtitle file format: **SubRip (.srt)**

Example excerpt:

```
1
00:00:00,000 --> 00:00:03,500
Welcome to the Subtile Generator demo.

2
00:00:03,600 --> 00:00:07,200
This tool automatically creates subtitles using Whisper.
```

---

## 🧰 Troubleshooting

| Issue | Possible Cause | Solution |
|--------|----------------|-----------|
| `ffmpeg: command not found` | FFmpeg not installed or not in PATH | Install FFmpeg and restart terminal |
| Whisper takes too long | Large model selected | Use smaller model (e.g., `base` or `small`) |
| Output file empty | Unsupported video/audio codec | Re-encode using `ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mp4` |

---

## 👥 Contributors

- **Maniteja Gaddam** — Creator and maintainer of Subtile Generator

Contributions are welcome! Feel free to open a pull request or submit issues.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🧩 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [FFmpeg](https://ffmpeg.org)
- Python community for their amazing libraries

---

> ⚡ *“Turn any video into text — easily, accurately, automatically.”*
