# -*- coding: utf-8 -*-
"""
Full HD 1080p Video Producer for Pembasuhan MAPER PERMATA GBKP Rg. Bogor.
Incorporates updated canonical lyrics:
- Seperti Rusa (Bait 1, 2, Chorus 'Yesus Yesus Kau berarti bagiku...')
- Sejauh Timur Dari Barat (Tubir laut & Tak Kau pandang hina hati yang hancur)
- Sujud Di Altar-Nya (Kutanya Yesus & Pemulihan mukjizat kemenangan)
- Hati Sebagai Hamba (Verse, Chorus 'Dalam Roh dan kebenaran', Bridge)
- Sentuh Hatiku (Verse 1, 2, Chorus)
- Hari Ini Kurasa Bahagia (Mempersatukan kita & Bergandingan tangan)
- Verified Bible Scriptures (TB LAI)
"""

import os
import sys
import time
import subprocess
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
work_dir = r"D:\Downloads\Lagu pembasuhan"
slides_dir = os.path.join(work_dir, "temp_video_slides")
os.makedirs(slides_dir, exist_ok=True)

master_audio_path = os.path.join(work_dir, "MASTER_PEMBASUHAN_MAPER_60_MENIT.mp3")
output_video_path = os.path.join(work_dir, "VIDEO_PEMBASUHAN_MAPER_60_MENIT.mp4")

# Load Windows System Fonts
f_header_title = ImageFont.truetype('segoeuib.ttf', 24)
f_header_sub = ImageFont.truetype('segoeui.ttf', 20)
f_badge = ImageFont.truetype('segoeuib.ttf', 20)
f_slide_title = ImageFont.truetype('segoeuib.ttf', 44)
f_slide_sub = ImageFont.truetype('segoeuib.ttf', 26)
f_body_scripture = ImageFont.truetype('georgia.ttf', 32)
f_body_lyrics = ImageFont.truetype('segoeuib.ttf', 46)
f_body_text = ImageFont.truetype('segoeui.ttf', 28)
f_footer = ImageFont.truetype('segoeui.ttf', 20)

f_alert_title = ImageFont.truetype('segoeuib.ttf', 28)
f_alert_count = ImageFont.truetype('segoeuib.ttf', 52)
f_alert_body = ImageFont.truetype('segoeuib.ttf', 24)
f_alert_sub = ImageFont.truetype('segoeui.ttf', 20)

def format_time(sec):
    m = int(sec // 60)
    s = int(sec % 60)
    return f"{m:02d}:{s:02d}"

def create_base_canvas():
    img = Image.new('RGB', (1920, 1080), color=(11, 16, 29))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(25, 25), (1895, 1055)], outline=(35, 50, 78), width=2)
    draw.rectangle([(25, 25), (1895, 95)], fill=(16, 24, 44))
    draw.line([(25, 95), (1895, 95)], fill=(212, 175, 55), width=2)
    draw.rectangle([(25, 995), (1895, 1055)], fill=(14, 20, 36))
    draw.line([(25, 995), (1895, 995)], fill=(45, 60, 90), width=1)
    return img, draw

def render_slide(slide_data, current_time_sec, countdown_val=None, alert_info=None):
    img, draw = create_base_canvas()
    
    # 1. Header info
    draw.text((60, 42), "PERMATA GBKP RG. BOGOR  •  IBADAH PEMBASUHAN KAKI", font=f_header_title, fill=(212, 175, 55))
    
    badge_text = slide_data.get('badge', 'PEMBASUHAN MAPER')
    draw.rectangle([(920, 40), (1380, 80)], fill=(24, 36, 62), outline=(55, 85, 135), width=1)
    draw.text((1150, 60), badge_text, font=f_badge, fill=(200, 225, 255), anchor="mm")
    
    time_str = f"{format_time(current_time_sec)} / 56:44"
    draw.text((1840, 60), time_str, font=f_header_sub, fill=(180, 200, 230), anchor="rm")
    
    # 2. Main Content
    stype = slide_data.get('type', 'text')
    title = slide_data.get('title', '')
    sub = slide_data.get('subtitle', '')
    content = slide_data.get('content', '')
    
    title_y = 165 if alert_info else 205
    draw.text((960, title_y), title, font=f_slide_title, fill=(240, 200, 75), anchor="mm")
    if sub:
        draw.text((960, title_y + 52), sub, font=f_slide_sub, fill=(160, 190, 230), anchor="mm")
    
    content_y = title_y + 95
    
    if stype == 'lyrics':
        draw.multiline_text((960, content_y + 120), content, font=f_body_lyrics, fill=(255, 255, 255), anchor="mm", align="center", spacing=20)
    elif stype == 'scripture':
        card_top = content_y + 20
        card_bottom = card_top + 280
        draw.rectangle([(220, card_top), (1700, card_bottom)], fill=(16, 26, 48), outline=(60, 90, 140), width=2)
        draw.rectangle([(220, card_top), (235, card_bottom)], fill=(212, 175, 55))
        draw.multiline_text((960, (card_top + card_bottom)//2), content, font=f_body_scripture, fill=(240, 245, 255), anchor="mm", align="center", spacing=18)
    else:
        card_top = content_y + 15
        card_bottom = card_top + 330
        draw.rectangle([(220, card_top), (1700, card_bottom)], fill=(15, 22, 40), outline=(50, 70, 110), width=1)
        draw.multiline_text((960, (card_top + card_bottom)//2), content, font=f_body_text, fill=(235, 240, 250), anchor="mm", align="center", spacing=18)
        
    # 3. Alert Box (If in transition countdown)
    if alert_info and countdown_val is not None:
        draw.rectangle([(200, 745), (1720, 955)], fill=(32, 24, 10), outline=(255, 195, 30), width=3)
        draw.text((240, 780), "[!] PERINGATAN TRANSISI OPERATOR & WL:", font=f_alert_title, fill=(255, 215, 50))
        
        if countdown_val > 0:
            c_color = (255, 75, 75) if countdown_val <= 3 else (255, 195, 30)
            draw.text((1580, 780), f"[ {countdown_val} DETIK ]", font=f_alert_count, fill=c_color, anchor="mm")
        else:
            draw.text((1580, 780), "[ MULAI ! ]", font=f_alert_count, fill=(50, 255, 120), anchor="mm")
            
        draw.text((240, 840), f">> AKAN MASUK: {alert_info['song_title']}", font=f_alert_body, fill=(255, 255, 255))
        draw.text((240, 882), f"* Petunjuk: {alert_info['note']}", font=f_alert_sub, fill=(210, 230, 255))
        
        progress = max(0.0, min(1.0, countdown_val / 10.0))
        bar_w = int(1440 * progress)
        draw.rectangle([(240, 930), (1680, 938)], fill=(55, 45, 25))
        if bar_w > 0:
            draw.rectangle([(240, 930), (240 + bar_w, 938)], fill=(255, 195, 30))

    # 4. Footer info
    audio_cue = slide_data.get('audio_cue', "Musik: Base Song (Ambient)")
    next_cue = slide_data.get('next_cue', "")
    draw.text((60, 1025), audio_cue, font=f_footer, fill=(170, 190, 220), anchor="lm")
    if next_cue:
        draw.text((1840, 1025), f"Berikutnya: {next_cue}", font=f_footer, fill=(212, 175, 55), anchor="rm")
        
    return img

print("Building Updated Slide Sequence with Revised Lyrics...")
slides = []

# --- SEGMENT 1: 00:00 - 01:30 (90s) ---
slides.append({
    'duration': 40.0,
    'badge': 'SESI 1: PENGANTAR',
    'type': 'text',
    'title': 'IBADAH PEMBASUHAN KAKI',
    'subtitle': 'Masa Pengakrabian (MAPER) PERMATA GBKP Runggun Bogor 2026',
    'content': 'Bukan berangkat dari kepantasan diri kita,\nmelainkan bagaimana kita dan Tuhan saling menerima\ndalam kerendahan hati yang seutuhnya.\n\n"Saling Merendahkan Hati & Mengasihi di dalam Kristus"',
    'audio_cue': 'Musik: Base Song Ambient (Leave It in God\'s Hands) • WL Menyapa',
    'next_cue': 'Petunjuk Masuk Hening (00:40)'
})

slides.append({
    'duration': 40.0,
    'badge': 'SESI 1: SAAT HENING',
    'type': 'text',
    'title': 'PETUNJUK AWAL & SAAT HENING',
    'subtitle': 'Menenangkan Pikiran dan Batin di Hadapan Tuhan',
    'content': '• Silakan menonaktifkan atau menyimpan telepon genggam (gadget)\n• Mengambil posisi duduk yang tenang, rileks, dan nyaman\n• Menutup mata perlahan, melepaskan kepenatan dan kesibukan\n• Membuka hati untuk mengalami perjumpaan dan pemulihan dari Tuhan',
    'audio_cue': 'Musik: Base Song Ambient • WL Mengajak Hening',
    'next_cue': 'Lagu 1: Seperti Rusa (01:30)'
})

alert_1 = {
    'song_title': 'Lagu 1: Seperti Rusa yang Rindu Sungai-Mu (Do = D)',
    'note': 'WL & Jemaat bersiap bernyanyi bersama dalam keheningan'
}
for c in range(10, 0, -1):
    slides.append({
        'duration': 1.0,
        'badge': 'SESI 1: TRANSISI',
        'type': 'text',
        'title': 'PETUNJUK AWAL & SAAT HENING',
        'subtitle': 'Menenangkan Pikiran dan Batin di Hadapan Tuhan',
        'content': '• Silakan menonaktifkan atau menyimpan telepon genggam (gadget)\n• Mengambil posisi duduk yang tenang, rileks, dan nyaman\n• Menutup mata perlahan, melepaskan kepenatan dan kesibukan\n• Membuka hati untuk mengalami perjumpaan dan pemulihan dari Tuhan',
        'audio_cue': 'Base Song Memudar (Fade-out) -> Solo Piano Masuk',
        'next_cue': 'Lagu 1: Seperti Rusa (01:30)',
        'alert': alert_1,
        'countdown': c
    })

# --- SEGMENT 2: LAGU 1 - SEPERTI RUSA (01:30 - 06:00 = 270s) ---
slides.append({
    'duration': 18.0,
    'badge': 'SESI 2: LAGU 1',
    'type': 'lyrics',
    'title': 'SEPERTI RUSA YANG RINDU SUNGAI-MU',
    'subtitle': 'Nada Dasar: Do = D  •  Musik Solo Piano',
    'content': '[ INTRO MUSIK PIANO ]\n\nBersiap Masuk Bait 1',
    'audio_cue': 'Musik: Solo Piano (Bersih & Teduh)',
    'next_cue': 'Bait 1'
})
slides.append({
    'duration': 37.0,
    'badge': 'SESI 2: LAGU 1',
    'type': 'lyrics',
    'title': 'SEPERTI RUSA YANG RINDU SUNGAI-MU',
    'subtitle': '[ BAIT 1 ]',
    'content': 'S\'perti rusa rindu sungai-Mu\nJiwaku rindu Engkau\nKaulah Tuhan hasrat hatiku\nKurindu menyembah-Mu',
    'audio_cue': 'Musik: Solo Piano • Jemaat Bernyanyi Bersama',
    'next_cue': 'Bait 2'
})
slides.append({
    'duration': 37.0,
    'badge': 'SESI 2: LAGU 1',
    'type': 'lyrics',
    'title': 'SEPERTI RUSA YANG RINDU SUNGAI-MU',
    'subtitle': '[ BAIT 2 ]',
    'content': 'Engkau kekuatan dan perisaiku\nKepada-Mu rohku berserah\nKaulah Tuhan hasrat hatiku\nKurindu menyembah-Mu',
    'audio_cue': 'Musik: Solo Piano • Jemaat Bernyanyi Bersama',
    'next_cue': 'Chorus / Reff'
})
slides.append({
    'duration': 55.0,
    'badge': 'SESI 2: LAGU 1',
    'type': 'lyrics',
    'title': 'SEPERTI RUSA YANG RINDU SUNGAI-MU',
    'subtitle': '[ CHORUS / REFF ]',
    'content': 'Yesus, Yesus\nKau berarti bagiku\nYesus, Yesus\nKau segalanya bagiku',
    'audio_cue': 'Musik: Solo Piano • Menyembah Yesus',
    'next_cue': 'Pengulangan Khusyuk'
})
slides.append({
    'duration': 50.0,
    'badge': 'SESI 2: LAGU 1',
    'type': 'lyrics',
    'title': 'SEPERTI RUSA YANG RINDU SUNGAI-MU',
    'subtitle': '[ PENGHAYATAN BERSAMA ]',
    'content': 'Engkau kekuatan dan perisaiku\nKepada-Mu rohku berserah\n\nYesus, Yesus, Kau berarti bagiku\nYesus, Yesus, Kau segalanya bagiku',
    'audio_cue': 'Musik: Solo Piano • Mengangkat Sembah',
    'next_cue': 'Reff Akhir'
})
slides.append({
    'duration': 38.0,
    'badge': 'SESI 2: LAGU 1',
    'type': 'lyrics',
    'title': 'SEPERTI RUSA YANG RINDU SUNGAI-MU',
    'subtitle': '[ REFF AKHIR ]',
    'content': 'Yesus, Yesus, Kau berarti bagiku\nYesus, Yesus, Kau segalanya bagiku',
    'audio_cue': 'Musik: Solo Piano • Berserah Penuh',
    'next_cue': 'Outro Piano (05:25)'
})
slides.append({
    'duration': 35.0,
    'badge': 'SESI 2: LAGU 1',
    'type': 'lyrics',
    'title': 'SEPERTI RUSA YANG RINDU SUNGAI-MU',
    'subtitle': '[ OUTRO PIANO ]',
    'content': '"Yesus, Yesus, Kau segalanya bagiku..."\n\n[ Menjaga Hati Tetap Hening di Hadapan Tuhan ]',
    'audio_cue': 'Solo Piano Berakhir -> Base Song Mulai Masuk Lembut',
    'next_cue': 'Refleksi Kerapuhan (06:00)'
})

# --- SEGMENT 3: REFLEKSI KERAPUHAN (06:00 - 08:00 = 120s) ---
slides.append({
    'duration': 55.0,
    'badge': 'SESI 3: REFLEKSI',
    'type': 'text',
    'title': 'REFLEKSI: MENGAKUI KERAPUHAN DIRI',
    'subtitle': 'Datang Apa Adanya di Hadapan Hadirat Bapa',
    'content': 'Kita sering merasa harus tampil kuat, mandiri, dan tanpa cela.\nNamun malam ini, di hadapan Tuhan, kita boleh menanggalkan topeng kita.\n\nBawalah keletihan, kerapuhan, luka hati, dan rasa bersalahmu.\nTuhan tidak menuntut kesempurnaan;\nIa hanya merindukan hati yang jujur dan berserah kepada-Nya.',
    'audio_cue': 'Musik: Base Song Ambient • WL Mengajak Refleksi',
    'next_cue': 'Firman: Yesaya 1:18 (06:55)'
})
slides.append({
    'duration': 55.0,
    'badge': 'SESI 3: FIRMAN TUHAN',
    'type': 'scripture',
    'title': 'FIRMAN PENGAMPUNAN ALLAH',
    'subtitle': 'Kitab Yesaya 1:18 (Terjemahan Baru LAI [Terverifikasi])',
    'content': '"Marilah, baiklah kita beperkara! — firman TUHAN —\nSekalipun dosamu merah seperti kirmizi,\nakan menjadi putih seperti salju;\nsekalipun berwarna merah seperti kain kesumba,\nakan menjadi putih seperti bulu domba."',
    'audio_cue': 'Musik: Base Song Ambient • Menghayati Kasih Karunia',
    'next_cue': 'Lagu 2: Sejauh Timur Dari Barat (08:00)'
})

alert_2 = {
    'song_title': 'Lagu 2: Sejauh Timur Dari Barat (Do = C / D)',
    'note': 'Mengakui kasih pengampunan Allah yang memulihkan hidup kita'
}
for c in range(10, 0, -1):
    slides.append({
        'duration': 1.0,
        'badge': 'SESI 3: TRANSISI',
        'type': 'scripture',
        'title': 'FIRMAN PENGAMPUNAN ALLAH',
        'subtitle': 'Kitab Yesaya 1:18',
        'content': '"Marilah, baiklah kita beperkara! — firman TUHAN —\nSekalipun dosamu merah seperti kirmizi, akan menjadi putih seperti salju; sekalipun berwarna merah seperti kain kesumba, akan menjadi putih seperti bulu domba."',
        'audio_cue': 'Base Song Memudar (Fade-out) -> Solo Piano Masuk',
        'next_cue': 'Lagu 2: Sejauh Timur Dari Barat (08:00)',
        'alert': alert_2,
        'countdown': c
    })

# --- SEGMENT 4: LAGU 2 - SEJAUH TIMUR DARI BARAT (08:00 - 13:35 = 335s) ---
slides.append({
    'duration': 20.0,
    'badge': 'SESI 4: LAGU 2',
    'type': 'lyrics',
    'title': 'SEJAUH TIMUR DARI BARAT',
    'subtitle': 'Nada Dasar: Do = C / D  •  Musik Solo Piano',
    'content': '[ INTRO MUSIK PIANO ]\n\nBersiap Masuk Bait 1',
    'audio_cue': 'Musik: Solo Piano (Bersih & Syahdu)',
    'next_cue': 'Bait 1'
})
slides.append({
    'duration': 50.0,
    'badge': 'SESI 4: LAGU 2',
    'type': 'lyrics',
    'title': 'SEJAUH TIMUR DARI BARAT',
    'subtitle': '[ BAIT 1 ]',
    'content': 'Sejauh timur dari barat\nEngkau membuang dosaku\nTiada Kau ingat lagi pelanggaranku',
    'audio_cue': 'Musik: Solo Piano • Jemaat Bernyanyi Bersama',
    'next_cue': 'Bait 2'
})
slides.append({
    'duration': 50.0,
    'badge': 'SESI 4: LAGU 2',
    'type': 'lyrics',
    'title': 'SEJAUH TIMUR DARI BARAT',
    'subtitle': '[ BAIT 2 ]',
    'content': 'Jauh ke dalam tubir laut\nKau melemparkan dosaku\nTiada Kau perhitungkan kesalahanku',
    'audio_cue': 'Musik: Solo Piano • Jemaat Bernyanyi Bersama',
    'next_cue': 'Reff / Chorus'
})
slides.append({
    'duration': 60.0,
    'badge': 'SESI 4: LAGU 2',
    'type': 'lyrics',
    'title': 'SEJAUH TIMUR DARI BARAT',
    'subtitle': '[ REFF / CHORUS ]',
    'content': 'Betapa besar kasih pengampunan-Mu Tuhan\nTak Kau pandang hina hati yang hancur\nKu berterima kasih kepada-Mu ya Tuhan\nPengampunan yang Kau beri pulihkanku',
    'audio_cue': 'Musik: Solo Piano • Mengakui Kesetiaan Tuhan',
    'next_cue': 'Pengulangan'
})
slides.append({
    'duration': 60.0,
    'badge': 'SESI 4: LAGU 2',
    'type': 'lyrics',
    'title': 'SEJAUH TIMUR DARI BARAT',
    'subtitle': '[ PENGHAYATAN BERSAMA ]',
    'content': 'Jauh ke dalam tubir laut\nKau melemparkan dosaku...\n\nBetapa besar kasih pengampunan-Mu Tuhan\nTak Kau pandang hina hati yang hancur',
    'audio_cue': 'Musik: Solo Piano • Sungguh-sungguh Bersyukur',
    'next_cue': 'Reff Puncak'
})
slides.append({
    'duration': 60.0,
    'badge': 'SESI 4: LAGU 2',
    'type': 'lyrics',
    'title': 'SEJAUH TIMUR DARI BARAT',
    'subtitle': '[ REFF PUNCAK ]',
    'content': 'Betapa besar kasih pengampunan-Mu Tuhan\nTak Kau pandang hina hati yang hancur\nKu berterima kasih kepada-Mu ya Tuhan\nPengampunan yang Kau beri pulihkanku',
    'audio_cue': 'Musik: Solo Piano • Menghayati Cinta Kasih-Nya',
    'next_cue': 'Outro Piano (13:00)'
})
slides.append({
    'duration': 35.0,
    'badge': 'SESI 4: LAGU 2',
    'type': 'lyrics',
    'title': 'SEJAUH TIMUR DARI BARAT',
    'subtitle': '[ OUTRO PIANO ]',
    'content': '"Pengampunan yang Kau beri pulihkanku..."\n\n[ Menjaga Hati Tetap Hening & Bersyukur ]',
    'audio_cue': 'Solo Piano Selesai -> Base Song Masuk Lembut',
    'next_cue': 'Tangan di Dada (13:35)'
})

# --- SEGMENT 5: TANGAN DI DADA (13:35 - 18:00 = 265s) ---
slides.append({
    'duration': 60.0,
    'badge': 'SESI 5: TANGAN DI DADA',
    'type': 'text',
    'title': 'SAAT HENING: MELETAKKAN TANGAN DI DADA',
    'subtitle': 'Menghayati Detak Kehidupan & Hadirat Tuhan',
    'content': '• Silakan letakkan tangan kananmu di dada sebelah kiri\n• Rasakan setiap detak jantung yang Tuhan masih anugerahkan hingga saat ini\n• Tarik napas perlahan... sadarilah napas hidup ini berasal dari Allah semata\n• Tidak ada yang tersembunyi bagi-Nya; Ia mengenal setiap luka dan air matamu',
    'audio_cue': 'Musik: Base Song Ambient • Suasana Khidmat & Intim',
    'next_cue': 'Saat Hening Doa Pribadi 2 Menit (14:35)'
})
slides.append({
    'duration': 60.0,
    'badge': 'SESI 5: DOA PRIBADI 2 MENIT',
    'type': 'text',
    'title': 'DOA PRIBADI DI HADAPAN HADIRAT ALLAH',
    'subtitle': 'Waktu Hening Khusus Bersama Bapa (2 Menit)',
    'content': 'Bawalah seluruh keletihan, pergumulan masa muda, kekhawatiran masa depan,\ndan rasa bersalah yang membebanimu ke hadapan Tuhan.\n\nKatakan dalam hatimu: "Tuhan, ini aku apa adanya. Aku butuh Engkau."\n\n[ Tetap letakkan tangan di dada & berdoa dalam keheningan batin ]',
    'audio_cue': 'Musik: Base Song Ambient • Doa Pribadi Berjalan',
    'next_cue': 'Firman: Yeremia 29:11-12 (15:35)'
})
slides.append({
    'duration': 65.0,
    'badge': 'SESI 5: JANJI ALLAH',
    'type': 'scripture',
    'title': 'JANJI PEMULIHAN DARI ALLAH',
    'subtitle': 'Kitab Yeremia 29:11-12 (Terjemahan Baru LAI [Terverifikasi])',
    'content': '"Sebab Aku ini mengetahui rancangan-rancangan apa yang ada pada-Ku mengenai kamu,\ndemikianlah firman TUHAN, yaitu rancangan damai sejahtera dan bukan rancangan kecelakaan,\nuntuk memberikan kepadamu hari depan yang penuh harapan.\nDan apabila kamu berseru dan datang untuk berdoa kepada-Ku, maka Aku akan mendengarkan kamu."',
    'audio_cue': 'Musik: Base Song Ambient • Meresapi Janji Tuhan',
    'next_cue': 'Doa Sahabat (16:40)'
})
slides.append({
    'duration': 70.0,
    'badge': 'SESI 5: DOA SAHABAT',
    'type': 'scripture',
    'title': 'PERSEKUTUAN & DOA SAHABAT',
    'subtitle': 'Surat Yakobus 5:16 (Terjemahan Baru LAI [Terverifikasi])',
    'content': '"Karena itu hendaklah kamu saling mengaku dosamu dan saling mendoakan,\nsupaya kamu sembuh.\nDoa orang yang benar, bila dengan yakin didoakan, sangat besar kuasanya."\n\nDi dalam PERMATA, kita dipanggil untuk tidak berjalan sendirian.\nMari saling mendoakan dan menopang dalam kasih persaudaraan Kristus.',
    'audio_cue': 'Musik: Base Song Ambient • Momen Saling Mendoakan',
    'next_cue': 'Lagu 3: Sujud Di Altar-Nya (18:00)'
})

alert_3 = {
    'song_title': 'Lagu 3: Sujud Di Altar-Nya (Do = D / E)',
    'note': 'Saling mendoakan & menyerahkan beban hidup di hadapan altar Tuhan'
}
for c in range(10, 0, -1):
    slides.append({
        'duration': 1.0,
        'badge': 'SESI 5: TRANSISI',
        'type': 'text',
        'title': 'PERSEKUTUAN & DOA SAHABAT',
        'subtitle': 'Surat Yakobus 5:16 • Saling Menopang dalam Kasih',
        'content': '"Hendaklah kamu saling mengaku dosamu dan saling mendoakan, supaya kamu sembuh."\n\nDi dalam PERMATA, kita dipanggil untuk tidak berjalan sendirian.\nTeman di sebelahmu adalah saudaramu seiman yang siap menopangmu.',
        'audio_cue': 'Base Song Memudar (Fade-out) -> Solo Piano Masuk',
        'next_cue': 'Lagu 3: Sujud Di Altar-Nya (18:00)',
        'alert': alert_3,
        'countdown': c
    })

# --- SEGMENT 6: LAGU 3 - SUJUD DI ALTAR-NYA (18:00 - 23:35 = 335s) ---
slides.append({
    'duration': 25.0,
    'badge': 'SESI 6: LAGU 3',
    'type': 'lyrics',
    'title': 'SUJUD DI ALTAR-NYA',
    'subtitle': 'Nada Dasar: Do = D / E  •  Musik Solo Piano',
    'content': '[ INTRO MUSIK PIANO ]\n\nBersiap Masuk Bait 1',
    'audio_cue': 'Musik: Solo Piano (Khidmat & Menyentuh)',
    'next_cue': 'Bait 1'
})
slides.append({
    'duration': 50.0,
    'badge': 'SESI 6: LAGU 3',
    'type': 'lyrics',
    'title': 'SUJUD DI ALTAR-NYA',
    'subtitle': '[ BAIT 1 ]',
    'content': 'Bila hati terasa berat\nTak seorang pun mengerti bebanku\nKutanya Yesus: apa yang harus kubuat?\nDia berfirman mari datanglah\nDia selalu pedulikan aku\nKudatang Yesus: Dia pikul segala bebanku',
    'audio_cue': 'Musik: Solo Piano • Jemaat Bernyanyi Bersama',
    'next_cue': 'Reff / Chorus'
})
slides.append({
    'duration': 65.0,
    'badge': 'SESI 6: LAGU 3',
    'type': 'lyrics',
    'title': 'SUJUD DI ALTAR-NYA',
    'subtitle': '[ REFF / CHORUS ]',
    'content': 'Sujud di altar-Nya, kubawa hidupku\nKuterima anugerah-Nya\nDia ampuniku dan bebaskanku\nDia ubah hidupku, baharui hatiku\nSesuatu terjadi saat datang di altar-Nya',
    'audio_cue': 'Musik: Solo Piano • Berserah di Hadapan Salib',
    'next_cue': 'Saling Mendoakan Sahabat'
})
slides.append({
    'duration': 65.0,
    'badge': 'SESI 6: LAGU 3',
    'type': 'lyrics',
    'title': 'SUJUD DI ALTAR-NYA',
    'subtitle': '[ PENGHAYATAN DOA BERSAMA ]',
    'content': 'Kutanya Yesus: apa yang harus kubuat?\nKudatang Yesus: Dia pikul segala bebanku\n\nSujud di altar-Nya, kubawa hidupku\nKuterima anugerah-Nya, Dia ampuniku dan bebaskanku',
    'audio_cue': 'Musik: Solo Piano • Berdoa Menumpangkan Tangan',
    'next_cue': 'Kemenangan & Pemulihan'
})
slides.append({
    'duration': 50.0,
    'badge': 'SESI 6: LAGU 3',
    'type': 'lyrics',
    'title': 'SUJUD DI ALTAR-NYA',
    'subtitle': '[ KEMENANGAN TERJADI ]',
    'content': 'Pemulihan terjadi\nMukjizat terjadi\nKemenangan terjadi\nSaat datang di altar-Nya!',
    'audio_cue': 'Musik: Solo Piano • Deklarasi Kemenangan',
    'next_cue': 'Reff Akhir'
})
slides.append({
    'duration': 50.0,
    'badge': 'SESI 6: LAGU 3',
    'type': 'lyrics',
    'title': 'SUJUD DI ALTAR-NYA',
    'subtitle': '[ REFF AKHIR ]',
    'content': 'Sujud di altar-Nya, kubawa hidupku\nKuterima anugerah-Nya\nDia ubah hidupku, baharui hatiku\nSesuatu terjadi saat datang di altar-Nya',
    'audio_cue': 'Musik: Solo Piano • Penyerahan Penuh',
    'next_cue': 'Outro Piano (23:05)'
})
slides.append({
    'duration': 30.0,
    'badge': 'SESI 6: LAGU 3',
    'type': 'lyrics',
    'title': 'SUJUD DI ALTAR-NYA',
    'subtitle': '[ OUTRO PIANO ]',
    'content': '"Sesuatu terjadi saat datang di altar-Nya..."\n\n[ Menjaga Keheningan & Menatap Salib Kristus ]',
    'audio_cue': 'Solo Piano Selesai -> Base Song Masuk Lembut',
    'next_cue': 'Prosesi Kendi Air (23:35)'
})

# --- SEGMENT 7: KENDI AIR & FILIPI 2 (23:35 - 26:30 = 175s) ---
slides.append({
    'duration': 60.0,
    'badge': 'SESI 7: PROSESI AIR',
    'type': 'text',
    'title': 'PROSESI KENDI AIR & BASKOM',
    'subtitle': 'Lampu Ruangan Diredupkan  •  Suara Gemercik Air Mengalir',
    'content': 'Para Pengurus PERMATA Rg. Bogor perlahan berjalan membawa:\nKendi berisi air bersih, baskom pembasuhan, dan kain handuk putih.\n\nMempersiapkan tempat untuk melayani dan menyambut\nsetiap adik-adik dan rekan pemuda di hadapan Tuhan.',
    'audio_cue': 'Musik: Base Song Ambient • Suasana Khidmat & Kudus',
    'next_cue': 'Firman: Filipi 2:3,5-7 (24:35)'
})
slides.append({
    'duration': 60.0,
    'badge': 'SESI 7: TELADAN KRISTUS',
    'type': 'scripture',
    'title': 'TELADAN KERENDAHAN HATI KRISTUS',
    'subtitle': 'Surat Filipi 2:3, 5-7 (Terjemahan Baru LAI [Terverifikasi])',
    'content': '"Hendaklah dengan rendah hati yang seorang menganggap yang lain lebih utama dari pada dirinya sendiri...\nHendaklah kamu dalam hidupmu bersama, menaruh pikiran dan perasaan yang terdapat juga dalam Kristus Yesus,\nyang walaupun dalam rupa Allah, tidak menganggap kesetaraan dengan Allah itu sebagai milik yang harus dipertahankan,\nmelainkan telah mengosongkan diri-Nya sendiri, dan mengambil rupa seorang hamba, dan menjadi sama dengan manusia."',
    'audio_cue': 'Musik: Base Song Ambient • Merenungkan Kerendahan Hati',
    'next_cue': 'Pengurus Bersiap (25:35)'
})
slides.append({
    'duration': 45.0,
    'badge': 'SESI 7: PENGURUS BERSIAP',
    'type': 'text',
    'title': 'PENGURUS PERMATA BERSIAP MELAYANI',
    'subtitle': 'Mengambil Rupa Seorang Hamba di Depan Peserta',
    'content': 'Pengurus bersujud dan duduk bersimpuh di depan kursi pembasuhan.\nMeneladani kerendahan hati Kristus yang membasuh kaki murid-murid-Nya.\n\nPengurus bersiap menyanyikan pujian ikrar kerendahan hati.',
    'audio_cue': 'Musik: Base Song Ambient • Pengurus Mengambil Posisi',
    'next_cue': 'Lagu 4: Hati Sebagai Hamba (26:30)'
})

alert_4 = {
    'song_title': 'Lagu 4: Hati Sebagai Hamba (Do = C / D)',
    'note': 'Dinyanyikan khusus oleh Pengurus PERMATA Bogor'
}
for c in range(10, 0, -1):
    slides.append({
        'duration': 1.0,
        'badge': 'SESI 7: TRANSISI',
        'type': 'text',
        'title': 'PENGURUS PERMATA BERSIAP MELAYANI',
        'subtitle': 'Mengambil Rupa Seorang Hamba di Depan Peserta',
        'content': 'Pengurus bersujud dan duduk bersimpuh di depan kursi pembasuhan.\nMeneladani kerendahan hati Kristus yang membasuh kaki murid-murid-Nya.\n\nPengurus bersiap menyanyikan pujian penyerahan hati.',
        'audio_cue': 'Base Song Memudar (Fade-out) -> Solo Piano Masuk',
        'next_cue': 'Lagu 4: Hati Sebagai Hamba (26:30)',
        'alert': alert_4,
        'countdown': c
    })

# --- SEGMENT 8: LAGU 4 - HATI SEBAGAI HAMBA (26:30 - 31:18 = 288s) ---
slides.append({
    'duration': 25.0,
    'badge': 'SESI 8: LAGU 4',
    'type': 'lyrics',
    'title': 'HATI SEBAGAI HAMBA',
    'subtitle': 'Nada Dasar: Do = C / D  •  Dinyanyikan Khusus oleh Pengurus',
    'content': '[ INTRO MUSIK PIANO ]\n\nPengurus Bersiap Bernyanyi',
    'audio_cue': 'Musik: Solo Piano • Pengurus Memulai Nyanyian',
    'next_cue': 'Verse'
})
slides.append({
    'duration': 60.0,
    'badge': 'SESI 8: LAGU 4',
    'type': 'lyrics',
    'title': 'HATI SEBAGAI HAMBA',
    'subtitle': '[ VERSE - DINYANYIKAN PENGURUS ]',
    'content': 'Ku tak membawa apapun juga\nSaat ku datang ke dunia\nKu tinggal semua pada akhirnya\nSaat ku kembali ke surga',
    'audio_cue': 'Musik: Solo Piano • Suara Nyanyian Pengurus',
    'next_cue': 'Chorus'
})
slides.append({
    'duration': 65.0,
    'badge': 'SESI 8: LAGU 4',
    'type': 'lyrics',
    'title': 'HATI SEBAGAI HAMBA',
    'subtitle': '[ CHORUS ]',
    'content': 'Inilah yang kupunya\nHati s\'bagai hamba\nYang mau taat dan setia\nPada-Mu Bapa\n\nKemanapun kubawa\nHati yang menyembah\nDalam Roh dan kebenaran\nSampai s\'lamanya',
    'audio_cue': 'Musik: Solo Piano • Komitmen Melayani',
    'next_cue': 'Bridge'
})
slides.append({
    'duration': 75.0,
    'badge': 'SESI 8: LAGU 4',
    'type': 'lyrics',
    'title': 'HATI SEBAGAI HAMBA',
    'subtitle': '[ BRIDGE & PENGHAYATAN ]',
    'content': 'Bagaimana ku membalas kasih-Mu?\nS\'gala yang kupunya itu milik-Mu\nItu milik-Mu oh...\n\nInilah yang kupunya: hati s\'bagai hamba\nYang mau taat dan setia pada-Mu Bapa',
    'audio_cue': 'Musik: Solo Piano • Kerendahan Hati Bersimpuh',
    'next_cue': 'Outro Piano (30:15)'
})
slides.append({
    'duration': 63.0,
    'badge': 'SESI 8: LAGU 4',
    'type': 'lyrics',
    'title': 'HATI SEBAGAI HAMBA',
    'subtitle': '[ OUTRO PIANO ]',
    'content': '"Dalam Roh dan kebenaran sampai s\'lamanya..."\n\n[ Pengurus Tetap Bersimpuh di Depan Kursi Pembasuhan ]',
    'audio_cue': 'Solo Piano Selesai -> Base Song Masuk Lembut',
    'next_cue': 'Penyambutan PERMATA Bogor (31:18)'
})

# --- SEGMENT 9: PENYAMBUTAN PERMATA BOGOR (31:18 - 33:00 = 102s) ---
slides.append({
    'duration': 47.0,
    'badge': 'SESI 9: PENYAMBUTAN',
    'type': 'text',
    'title': 'PENYAMBUTAN DALAM KERENDAHAN HATI',
    'subtitle': 'Pernyataan Kasih Pengurus PERMATA GBKP Rg. Bogor',
    'content': 'WL:\n"Pembasuhan merupakan salah satu teladan yang dilakukan\nTuhan Yesus kepada murid-murid-Nya. Di sini kami Pengurus PERMATA,\nsiap membasuh kaki kamu sebagai bentuk penyambutan dan persahabatan\nkita di dalam PERMATA Bogor."',
    'audio_cue': 'Musik: Base Song Ambient • Narasi WL Penyambutan',
    'next_cue': 'Ajakan Berdiri & Doa Syukur (32:05)'
})
slides.append({
    'duration': 45.0,
    'badge': 'SESI 9: AJAKAN BERDIRI',
    'type': 'text',
    'title': 'PANGGILAN MENUJU POS PEMBASUHAN',
    'subtitle': 'Doa Syukur Menyambut Masa Muda dalam PERMATA',
    'content': '"Buat teman-teman yang akan dibasuh kakinya,\nsilakan berdiri di tempat yang sudah disediakan.\nMari sama-sama kita mengalami pemulihan dari Tuhan\ndan semoga lagu ini menjadi doa kita bersama..."\n\nSESI BASUH IRINGAN MUSIK WL:\n"Kami bersyukur Tuhan untuk menyambut adik-adik kami, teman-teman kami\nuntuk bersama-sama menikmati masa muda dalam PERMATA. Ini kami anak-anak Tuhan,\nkami butuh Engkau dan kiranya Tuhan berkenan untuk kami saling merangkul."',
    'audio_cue': 'Musik: Base Song Ambient • Peserta Mengambil Posisi',
    'next_cue': 'PUNCAK: Pembasuhan Kaki (33:00)'
})

alert_5 = {
    'song_title': 'PUNCAK BASUH KAKI: Lagu 5 - Sentuh Hatiku (Looped 16.5m)',
    'note': 'POS BASUH DIMULAI: Pengurus mulai membasuh kaki peserta'
}
for c in range(10, 0, -1):
    slides.append({
        'duration': 1.0,
        'badge': 'SESI 9: TRANSISI',
        'type': 'text',
        'title': 'PANGGILAN MENUJU POS PEMBASUHAN',
        'subtitle': 'Doa Syukur Menyambut Masa Muda dalam PERMATA',
        'content': '"Buat teman-teman yang akan dibasuh kakinya, silakan berdiri di tempat yang sudah disediakan..."\n\nSESI BASUH IRINGAN MUSIK WL:\n"Kami bersyukur Tuhan untuk menyambut adik-adik kami, teman-teman kami untuk bersama-sama menikmati masa muda dalam PERMATA. Ini kami anak-anak Tuhan, kami butuh Engkau dan kiranya Tuhan berkenan untuk kami saling merangkul."',
        'audio_cue': 'Base Song Memudar (Fade-out) -> Solo Piano Sentuh Hatiku Masuk',
        'next_cue': 'PUNCAK: Lagu 5 Sentuh Hatiku (33:00)',
        'alert': alert_5,
        'countdown': c
    })

# --- SEGMENT 10: PUNCAK - SENTUH HATIKU (33:00 - 49:25 = 985s) ---
loop_durations = [328.0, 328.0, 329.0]
for loop_idx, loop_total in enumerate(loop_durations):
    loop_num = loop_idx + 1
    badge_name = f'PUNCAK BASUH (PUTARAN {loop_num})'
    
    slides.append({
        'duration': 20.0,
        'badge': badge_name,
        'type': 'lyrics',
        'title': 'SENTUH HATIKU',
        'subtitle': f'Puncak Pembasuhan Kaki • Bagian {loop_num} dari 3',
        'content': '[ ALUNAN SOLO PIANO ]\n\n"Setiap basuhan air melambangkan penerimaan kami seutuhnya.\nDi dalam PERMATA Bogor, kamu tidak lagi berjalan sendirian."',
        'audio_cue': 'Musik: Solo Piano (Khidmat & Menyentuh Kalbu)',
        'next_cue': 'Verse 1'
    })
    slides.append({
        'duration': 65.0,
        'badge': badge_name,
        'type': 'lyrics',
        'title': 'SENTUH HATIKU',
        'subtitle': '[ VERSE 1 ]',
        'content': 'Betapa kumencintai\nSegala yang t\'lah terjadi\nTak pernah sendiri jalani hidup ini\nSelalu menyertai',
        'audio_cue': 'Musik: Solo Piano • Prosesi Basuh Kaki Berlangsung',
        'next_cue': 'Verse 2'
    })
    slides.append({
        'duration': 65.0,
        'badge': badge_name,
        'type': 'lyrics',
        'title': 'SENTUH HATIKU',
        'subtitle': '[ VERSE 2 ]',
        'content': 'Betapa kumenyadari\nDi dalam hidupku ini\nKau s\'lalu memberi rancangan terbaik\nOleh karena kasih',
        'audio_cue': 'Musik: Solo Piano • Pengurus Membasuh Kaki dengan Lembut',
        'next_cue': 'Chorus 1'
    })
    slides.append({
        'duration': 75.0,
        'badge': badge_name,
        'type': 'lyrics',
        'title': 'SENTUH HATIKU',
        'subtitle': '[ CHORUS 1 ]',
        'content': 'Bapa, sentuh hatiku\nUbah hidupku menjadi yang baru\nBagai emas yang murni\nKau membentuk bejana hatiku',
        'audio_cue': 'Musik: Solo Piano • Doa Pemulihan Hati',
        'next_cue': 'Chorus 2'
    })
    slides.append({
        'duration': 75.0,
        'badge': badge_name,
        'type': 'lyrics',
        'title': 'SENTUH HATIKU',
        'subtitle': '[ CHORUS 2 ]',
        'content': 'Bapa, ajarku mengerti\nSebuah kasih yang selalu memberi\nBagai air mengalir\nYang tiada pernah berhenti',
        'audio_cue': 'Musik: Solo Piano • Mengeringkan Kaki dengan Handuk Putih',
        'next_cue': 'Penghayatan Persaudaraan'
    })
    outro_dur = loop_total - (20.0 + 65.0 + 65.0 + 75.0 + 75.0)
    slides.append({
        'duration': outro_dur,
        'badge': badge_name,
        'type': 'lyrics',
        'title': 'SENTUH HATIKU',
        'subtitle': '[ KASIH PERSAUDARAAN KRISTUS ]',
        'content': '"Bagai air mengalir, yang tiada pernah berhenti..."\n\nDi PERMATA GBKP Runggun Bogor, kita saling menerima\ndalam kasih dan kerendahan hati.',
        'audio_cue': 'Musik: Solo Piano • Pos Pembasuhan Bergantian',
        'next_cue': 'Putaran Berikutnya' if loop_num < 3 else 'Doa Penutup (49:25)'
    })

# --- SEGMENT 11: DOA PENUTUP & PENGURAPAN (49:25 - 53:30 = 245s) ---
slides.append({
    'duration': 80.0,
    'badge': 'SESI 11: DOA PENUTUP',
    'type': 'text',
    'title': 'DOA PENUTUP & PENGURAPAN PERSAUDARAAN',
    'subtitle': 'Dipimpin oleh: Bang Nuel / BP PERMATA Rg. Bogor',
    'content': 'Tuhan Yesus yang baik, kami mengucap syukur untuk malam yang kudus ini.\nEngkau telah melawat setiap hati yang lelah dan membasuh kepenatan jiwa kami.\n\nKami serahkan setiap adik-adik kami dan pemuda-pemudi PERMATA Bogor ke dalam tangan-Mu.\nKiranya pengurapan Roh Kudus memenuhi kehidupan masa muda kami,\nagar kami hidup saling mengasihi, merangkul, dan saling menopang.',
    'audio_cue': 'Musik: Base Song Ambient • Doa Pengurapan Dipanjatkan',
    'next_cue': 'Pelukan Persaudaraan (50:45)'
})
slides.append({
    'duration': 80.0,
    'badge': 'SESI 11: PENEGUHAN',
    'type': 'text',
    'title': 'PENEGUHAN KELUARGA ALLAH',
    'subtitle': 'Saling Mengasihi & Merangkul di dalam PERMATA Bogor',
    'content': 'Pengurus memeluk dan menyalami setiap peserta yang telah dibasuh kakinya.\n\n"Selamat datang di rumah persekutuan PERMATA GBKP Runggun Bogor."\n"Kamu berharga, kamu dikasihi, dan kita adalah satu keluarga di dalam Kristus."',
    'audio_cue': 'Musik: Base Song Ambient • Pelukan Persaudaraan Hangat',
    'next_cue': 'Berkat & Pengutusan (52:05)'
})
slides.append({
    'duration': 75.0,
    'badge': 'SESI 11: BERKAT ALLAH',
    'type': 'scripture',
    'title': 'BERKAT & PENGUTUSAN MASA MUDA',
    'subtitle': 'Kitab Bilangan 6:24-26 (Terjemahan Baru LAI [Terverifikasi])',
    'content': '"TUHAN memberkati engkau dan melindungi engkau;\nTUHAN menyinari engkau dengan wajah-Nya\ndan memberi engkau kasih karunia;\nTUHAN menghadapkan wajah-Nya kepadamu\ndan memberi engkau damai sejahtera."',
    'audio_cue': 'Musik: Base Song Ambient • Menerima Berkat Tuhan',
    'next_cue': 'Lagu 6: Hari Ini Kurasa Bahagia (53:30)'
})

alert_6 = {
    'song_title': 'Lagu 6: Hari Ini Kurasa Bahagia (Sukacita Penutup)',
    'note': 'LAMPU DINYALAKAN TERANG! Bersiap bergandengan tangan penuh sukacita!'
}
for c in range(10, 0, -1):
    slides.append({
        'duration': 1.0,
        'badge': 'SESI 11: TRANSISI',
        'type': 'scripture',
        'title': 'BERKAT & PENGUTUSAN MASA MUDA',
        'subtitle': 'Kitab Bilangan 6:24-26',
        'content': '"TUHAN memberkati engkau dan melindungi engkau;\nTUHAN menyinari engkau dengan wajah-Nya dan memberi engkau kasih karunia;\nTUHAN menghadapkan wajah-Nya kepadamu dan memberi engkau damai sejahtera."',
        'audio_cue': 'Base Song Memudar Tuntas -> Lagu Sukacita Masuk',
        'next_cue': 'Lagu 6: Hari Ini Kurasa Bahagia (53:30)',
        'alert': alert_6,
        'countdown': c
    })

# --- SEGMENT 12: LAGU 6 - HARI INI KURASA BAHAGIA (53:30 - 56:34 = 184s) ---
slides.append({
    'duration': 15.0,
    'badge': 'SESI 12: LAGU 6',
    'type': 'lyrics',
    'title': 'HARI INI KURASA BAHAGIA',
    'subtitle': 'Sukacita Persekutuan Pemuda  •  Lampu Menyala Terang',
    'content': '[ INTRO MUSIK SUKACITA ]\n\nMari Bergandengan Tangan & Bernyanyi Bersama!',
    'audio_cue': 'Musik: Upbeat Karaoke Rohani • Sukacita Dimulai',
    'next_cue': 'Bait 1'
})
slides.append({
    'duration': 45.0,
    'badge': 'SESI 12: LAGU 6',
    'type': 'lyrics',
    'title': 'HARI INI KURASA BAHAGIA',
    'subtitle': '[ BAIT 1 ]',
    'content': 'Hari ini kurasa bahagia\nBerkumpul bersama saudara seiman\nTuhan Yesus mempersatukan kita\nTanpa memandang di antara kita',
    'audio_cue': 'Musik: Upbeat Karaoke • Jemaat Bernyanyi Bersama',
    'next_cue': 'Reff / Chorus'
})
slides.append({
    'duration': 50.0,
    'badge': 'SESI 12: LAGU 6',
    'type': 'lyrics',
    'title': 'HARI INI KURASA BAHAGIA',
    'subtitle': '[ REFF / CHORUS ]',
    'content': 'Bergandingan tangan dalam kasih\nDalam satu hati\nBerjalan dalam terang kasih Tuhan\n\nKau sahabatku, kau saudaraku\nTiada yang dapat memisahkan kita',
    'audio_cue': 'Musik: Upbeat Karaoke • Bergandengan Tangan',
    'next_cue': 'Reff Pengulangan & Pelukan'
})
slides.append({
    'duration': 50.0,
    'badge': 'SESI 12: LAGU 6',
    'type': 'lyrics',
    'title': 'HARI INI KURASA BAHAGIA',
    'subtitle': '[ SUKACITA BERSAMA ]',
    'content': 'Kau sahabatku, kau saudaraku\nTiada yang dapat memisahkan kita\n\nBergandingan tangan dalam kasih...\nTiada yang dapat memisahkan kita!',
    'audio_cue': 'Musik: Upbeat Karaoke • Sorak Sukacita & Pelukan',
    'next_cue': 'Outro Sukacita (56:10)'
})
slides.append({
    'duration': 24.0,
    'badge': 'SESI 12: LAGU 6',
    'type': 'lyrics',
    'title': 'HARI INI KURASA BAHAGIA',
    'subtitle': '[ OUTRO SUKACITA ]',
    'content': '"Tiada yang dapat memisahkan kita!"\n\n[ Sorak Sukacita & Tepuk Tangan Bersama! Haleluya! ]',
    'audio_cue': 'Musik: Outro Sukacita',
    'next_cue': 'Penutup (56:34)'
})

# --- SEGMENT 13: PENUTUP (56:34 - 56:44.04 = 10.04s) ---
slides.append({
    'duration': 10.04,
    'badge': 'PENUTUP',
    'type': 'text',
    'title': 'IBADAH PEMBASUHAN KAKI TELAH SELESAI',
    'subtitle': 'Masa Pengakrabian (MAPER) PERMATA GBKP Runggun Bogor 2026',
    'content': 'Selamat Berproses dan Bertumbuh Bersama!\n\n"Ersada Arih Man Dibata, Si Sampat-sampaten Ibas Kekelengen"\n\nTUHAN YESUS MEMBERKATI KITA SEMUA',
    'audio_cue': 'Musik: Selesai',
    'next_cue': 'Selesai'
})

print(f"Total defined slides/frames: {len(slides)}")
total_dur = sum(s['duration'] for s in slides)
print(f"Total Duration: {total_dur:.2f}s ({format_time(total_dur)})")

# Render all slides to PNG
print("Rendering slide PNG images...")
t_render_start = time.time()
concat_entries = []
curr_time = 0.0
for idx, s in enumerate(slides):
    img_filename = f"slide_{idx:03d}.png"
    img_filepath = os.path.join(slides_dir, img_filename)
    alert_info = s.get('alert', None)
    countdown_val = s.get('countdown', None)
    slide_img = render_slide(s, curr_time, countdown_val, alert_info)
    slide_img.save(img_filepath, "PNG")
    concat_entries.append((img_filename, s['duration']))
    curr_time += s['duration']

print(f"Rendered {len(slides)} slides in {time.time() - t_render_start:.2f}s!")

# Write ffconcat script
concat_file = os.path.join(slides_dir, "concat_slides.txt")
with open(concat_file, 'w', encoding='utf-8') as f:
    f.write("ffconcat version 1.0\n")
    for img_name, dur in concat_entries:
        f.write(f"file '{img_name}'\n")
        f.write(f"duration {dur:.3f}\n")
    f.write(f"file '{concat_entries[-1][0]}'\n")

print(f"Concat script created: {concat_file}")
