import os
import subprocess
import math

def get_video_duration(video_path):
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries',
         'format=duration', '-of',
         'default=noprint_wrappers=1:nokey=1', video_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    return float(result.stdout)

def split_video(input_path, slug, output_dir='./clips', part_length=120, overlap=5):
    os.makedirs(output_dir, exist_ok=True)
    duration = get_video_duration(input_path)
    part_index = 1
    start = 0
    clips = []

    while start < duration:
        effective_start = max(0, start - overlap if start > 0 else 0)
        output_file = os.path.join(output_dir, f"video_{slug}_part{part_index}.mp4")

        ffmpeg_cmd = [
            'ffmpeg',
            '-y',
            '-ss', str(effective_start),
            '-i', input_path,
            '-t', str(part_length),
            '-c:v', 'h264_nvenc',
            '-preset', 'fast',
            '-c:a', 'aac',
            '-b:a', '128k',
            output_file
        ]

        subprocess.run(ffmpeg_cmd, check=True)
        clips.append(output_file)

        start += part_length
        part_index += 1

        if start >= duration:
            break

    return clips
