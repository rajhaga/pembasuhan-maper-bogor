# -*- coding: utf-8 -*-
"""
Fast Video Encoder for Pembasuhan MAPER PERMATA GBKP Rg. Bogor.
Encodes 1080p MP4 from pre-rendered slides and master audio at 15fps ultrafast.
Includes +faststart and 320kbps audio.
"""

import os
import sys
import time
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
work_dir = r"D:\Downloads\Lagu pembasuhan"
slides_dir = os.path.join(work_dir, "temp_video_slides")
concat_file = os.path.join(slides_dir, "concat_slides.txt")
master_audio_path = os.path.join(work_dir, "MASTER_PEMBASUHAN_MAPER_60_MENIT.mp3")
output_video_path = os.path.join(work_dir, "VIDEO_PEMBASUHAN_MAPER_60_MENIT.mp4")

if not os.path.exists(concat_file):
    print("Error: concat_slides.txt not found!")
    sys.exit(1)

if not os.path.exists(master_audio_path):
    print("Error: Master MP3 not found!")
    sys.exit(1)

print("=" * 65)
print("  MEMULAI ENCODING VIDEO MP4 FULL HD 1080P")
print("  PEMBASUHAN MAPER PERMATA GBKP RG. BOGOR (56:44)")
print("=" * 65)

cmd = [
    ffmpeg_exe, "-y",
    "-f", "concat", "-safe", "0", "-i", concat_file,
    "-i", master_audio_path,
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-crf", "20",
    "-pix_fmt", "yuv420p",
    "-r", "15",
    "-g", "150",
    "-c:a", "aac",
    "-b:a", "320k",
    "-movflags", "+faststart",
    "-shortest",
    output_video_path
]

t0 = time.time()
print("Menjalankan FFmpeg...")
proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, universal_newlines=True)

last_print = 0
for line in proc.stderr:
    line_s = line.strip()
    if 'time=' in line_s and 'speed=' in line_s:
        now = time.time()
        if now - last_print >= 5: # print every 5 seconds
            print(f"  Progres: {line_s}")
            last_print = now

proc.wait()

if proc.returncode != 0:
    print(f"Error: FFmpeg exited with code {proc.returncode}")
    sys.exit(1)

elapsed = time.time() - t0
print("=" * 65)
print(f"  SELESAI! Video berhasil dibuat dalam {elapsed:.1f} detik ({elapsed/60:.2f} menit)")
print(f"  File Output: {output_video_path}")
if os.path.exists(output_video_path):
    size_mb = os.path.getsize(output_video_path) / (1024 * 1024)
    print(f"  Ukuran File: {size_mb:.2f} MB")
print("=" * 65)
