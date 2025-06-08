# app.py
from flask import Flask, request, jsonify
from movie_generator import generate_video
from youtube_uploader import upload_video
import os

app = Flask(__name__)

@app.route("/render", methods=["POST"])
def render():
    data = request.json
    quote = data.get("quote")
    video_url = data.get("video_url")
    music_url = data.get("music_url")

    if not all([quote, video_url, music_url]):
        return jsonify({"error": "Missing fields"}), 400

    try:
        output_path = generate_video(quote, video_url, music_url)
        return jsonify({"message": "Video created", "path": output_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    video_path = data.get("path")
    title = data.get("title", "Motivational Short")
    desc = data.get("description", "Automated YouTube upload")

    if not video_path or not os.path.exists(video_path):
        return jsonify({"error": "Invalid video path"}), 400

    try:
        youtube_url = upload_video(video_path, title, desc)
        return jsonify({"message": "Uploaded", "url": youtube_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
