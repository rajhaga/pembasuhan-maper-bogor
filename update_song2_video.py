# -*- coding: utf-8 -*-
import os
import imageio_ffmpeg
import yt_dlp

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
output_dir = r"D:\Downloads\Lagu pembasuhan\Video_MP4"
url = "https://youtu.be/AiO90i4Rybk?si=4YR4Swb8ZQHXYFvx"

# Remove old file for song 2
for f in os.listdir(output_dir):
    if f.startswith("2."):
        old_path = os.path.join(output_dir, f)
        print(f"Removing old video: {old_path}")
        os.remove(old_path)

out_template = os.path.join(output_dir, "2. Sejauh Timur Dari Barat - %(title)s.%(ext)s")

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': out_template,
    'ffmpeg_location': ffmpeg_exe,
    'merge_output_format': 'mp4',
    'noplaylist': True
}

print("Downloading new video for Sejauh Timur Dari Barat...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("\nFinished! Current files in Video_MP4:")
for f in sorted(os.listdir(output_dir)):
    p = os.path.join(output_dir, f)
    print(" -", f, f"({round(os.path.getsize(p)/1024/1024, 2)} MB)")
