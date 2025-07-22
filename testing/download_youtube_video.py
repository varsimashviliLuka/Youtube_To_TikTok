import os
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip
import math

# ========== STEP 1: Download YouTube Video ==========
def download_youtube_video(url, output_path='video.mp4'):
    ydl_opts = {
        'format': 'bestvideo[height<=1080][fps<=30][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
        'quiet': False,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path

# ========== STEP 2: Convert to Vertical ==========
def convert_to_vertical(input_path, output_path='vertical_video.mp4', height=1280):
    clip = VideoFileClip(input_path)
    aspect_ratio = 9 / 16
    width = int(height * aspect_ratio)

    resized = clip.resize(height=height)
    x_center = resized.w / 2
    x1 = x_center - width / 2
    x2 = x_center + width / 2

    vertical_clip = resized.crop(x1=x1, x2=x2)
    vertical_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    return output_path

def process_youtube_video_for_tiktok(youtube_url):
    print("📥 Downloading video...")
    downloaded = download_youtube_video(youtube_url)

    print("📱 Converting to vertical format...")
    vertical = convert_to_vertical(downloaded)

    # print(f"✅ Done. Created {len(clips)} TikTok-ready clips in './clips'")
    return 'done!'


if __name__ == "__main__":
    url = input("Paste YouTube video URL: ").strip()
    process_youtube_video_for_tiktok(url)