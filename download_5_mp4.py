# -*- coding: utf-8 -*-
import os
import sys
import imageio_ffmpeg
import yt_dlp

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)

output_dir = r"D:\Downloads\Lagu pembasuhan\Video_MP4"
os.makedirs(output_dir, exist_ok=True)

songs = [
    {
        "num": 1,
        "name": "1. Seperti Rusa yang Rindu Sungai-Mu",
        "url": "https://www.youtube.com/watch?v=ggU3kDvN0RE"
    },
    {
        "num": 2,
        "name": "2. Sejauh Timur Dari Barat",
        "url": "https://www.youtube.com/watch?v=EvRq3dF4mks"
    },
    {
        "num": 3,
        "name": "3. Sujud Di Altar-Nya",
        "url": "https://www.youtube.com/watch?v=uNXLkMSAWKc"
    },
    {
        "num": 4,
        "name": "4. Hati Sebagai Hamba",
        "url": "https://www.youtube.com/watch?v=DFQ_OBbmDxk"
    },
    {
        "num": 5,
        "name": "5. Sentuh Hatiku",
        "url": "https://www.youtube.com/watch?v=-3cEhTJkiSc"
    }
]

print(f"Mengunduh 5 video MP4 ke: {output_dir}")
print(f"FFmpeg binary: {ffmpeg_exe}")

for s in songs:
    print(f"\n==========================================")
    print(f"[{s['num']}/5] Mengunduh: {s['name']}")
    print(f"URL: {s['url']}")
    print(f"==========================================")
    
    out_template = os.path.join(output_dir, f"{s['name']} - %(title)s.%(ext)s")
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': out_template,
        'ffmpeg_location': ffmpeg_exe,
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'quiet': False,
        'no_warnings': False
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([s['url']])
        print(f"BERHASIL: {s['name']}")
    except Exception as e:
        print(f"GAGAL {s['name']}: {e}")

print("\n--- SELESAI SEMUA ---")
print("Daftar file di folder:")
for f in os.listdir(output_dir):
    print(" -", f)
