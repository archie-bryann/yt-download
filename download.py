import yt_dlp
import os

# Make sure ffmpeg path is correctly set for merging video and audio
FFMPEG_PATH = os.path.join("C:", os.sep, "ffmpeg", "bin", "ffmpeg.exe")

# yt-dlp configuration options
ydl_opts = {
    # 'format': 'bestvideo+bestaudio/best',                     # Best available (up to 8K)
    # 'format': 'bestvideo[height<=4320]+bestaudio/best',       # 8K
    # 'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',  # 4K
    # 'format': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',  # 2K (1440p)
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',    # 1080p
    # 'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',    # 720p
    # 'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',    # 480p
    # 'format': 'bestvideo[height<=360]+bestaudio/best[height<=360]',    # 360p
    'merge_output_format': 'mp4',                # Output format after merging
    'ffmpeg_location': FFMPEG_PATH,              # Path to ffmpeg executable
    'outtmpl': '%(title)s.%(ext)s',              # Output file naming template
    'quiet': False,                              # Show download progress
    'noplaylist': True                           # Download only one video if playlist
}

# Example URL — Replace with your desired video link
video_url = 'https://www.youtube.com/watch?v=J3GiM2DxUlc'

# Start downloading
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
