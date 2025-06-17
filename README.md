# YouTube Downloader

`yt_downloader` is a simple utility for downloading videos and/or audio from YouTube. It provides a command-line interface to fetch and save content locally for offline use.
It is based on the [`pytubefix`](https://pypi.org/project/pytubefix/) library.

## 📦 Features

- Download full YouTube videos in the highest available resolution.
- Extract audio from YouTube videos.
- Simple and easy-to-use CLI.
- Specify the output directory for downloads.
- Cross-platform support.

## 🛠 Requirements

- Python 3.7+
- [pytubefix](https://pypi.org/project/pytubefix/)

## Installation

Clone the repository:

```bash
git clone https://github.com/5e77e/yt_downloader.git
cd yt_downloader
```

Install dependencies:

```bash
pip install pytubefix
```

## 🚀 Usage

```bash
python yt_downloader.py
```

You will be prompted to:
1. Enter the YouTube video URL.
2. Choose whether to download the video or audio only (v for video, a for audio).
3. Specify the output directory (press Enter to use the current working directory).

**📁 Example:**

Enter the YouTube video URL: https://www.youtube.com/watch?v=abcd1234
Title: Sample Video Title
Views: 1234567
Length: 210 seconds

Download (v)ideo or (a)udio only? [v/a]: a
Enter the output path (default is current directory): /Users/yourname/Downloads

Downloading to: /Users/yourname/Downloads
Download completed successfully.

## ⚠️ Notes

- Make sure the provided URL is valid and accessible.
- Some videos may be unavailable due to regional restrictions or copyright issues.
- This tool is intended for educational and personal use only. Please respect YouTube's terms of service.