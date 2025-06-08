from flask import Flask, request, send_file, jsonify, after_this_request
import os
import uuid
import subprocess

app = Flask(__name__)

# Ensure output folder exists
os.makedirs("renders", exist_ok=True)

@app.route("/render", methods=["POST"])
def render_video():
    data = request.json

    quote = data.get("quote")
    video_url = data.get("video_url")
    music_url = data.get("music_url")

    if not all([quote, video_url, music_url]):
        return jsonify({"error": "Missing required fields."}), 400

    uid = str(uuid.uuid4())
    video_path = f"renders/{uid}_video.mp4"
    music_path = f"renders/{uid}_music.mp3"
    text_path = f"renders/{uid}_text.txt"
    output_path = f"renders/{uid}_output.mp4"

    try:
        with open(text_path, "w") as f:
            f.write(quote)

        subprocess.run(["wget", "-O", video_path, video_url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        subprocess.run(["wget", "-O", music_path, music_url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if not os.path.exists(font_path):
            font_path = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"  # fallback

        command = [
            "ffmpeg",
            "-i", video_path,
            "-vf",
            f"drawtext=fontfile={font_path}:textfile={text_path}:fontcolor=white:fontsize=48:box=1:boxcolor=black@0.5:boxborderw=10:x=(w-text_w)/2:y=h-150",
            "-i", music_path,
            "-shortest",
            "-y",
            output_path
        ]

        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if not os.path.exists(output_path):
            return jsonify({"error": "Rendered file not found"}), 500

        @after_this_request
        def cleanup(response):
            for file in [video_path, music_path, text_path, output_path]:
                if os.path.exists(file):
                    os.remove(file)
            return response

        return send_file(output_path, mimetype="video/mp4")

    except subprocess.CalledProcessError as e:
        return jsonify({
            "error": "Subprocess failed.",
            "details": e.stderr
        }), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
