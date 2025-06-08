# movie_generator.py
import requests
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
import uuid
import os


def generate_video(quote, video_url, music_url):
    uid = str(uuid.uuid4())
    os.makedirs("renders", exist_ok=True)
    video_path = f"renders/{uid}_video.mp4"
    music_path = f"renders/{uid}_music.mp3"
    output_path = f"renders/{uid}_final.mp4"

    # Download video
    with requests.get(video_url, stream=True) as r:
        r.raise_for_status()
        with open(video_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Download music
    with requests.get(music_url, stream=True) as r:
        r.raise_for_status()
        with open(music_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Load video and audio
    clip = VideoFileClip(video_path).subclip(0, 15)
    audioclip = AudioFileClip(music_path).subclip(0, clip.duration)
    clip = clip.set_audio(audioclip)

    # Add text
    txt_clip = TextClip(quote, fontsize=40, color='white', font='DejaVu-Sans-Bold', method='caption', size=(clip.w * 0.8, None)).set_position('center').set_duration(clip.duration)

    final = CompositeVideoClip([clip, txt_clip])
    final.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac', threads=2, preset='ultrafast')

    # Clean up source files
    os.remove(video_path)
    os.remove(music_path)

    return output_path
