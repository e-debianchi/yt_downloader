from pytubefix import YouTube
import os

def download_youtube_content():
    url = input("Enter the YouTube video URL: ").strip()
    try:
        yt = YouTube(url)
    except Exception as e:
        print(f"Error: {e}")
        return

    print(f"\nTitle: {yt.title}")
    print(f"Views: {yt.views}")
    print(f"Length: {yt.length} seconds\n")

    choice = input("Download (v)ideo or (a)udio only? [v/a]: ").strip().lower()
    if choice == 'v':
        stream = yt.streams.get_highest_resolution()
    elif choice == 'a':
        stream = yt.streams.get_audio_only()
    else:
        print("Invalid choice. Please enter 'v' for video or 'a' for audio.")
        return

    output_path = input('Enter the output path (default is current directory): ').strip()
    if not output_path:
        output_path = os.getcwd()
    os.makedirs(output_path, exist_ok=True)

    print(f"\nDownloading to: {output_path}")
    try:
        stream.download(output_path=output_path)
        print("Download completed successfully.")
    except Exception as e:
        print(f"Download failed: {e}")

if __name__ == "__main__":
    download_youtube_content()
