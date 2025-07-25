import os
import re
from yt_dlp import YoutubeDL

def slugify(text):
    return re.sub(r'\W+', '', text)[:5]  # first 5 alphanumeric chars

def download_youtube_video(url, output_dir='./downloaded_videos'):
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': '137+140/best',
        'quiet': False,
        'outtmpl': os.path.join(output_dir, '%(title).70s.%(ext)s'),
        'merge_output_format': 'mp4',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "video")
        ext = info.get("ext", "mp4")
        slug = slugify(title)
        downloaded_path = os.path.join(output_dir, f"{title}.{ext}")
        final_filename = f"video_{slug}.{ext}"
        final_path = os.path.join(output_dir, final_filename)

        if os.path.exists(downloaded_path):
            os.rename(downloaded_path, final_path)

        return final_path, slug
