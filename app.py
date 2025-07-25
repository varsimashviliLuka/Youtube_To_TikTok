from utils import download_youtube_video, make_video_vertical, split_video

def main():
    url = input("Enter YouTube video URL: ")
    
    print("⬇️ Downloading video...")
    downloaded_path, slug = download_youtube_video(url)

    print("📱 Making video vertical...")
    vertical_path = make_video_vertical(downloaded_path, slug)

    print("✂️ Splitting vertical video into parts...")
    split_clips = split_video(vertical_path, slug)

    print("\n✅ Done. Created clips:")
    for clip in split_clips:
        print(f" - {clip}")

if __name__ == "__main__":
    main()
