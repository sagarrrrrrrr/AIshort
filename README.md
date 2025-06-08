# Video Renderer API with Flask & FFmpeg

## Overview

This project provides a simple REST API built with Flask that generates short videos by overlaying quotes on a background video with background music. It downloads the video and music from given URLs, adds the text overlay using FFmpeg, and returns the final video.

It’s designed for use in automation workflows (like n8n) to create faceless YouTube shorts or similar content.

---

## Features

- Accepts JSON input with:
  - **quote** — Text to overlay on the video
  - **video_url** — URL of the background video file (MP4)
  - **music_url** — URL of the background music file (MP3)
- Downloads and processes media files on the fly
- Uses FFmpeg to overlay text with styling (font, box, color)
- Returns the processed video file in MP4 format
- Auto cleans up temporary files after rendering

---

## Requirements

- Python 3.8+
- FFmpeg installed and accessible in your system PATH
- wget installed (or modify to use Python download method)
- Fonts installed (DejaVuSans or FreeSans recommended)

---

## Setup

1. Clone this repo

```bash
git clone <repo-url>
cd <repo-folder>
