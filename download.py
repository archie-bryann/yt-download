import yt_dlp
import os

# Make sure ffmpeg path is correctly set for merging video and audio
FFMPEG_PATH = os.path.join("C:", os.sep, "ffmpeg", "bin", "ffmpeg.exe")

# yt-dlp configuration options
ydl_opts = {
    # 'format': 'bestvideo+bestaudio/best',        # Select best video and best audio (usually 8k)
    'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]', # 4k
    'merge_output_format': 'mp4',                # Output format after merging
    'ffmpeg_location': FFMPEG_PATH,              # Path to ffmpeg executable
    'outtmpl': '%(title)s.%(ext)s',              # Output file naming template
    'quiet': False,                              # Show download progress
    'noplaylist': True                           # Download only one video if playlist
}

# Example URL — Replace with your desired video link
video_url = 'https://www.youtube.com/watch?v=2y2Z06hVmWE'

# Start downloading
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])