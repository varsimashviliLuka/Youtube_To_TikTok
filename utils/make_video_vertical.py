import os
import subprocess

def make_video_vertical(input_path, slug, output_dir='./vertical_videos'):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"video_{slug}.mp4")

    ffmpeg_cmd = [
        'ffmpeg',
        '-y',
        '-i', input_path,
        '-vf', 'scale=-1:1280,crop=720:1280',
        '-c:v', 'h264_nvenc',
        '-preset', 'fast',
        '-c:a', 'aac',
        '-b:a', '128k',
        output_path
    ]

    subprocess.run(ffmpeg_cmd, check=True)
    return output_path
