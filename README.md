Video Renderer API with Flask & FFmpeg
Overview
This project provides a simple REST API built with Flask that generates short videos by overlaying quotes on a background video with background music. It downloads the video and music from given URLs, adds the text overlay using FFmpeg, and returns the final video.

It’s designed for use in automation workflows (like n8n) to create faceless YouTube shorts or similar content.

Features
Accepts JSON input with:

quote — Text to overlay on the video

video_url — URL of the background video file (MP4)

music_url — URL of the background music file (MP3)

Downloads and processes media files on the fly

Uses FFmpeg to overlay text with styling (font, box, color)

Returns the processed video file in MP4 format

Auto cleans up temporary files after rendering

Requirements
Python 3.8+

FFmpeg installed and accessible in your system PATH

wget installed (or modify to use Python download method)

Fonts installed (DejaVuSans or FreeSans recommended)

Setup
Clone this repo

bash
Copy
Edit
git clone <repo-url>
cd <repo-folder>
Install dependencies

bash
Copy
Edit
pip install flask
Install system dependencies (Ubuntu example):

bash
Copy
Edit
sudo apt update
sudo apt install -y ffmpeg wget fonts-dejavu-core fonts-freefont-ttf
Running the Server
bash
Copy
Edit
python app.py
The server will run at http://127.0.0.1:5000.

API Usage
Endpoint: /render (POST)
Request Body JSON:

json
Copy
Edit
{
  "quote": "Your inspirational quote here",
  "video_url": "https://example.com/background-video.mp4",
  "music_url": "https://example.com/background-music.mp3"
}
Response:

On success: returns the generated MP4 video file.

On failure: returns JSON error message with status code.

Example Request
bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/render \
-H "Content-Type: application/json" \
-d '{
  "quote": "Believe in yourself.",
  "video_url": "https://player.vimeo.com/external/478125275.sd.mp4?s=ee52c5b8c43f7e8f9d191e4a4910020b8d3844fa&profile_id=165",
  "music_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
}'
Notes
Ensure video and audio URLs are direct file links accessible publicly.

For best results, use videos around 15-60 seconds for YouTube Shorts.

Customize the font path in the code if your system uses different fonts.

License
MIT License © Sagar Hirulkar
