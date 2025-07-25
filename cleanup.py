import os
import sys

DOWNLOAD_DIR = './downloaded_videos'
VERTICAL_DIR = './vertical_videos'
CLIPS_DIR = './clips'

def cleanup_files(slug: str):
    deleted = []

    # Helper to delete files with slug in filename from a folder
    def delete_from_dir(dir_path):
        for file in os.listdir(dir_path):
            if slug in file:
                file_path = os.path.join(dir_path, file)
                try:
                    os.remove(file_path)
                    deleted.append(file_path)
                except Exception as e:
                    print(f"⚠️ Failed to delete {file_path}: {e}")

    delete_from_dir(DOWNLOAD_DIR)
    delete_from_dir(VERTICAL_DIR)
    delete_from_dir(CLIPS_DIR)

    if deleted:
        print("🗑️ Deleted files:")
        for f in deleted:
            print(f" - {f}")
    else:
        print("❌ No matching files found to delete.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 cleanup.py <video-slug>")
        print("Example: python3 cleanup.py Deplo")
    else:
        slug = sys.argv[1]
        cleanup_files(slug)
