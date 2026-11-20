# -*- coding: utf-8 -*-
import os
import sys
import socket
from flask import Flask, send_file, render_template_string, jsonify, Response

app = Flask(__name__)

AUDIO_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_SONG_FILE = os.path.join(AUDIO_DIR, "Basesong_leave it in God's hands tonight.mp3")
VIDEO_DIR = os.path.join(AUDIO_DIR, "Video_MP4")
PDF_FILE = os.path.join(AUDIO_DIR, "Buku_Lirik_Lagu_Pembasuhan_MAPER_Bogor.pdf")

def get_all_ips():
    ips = []
    for info in socket.getaddrinfo(socket.gethostname(), None):
        ip = info[4][0]
        if '.' in ip and not ip.startswith('127.') and not ip.startswith('169.254.'):
            if ip not in ips:
                ips.append(ip)
    return ips

def get_video_path(song_num):
    if not os.path.exists(VIDEO_DIR):
        return None
    for f in os.listdir(VIDEO_DIR):
        if f.startswith(f"{song_num}."):
            return os.path.join(VIDEO_DIR, f)
    return None

HTML_PAGE = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Smart Operator &amp; Video Companion - Pembasuhan MAPER PERMATA Bogor</title>
  <style>
    :root {
      --bg: #0b1120;
      --card-bg: #1e293b;
      --card-active: #172554;
      --border: #334155;
      --gold: #f59e0b;
      --gold-light: #fef3c7;
      --cyan: #38bdf8;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --green: #22c55e;
      --rose: #fb7185;
      --purple: #c084fc;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      padding-bottom: 110px; /* space for persistent bottom bar */
    }

    /* Top Sticky Header */
    .top-bar {
      position: sticky;
      top: 0;
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      padding: 10px 16px;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .top-title {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--gold);
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .top-sub {
      font-size: 11px;
      color: var(--text-muted);
    }
    .status-badge {
      font-size: 10.5px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 20px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.3s;
    }
    .badge-ambient {
      background: rgba(34, 197, 94, 0.15);
      border: 1px solid var(--green);
      color: #86efac;
    }
    .badge-video {
      background: rgba(239, 68, 68, 0.2);
      border: 1px solid #ef4444;
      color: #fca5a5;
    }
    .badge-paused {
      background: rgba(148, 163, 184, 0.15);
      border: 1px solid #64748b;
      color: #cbd5e1;
    }
    .pulse-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: currentColor;
      animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
      0% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.3; transform: scale(0.8); }
      100% { opacity: 1; transform: scale(1); }
    }

    /* Filter Bar */
    .filter-bar {
      padding: 10px 14px;
      background: #111827;
      display: flex;
      gap: 8px;
      overflow-x: auto;
      border-bottom: 1px solid #1f2937;
      position: sticky;
      top: 51px;
      z-index: 95;
    }
    .filter-pill {
      background: #1f2937;
      border: 1px solid var(--border);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 16px;
      white-space: nowrap;
      cursor: pointer;
    }
    .filter-pill.active {
      background: var(--gold);
      color: #000000;
      border-color: var(--gold);
    }

    /* Rundown Container */
    .container {
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-width: 820px;
      margin: 0 auto;
      width: 100%;
    }

    /* Section Card */
    .section-card {
      background: var(--card-bg);
      border: 1.5px solid var(--border);
      border-radius: 12px;
      padding: 14px 16px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
      transition: all 0.3s;
    }
    .section-card.active-session {
      border-color: var(--gold);
      background: var(--card-active);
      box-shadow: 0 0 16px rgba(245, 158, 11, 0.25);
    }
    .section-card.song-session {
      border-left: 5px solid var(--cyan);
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 8px;
    }
    .time-badge {
      font-size: 11px;
      font-weight: 800;
      color: var(--gold);
      background: rgba(245, 158, 11, 0.15);
      padding: 2.5px 8px;
      border-radius: 12px;
      display: inline-block;
      margin-bottom: 4px;
    }
    .session-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.3;
    }
    .session-type-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 8px;
      white-space: nowrap;
    }
    .type-speech {
      background: rgba(245, 158, 11, 0.15);
      color: var(--gold);
      border: 1px solid var(--gold);
    }
    .type-song {
      background: rgba(56, 189, 248, 0.15);
      color: var(--cyan);
      border: 1px solid var(--cyan);
    }

    /* Boxes */
    .box {
      border-radius: 8px;
      padding: 12px 14px;
      margin-top: 10px;
      font-size: 13.5px;
      line-height: 1.5;
    }
    .speech-box {
      background: rgba(245, 158, 11, 0.08);
      border-left: 4px solid var(--gold);
      color: #fef08a;
    }
    .speech-title {
      font-size: 12px;
      font-weight: 800;
      color: var(--gold);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 5px;
    }
    .speech-text {
      white-space: pre-line;
      line-height: 1.55;
    }

    .scripture-box {
      background: rgba(251, 113, 133, 0.08);
      border-left: 4px solid var(--rose);
      color: #ffe4e6;
    }
    .scripture-title {
      font-size: 12px;
      font-weight: 800;
      color: var(--rose);
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .scripture-text {
      font-style: italic;
      line-height: 1.45;
    }

    .cue-box {
      background: rgba(34, 197, 94, 0.08);
      border-left: 4px solid var(--green);
      color: #dcfce7;
      font-size: 12.5px;
    }
    .cue-title {
      font-size: 11.5px;
      font-weight: 800;
      color: var(--green);
      text-transform: uppercase;
      margin-bottom: 3px;
    }

    .lyrics-box {
      background: rgba(56, 189, 248, 0.06);
      border-left: 4px solid var(--cyan);
      color: #e0f2fe;
    }
    .lyrics-title {
      font-size: 12px;
      font-weight: 800;
      color: var(--cyan);
      text-transform: uppercase;
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
    }
    .lyrics-text {
      font-weight: 600;
      color: #f0f9ff;
      white-space: pre-line;
      line-height: 1.5;
    }

    /* Video Player Component */
    .video-card {
      background: #020617;
      border: 1.5px solid #38bdf8;
      border-radius: 10px;
      overflow: hidden;
      margin-top: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }
    .video-card-header {
      padding: 8px 12px;
      background: #0f172a;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
    }
    .video-card-title {
      font-size: 12px;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .video-card-badge {
      background: #0284c7;
      color: #ffffff;
      font-size: 9.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
    }
    .song-video {
      width: 100%;
      max-height: 270px;
      display: block;
      background: #000000;
      outline: none;
    }

    /* Big Action Button for Song Video */
    .play-video-cta {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      padding: 12px 18px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      margin-top: 10px;
      width: 100%;
      box-shadow: 0 4px 10px rgba(37, 99, 235, 0.35);
      transition: all 0.2s;
    }
    .play-video-cta:active {
      transform: scale(0.98);
      background: #1d4ed8;
    }

    .next-session-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 9px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      margin-top: 12px;
      width: 100%;
    }
    .next-session-btn:hover, .next-session-btn:active {
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
    }

    /* Persistent Bottom Control Bar */
    .bottom-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(15, 23, 42, 0.98);
      backdrop-filter: blur(12px);
      border-top: 1.5px solid var(--border);
      padding: 10px 16px;
      z-index: 100;
      display: flex;
      flex-direction: column;
      gap: 8px;
      max-width: 860px;
      margin: 0 auto;
    }
    .bottom-row-1 {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .bottom-status-text {
      font-size: 12px;
      font-weight: 700;
      color: #e2e8f0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      max-width: 230px;
    }
    .base-btn {
      background: var(--green);
      color: #000000;
      border: none;
      font-size: 12px;
      font-weight: 800;
      padding: 7px 14px;
      border-radius: 20px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      white-space: nowrap;
    }
    .base-btn.playing {
      background: #eab308;
      color: #000000;
    }
    .volume-container {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      color: var(--text-muted);
    }
    .volume-slider {
      flex: 1;
      accent-color: var(--gold);
      height: 4px;
    }
  </style>
</head>
<body>

  <!-- Audio Element for Continuous Base Song -->
  <audio id="base-audio" loop preload="auto" src="/base-song"></audio>

  <!-- Top Sticky Header -->
  <div class="top-bar">
    <div>
      <div class="top-title">PERMATA GBKP RG. BOGOR</div>
      <div class="top-sub">IBADAH PEMBASUHAN KAKI (MAPER 60 MENIT)</div>
    </div>
    <div id="status-badge" class="status-badge badge-paused">
      <div class="pulse-dot"></div>
      <span id="badge-text">STANDBY</span>
    </div>
  </div>

  <!-- Filter Bar -->
  <div class="filter-bar">
    <div class="filter-pill active" onclick="setFilter('all', this)">Semua Sesi (12)</div>
    <div class="filter-pill" onclick="setFilter('songs', this)">🎬 6 Video Lagu</div>
    <div class="filter-pill" onclick="setFilter('speeches', this)">🎙️ Naskah WL</div>
    <div class="filter-pill" onclick="setFilter('scriptures', this)">📖 Ayat Alkitab</div>
    <a href="/download-guide" class="filter-pill" style="background:#1d4ed8; color:#ffffff; border-color:#3b82f6; text-decoration:none; font-weight:700;">📘 Unduh Panduan Pengurus (PDF 6 Hal)</a>
    <a href="/download-pdf" class="filter-pill" style="background:#047857; color:#ffffff; border-color:#10b981; text-decoration:none; font-weight:700;">🎵 Unduh Lirik Lagu (PDF 3 Hal)</a>
  </div>

  <!-- Rundown Container -->
  <div class="container" id="rundown-container">

    <!-- SESI 1: 00:00 - 03:30 (PEMBUKAAN & PERSIAPAN DIRI) -->
    <div class="section-card active-session" id="session-1">
      <div class="section-header">
        <div>
          <span class="time-badge">00:00 - 03:30 (3.5 Menit Hening &amp; Santai)</span>
          <div class="session-title">Sesi 1: Pengantar WL &amp; Menyiapkan Hati</div>
        </div>
        <span class="session-type-badge type-speech">🎙️ Pengantar WL</span>
      </div>

      <div class="box cue-box">
        <div class="cue-title">💡 Petunjuk Operator, Lighting &amp; Fasilitator</div>
        • <strong>Suasana:</strong> Santai, tenang, dan redup. Base Song Ambient mengalun lembut.<br>
        • <strong>Aksi:</strong> Peserta duduk rileks, gadget disimpan, semua hening/diam. Kakak-abang mendekat dan merangkul pundak adik-adiknya dengan hangat.
      </div>

      <div class="box speech-box">
        <div class="speech-title">🎙️ Kata-Kata yang Dikeluarkan WL (Lebih Santai &amp; Singkat)</div>
        <div class="speech-text">"Syalom PERMATA! Gimana makannya hari ini? Enak ya?
Yuk, sekarang kita ambil posisi duduk yang paling santai dan paling nyaman... Letakkan tas di samping, dan simpan dulu handphone atau gadget kita masing-masing.

Mari sejenak kita semua diam... Tarik napas panjang, tenangkan pikiran dari segala keramaian dan kesibukan di luar sana. Di sini, kita tidak perlu berpura-pura tegar atau memakai topeng. Biarkan hati kita benar-benar hening di hadapan Tuhan.

[KAKAK-ABANG MERANGKUL PUNDAK ADIK-ADIKNYA]

Di tengah rasa lelah dan kekeringan yang mungkin kita rasakan, mari buka hati kita... Rasakan betapa jiwa kita merindukan jamahan dan pelukan Tuhan yang memulihkan. Mari bersama-sama kita menyembah Dia."</div>
      </div>

      <button class="next-session-btn" onclick="scrollToSession(2)">
        <span>Siap Bernyanyi &rarr; Lanjut ke Lagu 1</span>
      </button>
    </div>

    <!-- SESI 2: LAGU 1 (SEPERTI RUSA) -->
    <div class="section-card song-session" id="session-2">
      <div class="section-header">
        <div>
          <span class="time-badge">03:30 - 08:00 (Durasi: 4.5 Menit)</span>
          <div class="session-title">Sesi 2: Lagu 1 — Seperti Rusa yang Rindu Sungai-Mu</div>
        </div>
        <span class="session-type-badge type-song">🎵 Video Lagu 1</span>
      </div>

      <!-- VIDEO PLAYER -->
      <div class="video-card">
        <div class="video-card-header">
          <div class="video-card-title">
            <span>🎬 Video Karaoke &amp; Lirik YouTube (Michael Tjanaka)</span>
          </div>
          <span class="video-card-badge">Do = D • 1080p</span>
        </div>
        <video id="video-1" controls playsinline preload="metadata" class="song-video" src="/video/1"></video>
      </div>

      <button class="play-video-cta" onclick="playSongVideo(1)">
        <span>▶ PUTAR VIDEO &amp; MULAI NYANYI (Base Song Auto-Fade Out)</span>
      </button>

      <div class="box lyrics-box">
        <div class="lyrics-title">
          <span>🎵 Teks Lirik Lagu</span>
          <span style="color:var(--gold);">Do = D</span>
        </div>
        <div class="lyrics-text"><strong>[Bait 1]</strong>
S'perti rusa rindu sungai-Mu
Jiwaku rindu Engkau
Kaulah Tuhan hasrat hatiku
Kurindu menyembah-Mu

<strong>[Bait 2]</strong>
Engkau kekuatan dan perisaiku
Kepada-Mu rohku berserah
Kaulah Tuhan hasrat hatiku
Kurindu menyembah-Mu

<strong>[Chorus / Reff]</strong>
Yesus, Yesus, Kau berarti bagiku
Yesus, Yesus, Kau segalanya bagiku</div>
      </div>

      <button class="next-session-btn" onclick="stopVideoAndAdvance(1, 3)">
        <span>Selesai Nyanyi &rarr; Lanjut ke Sesi 3 (Refleksi Diri)</span>
      </button>
    </div>

    <!-- SESI 3: 08:00 - 10:00 -->
    <div class="section-card" id="session-3">
      <div class="section-header">
        <div>
          <span class="time-badge">08:00 - 10:00 (Durasi: 2 Menit)</span>
          <div class="session-title">Sesi 3: Refleksi Kerapuhan Diri &amp; Pengakuan Dosa</div>
        </div>
        <span class="session-type-badge type-speech">🎙️ Refleksi WL</span>
      </div>

      <div class="box cue-box">
        <div class="cue-title">💡 Petunjuk Operator &amp; Fasilitator</div>
        • <strong>Musik:</strong> Base Song Ambient mengalun lembut menjembatani refleksi.<br>
        • <strong>Fasilitator:</strong> Merangkul peserta, alirkan rasa aman sejati tanpa penghakiman.
      </div>

      <div class="box speech-box">
        <div class="speech-title">🎙️ Kata-Kata yang Dikeluarkan WL (Naskah Lengkap)</div>
        <div class="speech-text">"Teman-teman sekalian, jika kita ada di tempat ini hari ini, tidak ada yang kebetulan. Ada maksud dan rancangan kekal Tuhan di balik keberadaan kita. Di masa muda ini, di balik senyuman kita, seringkali ada kepahitan yang kita telan sendiri, luka masa kecil, kekecewaan mendalam, dan rasa hampa yang membayangi.

Banyak hal dalam hidup mungkin tidak kita pahami, tetapi satu hal yang pasti: langkah kaki kecil kita tidak pernah sedetik pun hilang dari pandangan kasih Tuhan. Namun mari kita jujur di hadapan Bapa yang Mahatahu... berapa sering kaki kita justru melangkah menjauhi-Nya? Berapa sering keegoisan, amarah terpendam, kesombongan, dan dosa mengotori kekudusan hidup kita? Kita merasa bersalah, merasa kotor, dan merasa tidak layak lagi datang kepada-Nya...

Dengarlah panggilan Bapa... Siapa di antara kita yang tidak pernah melakukan dosa? Kita semua pernah tersandung, pernah melanggar perintah Tuhan, dan pernah melukai orang lain. Tetapi bersyukurlah, Tuhan kita bukanlah Allah yang suka menghakimi, mempermalukan, atau mengungkit masa lalu kita! Di atas kayu salib Golgota, kasih dan darah-Nya telah tercurah untuk membasuh segala cela kita. Di hadapan salib, tidak ada dosa yang terlalu hitam yang tak sanggup diputihkan oleh anugerah-Nya. Jangan takut, jangan bersembunyi lagi... datanglah pada pelukan-Nya saat ini."</div>
      </div>

      <div class="box scripture-box">
        <div class="scripture-title">📖 Ayat Alkitab (TB LAI Terverifikasi)</div>
        <div class="scripture-text"><strong>Yesaya 1:18</strong> — "Marilah, baiklah kita beperkara! — firman TUHAN — Sekalipun dosamu merah seperti kirmizi, akan menjadi putih seperti salju; sekalipun berwarna merah seperti kain kesumba, akan menjadi putih seperti bulu domba."</div>
      </div>

      <button class="next-session-btn" onclick="scrollToSession(4)">
        <span>Siap Bernyanyi &rarr; Lanjut ke Lagu 2 (Sejauh Timur Dari Barat)</span>
      </button>
    </div>

    <!-- SESI 4: LAGU 2 (SEJAUH TIMUR DARI BARAT) -->
    <div class="section-card song-session" id="session-4">
      <div class="section-header">
        <div>
          <span class="time-badge">10:00 - 15:35 (Durasi: 5.5 Menit)</span>
          <div class="session-title">Sesi 4: Lagu 2 — Sejauh Timur Dari Barat</div>
        </div>
        <span class="session-type-badge type-song">🎵 Video Lagu 2</span>
      </div>

      <div class="video-card">
        <div class="video-card-header">
          <div class="video-card-title">
            <span>🎬 Video Karaoke &amp; Lirik YouTube (Maria Shandi)</span>
          </div>
          <span class="video-card-badge">Do = C / D • 1080p</span>
        </div>
        <video id="video-2" controls playsinline preload="metadata" class="song-video" src="/video/2"></video>
      </div>

      <button class="play-video-cta" onclick="playSongVideo(2)">
        <span>▶ PUTAR VIDEO &amp; MULAI NYANYI (Base Song Auto-Fade Out)</span>
      </button>

      <div class="box lyrics-box">
        <div class="lyrics-title">
          <span>🎵 Teks Lirik Lagu</span>
          <span style="color:var(--gold);">Do = C / D</span>
        </div>
        <div class="lyrics-text"><strong>[Bait 1]</strong>
Sejauh timur dari barat
Engkau membuang dosaku
Tiada Kau ingat lagi pelanggaranku

<strong>[Bait 2]</strong>
Jauh ke dalam tubir laut
Kau melemparkan dosaku
Tiada Kau perhitungkan kesalahanku

<strong>[Reff / Chorus]</strong>
Betapa besar kasih pengampunan-Mu Tuhan
Tak Kau pandang hina hati yang hancur
Ku berterima kasih kepada-Mu ya Tuhan
Pengampunan yang Kau beri pulihkanku</div>
      </div>

      <button class="next-session-btn" onclick="stopVideoAndAdvance(2, 5)">
        <span>Selesai Nyanyi &rarr; Lanjut ke Sesi 5 (Hening 2 Menit Tangan di Dada)</span>
      </button>
    </div>

    <!-- SESI 5: 15:35 - 20:00 -->
    <div class="section-card" id="session-5">
      <div class="section-header">
        <div>
          <span class="time-badge">15:35 - 20:00 (Durasi: 4.5 Menit)</span>
          <div class="session-title">Sesi 5: Tangan di Dada &amp; Hening Doa Pribadi (2 Menit)</div>
        </div>
        <span class="session-type-badge type-speech">🎙️ Hening Doa Pribadi</span>
      </div>

      <div class="box cue-box">
        <div class="cue-title">💡 Petunjuk Operator &amp; WL (MOMEN SANGAT KHIDMAT)</div>
        • <strong>Musik:</strong> Base Song Ambient mengalun tipis. Ruangan hening total.<br>
        • <strong>Instruksi Fisik:</strong> WL mengajak peserta meletakkan tangan kanan di dada kiri.<br>
        • <strong>Waktu Hening:</strong> Beri jeda 2 menit penuh tanpa kata-kata agar peserta mencurahkan isi hatinya secara pribadi kepada Tuhan.
      </div>

      <div class="box speech-box">
        <div class="speech-title">🎙️ Kata-Kata yang Dikeluarkan WL (Naskah Lengkap)</div>
        <div class="speech-text">"Saat ini, mari kita semua menundukkan kepala... Boleh perlahan letakkan tangan kananmu di dadamu masing-masing. Rasakan detak jantungmu. Di balik dadamu yang berdetak ini, ada hati yang mungkin sedang sangat lelah, ada luka yang tak pernah kau ceritakan pada siapapun, ada penyesalan dan kesalahan masa lalu yang kau simpan sendiri.

Rasakan nafas hidup yang masih Tuhan berikan. Tanggalkan segala topeng dan gengsimu, bicaralah kepada Tuhan dalam lubuk hatimu yang terdalam... Dia mendengarkan setiap detak hatimu.

[HENINGKAN HATI SELAMA 2 MENIT — HANYA ALUNAN AMBIENT BASE SONG]

Tuhan berfirman dalam 1 Yohanes 1:9: <em>'Jika kita mengaku dosa kita, maka Ia adalah setia dan adil, sehingga Ia akan mengampuni segala dosa kita dan menyucikan kita dari segala kejahatan.'</em> Dan rancangan-Nya bukanlah rancangan kecelakaan, melainkan damai sejahtera untuk hari depan yang penuh harapan. Mari bawa seluruh bebanmu sujud di hadapan altar-Nya."</div>
      </div>

      <div class="box scripture-box">
        <div class="scripture-title">📖 Ayat Alkitab (TB LAI Terverifikasi)</div>
        <div class="scripture-text"><strong>1 Yohanes 1:9</strong> — "Jika kita mengaku dosa kita, maka Ia adalah setia dan adil, sehingga Ia akan mengampuni segala dosa kita dan menyucikan kita dari segala kejahatan."<br><br>
<strong>Yeremia 29:11</strong> — "Sebab Aku ini mengetahui rancangan-rancangan apa yang ada pada-Ku mengenai kamu, demikianlah firman TUHAN, yaitu rancangan damai sejahtera dan bukan rancangan kecelakaan, untuk memberikan kepadamu hari depan yang penuh harapan."</div>
      </div>

      <button class="next-session-btn" onclick="scrollToSession(6)">
        <span>Siap Bernyanyi &rarr; Lanjut ke Lagu 3 (Sujud Di Altar-Nya)</span>
      </button>
    </div>

    <!-- SESI 6: LAGU 3 (SUJUD DI ALTAR-NYA) -->
    <div class="section-card song-session" id="session-6">
      <div class="section-header">
        <div>
          <span class="time-badge">20:00 - 25:35 (Durasi: 5.5 Menit)</span>
          <div class="session-title">Sesi 6: Lagu 3 — Sujud Di Altar-Nya</div>
        </div>
        <span class="session-type-badge type-song">🎵 Video Lagu 3</span>
      </div>

      <div class="video-card">
        <div class="video-card-header">
          <div class="video-card-title">
            <span>🎬 Video Karaoke &amp; Lirik YouTube (Sujud di Altar-Nya)</span>
          </div>
          <span class="video-card-badge">Do = D / E • 1080p</span>
        </div>
        <video id="video-3" controls playsinline preload="metadata" class="song-video" src="/video/3"></video>
      </div>

      <button class="play-video-cta" onclick="playSongVideo(3)">
        <span>▶ PUTAR VIDEO &amp; MULAI NYANYI (Base Song Auto-Fade Out)</span>
      </button>

      <div class="box lyrics-box">
        <div class="lyrics-title">
          <span>🎵 Teks Lirik Lagu</span>
          <span style="color:var(--gold);">Do = D / E</span>
        </div>
        <div class="lyrics-text"><strong>[Bait 1]</strong>
Bila hati terasa berat
Tak seorang pun mengerti bebanku
Kutanya Yesus: apa yang harus kubuat?
Dia berfirman mari datanglah
Dia selalu pedulikan aku
Kudatang Yesus: Dia pikul segala bebanku

<strong>[Reff / Chorus]</strong>
Sujud di altar-Nya, kubawa hidupku
Kuterima anugerah-Nya
Dia ampuniku dan bebaskanku
Dia ubah hidupku, baharui hatiku
Sesuatu terjadi saat datang di altar-Nya

<strong>[Kemenangan &amp; Pemulihan]</strong>
Pemulihan terjadi
Mukjizat terjadi
Kemenangan terjadi
Saat datang di altar-Nya!</div>
      </div>

      <button class="next-session-btn" onclick="stopVideoAndAdvance(3, 7)">
        <span>Selesai Nyanyi &rarr; Lanjut ke Sesi 7 (Prosesi Kendi Air)</span>
      </button>
    </div>

    <!-- SESI 7: 25:35 - 28:30 -->
    <div class="section-card" id="session-7">
      <div class="section-header">
        <div>
          <span class="time-badge">25:35 - 28:30 (Durasi: 3 Menit)</span>
          <div class="session-title">Sesi 7: Kedatangan Kendi Air &amp; Firman Filipi 2</div>
        </div>
        <span class="session-type-badge type-speech">🎙️ Prosesi Kendi Air</span>
      </div>

      <div class="box cue-box">
        <div class="cue-title">💡 HIGHLIGHT UTAMA: SOUND OF WATER &amp; LIGHTING</div>
        • <strong>Lighting:</strong> Lampu ruangan diredupkan perlahan (warm ambient). Sorotan lembut tertuju ke kendi &amp; salib.<br>
        • <strong>Prosesi:</strong> Pengurus berjalan khidmat membawa kendi air bersih, baskom, dan handuk putih.<br>
        • <strong>SUARA AIR (5-7 Detik):</strong> Air dituangkan perlahan dari kendi ke baskom. Suara gemericik air meditatif memenuhi ruangan.
      </div>

      <div class="box speech-box">
        <div class="speech-title">🎙️ Kata-Kata yang Dikeluarkan WL (Naskah Lengkap)</div>
        <div class="speech-text">(Biarkan suara gemericik air terdengar 5-7 detik dalam keheningan total...)

"Dengarkanlah... suara gemericik air yang mengalir itu...
Dua ribu tahun yang lalu, di sebuah ruang atas di Yerusalem, sebelum kayu salib ditegakkan, Yesus – Tuhan semesta alam – melakukan hal yang meruntuhkan keangkuhan dunia. Dia melepaskan jubah kemuliaan-Nya. Dia mengambil sehelai kain lenan, mengikatkannya di pinggang-Nya, dan menuangkan air bersih ke dalam baskom.
Raja segala raja itu berlutut di tanah berdebu, tepat di bawah telapak kaki murid-murid-Nya. Kaki yang kotor oleh debu perjalanan, kaki yang lelah, kaki yang kerap kali salah melangkah. Yesus membasuh kaki mereka satu per satu dengan tangan penuh kasih, lalu menyekanya dengan kain lenan-Nya.
Saat Petrus menolak karena merasa tidak layak, Yesus memandangnya dan berkata: <em>'Jikalau Aku tidak membasuh engkau, engkau tidak mendapat bagian dalam-Ku.'</em>

Air yang ada di hadapan kita hari ini adalah simbol kerendahan hati dan kasih pemulihan Kristus. Kami pengurus dan kakak-abangmu di PERMATA Bogor bukanlah orang-orang yang tanpa cela. Kami pun orang berdosa yang telah ditebus oleh anugerah. Tetapi hari ini, dengan hati seorang hamba, kami rindu menanggalkan keangkuhan kami untuk melayani kalian. Kami rindu membasuh kakimu, sebagai tanda bahwa engkau diterima seutuhnya dalam pelukan persaudaraan PERMATA Bogor."</div>
      </div>

      <div class="box scripture-box">
        <div class="scripture-title">📖 Detail Ayat Alkitab (TB LAI Terverifikasi)</div>
        <div class="scripture-text"><strong>Yohanes 13:14-15</strong> — "Jadi jikalau Aku membasuh kakimu, Aku yang adalah Tuhan dan Guru, maka kamupun wajib saling membasuh kaki; sebab Aku telah memberikan suatu teladan kepada kamu, supaya kamu juga berbuat sama seperti yang telah Kuperbuat kepadamu."<br><br>
<strong>Filipi 2:5,7</strong> — "Hendaklah kamu dalam hidupmu bersama, menaruh pikiran dan perasaan yang terdapat juga dalam Kristus Yesus... melainkan telah mengosongkan diri-Nya sendiri, dan mengambil rupa seorang hamba, dan menjadi sama dengan manusia."</div>
      </div>

      <button class="next-session-btn" onclick="scrollToSession(8)">
        <span>Siap Bernyanyi &rarr; Lanjut ke Lagu 4 (Hati Sebagai Hamba)</span>
      </button>
    </div>

    <!-- SESI 8: LAGU 4 (HATI SEBAGAI HAMBA) -->
    <div class="section-card song-session" id="session-8">
      <div class="section-header">
        <div>
          <span class="time-badge">28:30 - 33:18 (Durasi: 4.8 Menit)</span>
          <div class="session-title">Sesi 8: Lagu 4 — Hati Sebagai Hamba</div>
        </div>
        <span class="session-type-badge type-song">🎵 Video Lagu 4</span>
      </div>

      <div class="video-card">
        <div class="video-card-header">
          <div class="video-card-title">
            <span>🎬 Video Karaoke &amp; Lirik YouTube (Nikita)</span>
          </div>
          <span class="video-card-badge">Do = C / D • 1080p</span>
        </div>
        <video id="video-4" controls playsinline preload="metadata" class="song-video" src="/video/4"></video>
      </div>

      <button class="play-video-cta" onclick="playSongVideo(4)">
        <span>▶ PUTAR VIDEO &amp; MULAI NYANYI (Base Song Auto-Fade Out)</span>
      </button>

      <div class="box lyrics-box">
        <div class="lyrics-title">
          <span>🎵 Teks Lirik Lagu (Dinyanyikan Khusus Pengurus)</span>
          <span style="color:var(--gold);">Do = C / D</span>
        </div>
        <div class="lyrics-text"><strong>[Verse - Dinyanyikan Khusus Pengurus Bersimpuh]</strong>
Ku tak membawa apapun juga
Saat ku datang ke dunia
Ku tinggal semua pada akhirnya
Saat ku kembali ke surga

<strong>[Chorus]</strong>
Inilah yang kupunya: hati s'bagai hamba
Yang mau taat dan setia pada-Mu Bapa
Kemanapun kubawa hati yang menyembah
Dalam Roh dan kebenaran sampai s'lamanya

<strong>[Bridge]</strong>
Bagaimana ku membalas kasih-Mu?
S'gala yang kupunya itu milik-Mu
Itu milik-Mu oh...</div>
      </div>

      <button class="next-session-btn" onclick="stopVideoAndAdvance(4, 9)">
        <span>Selesai Nyanyi &rarr; Lanjut ke Sesi 9 (Penyambutan PERMATA Bogor)</span>
      </button>
    </div>

    <!-- SESI 9: 33:18 - 35:00 -->
    <div class="section-card" id="session-9">
      <div class="section-header">
        <div>
          <span class="time-badge">33:18 - 35:00 (Durasi: 1.7 Menit)</span>
          <div class="session-title">Sesi 9: Penyambutan Kerendahan Hati PERMATA Bogor</div>
        </div>
        <span class="session-type-badge type-speech">🎙️ Ajakan Basuh Kaki</span>
      </div>

      <div class="box cue-box">
        <div class="cue-title">💡 Petunjuk Operator, Posisi Duduk &amp; Pengurus</div>
        • <strong>Posisi Duduk:</strong> Adik-adik yang akan dibasuh kakinya dipersilakan duduk dengan tenang di kursi pembasuhan.<br>
        • <strong>Pengurus:</strong> Seluruh pengurus PERMATA dan kakak-abang mengambil posisi berada di depan adik-adik/teman-teman PERMATA.<br>
        • <strong>Musik:</strong> Base Song mengalir lembut mengiringi ajakan berlutut melayani.
      </div>

      <div class="box speech-box">
        <div class="speech-title">🎙️ Kata-Kata yang Dikeluarkan WL (Ajakan Pembasuhan &amp; Penyambutan Kasih)</div>
        <div class="speech-text">"Teman-teman sekalian, pembasuhan ini merupakan salah satu teladan yang dilakukan oleh Tuhan kita Yesus Kristus kepada para murid yang terkasih...

Di sini, kami pengurus PERMATA — kami segenap keluarga PERMATA — akan melakukan pembasuhan kaki dari tiap-tiap di antara kamu, sebagai bentuk kami menyambut rasa kasih yang begitu besar dan juga menjalin persahabatan yang erat di dalam wadah PERMATA Bogor.

Kiranya teman-teman yang nantinya dibasuh kakinya akan terus berdiri teguh bersama dengan Tuhan, dan berdiri bersama kami. Mari sama-sama kita mengalami pemulihan sejati dari Tuhan. Semoga dengan apa yang sudah teman-teman doakan tadi sebelumnya, dan juga lewat pembasuhan kaki ini, kita bisa merasakan betapa teramat besarnya kasih Tuhan terhadap kita, bagaimana Dia mengampuni dan menerima kita apa adanya.

Oleh sebab itu, mari dari antara kita, adik-adik kami yang akan dibasuh kakinya untuk bisa duduk, dan seluruh setiap dari pengurus PERMATA silakan mengambil tempat berada di depan adik-adik atau teman-teman PERMATA lainnya."

[SAAT PEMBASUHAN BERJALAN DENGAN IRINGAN MUSIK - DOA REFLEKSI WL]:
"Kami bersyukur Tuhan untuk menyambut adik-adik kami, teman-teman kami, untuk bersama-sama menikmati masa muda dalam PERMATA. Ini kami anak-anak Tuhan, kami butuh Engkau, dan kiranya Tuhan berkenan untuk kami selalu saling merangkul."</div>
      </div>

      <button class="next-session-btn" onclick="scrollToSession(10)">
        <span>Masuk Puncak &rarr; Lanjut ke Lagu 5 (Sentuh Hatiku)</span>
      </button>
    </div>

    <!-- SESI 10: LAGU 5 (PUNCAK PEMBASUHAN KAKI - SENTUH HATIKU) -->
    <div class="section-card song-session" id="session-10">
      <div class="section-header">
        <div>
          <span class="time-badge">35:00 - 51:25 (PUNCAK SAKRAL)</span>
          <div class="session-title">Sesi 10: PUNCAK — Pembasuhan Kaki (Sentuh Hatiku)</div>
        </div>
        <span class="session-type-badge type-song">🌊 Puncak Pembasuhan</span>
      </div>

      <div class="video-card">
        <div class="video-card-header">
          <div class="video-card-title">
            <span>🎬 Video Karaoke &amp; Lirik YouTube (Sentuh Hatiku)</span>
          </div>
          <span class="video-card-badge">Do = G / A • 1080p</span>
        </div>
        <video id="video-5" controls loop playsinline preload="metadata" class="song-video" src="/video/5"></video>
      </div>

      <button class="play-video-cta" onclick="playSongVideo(5)">
        <span>▶ PUTAR VIDEO &amp; MULAI NYANYI (Base Song Auto-Fade Out)</span>
      </button>

      <div class="box cue-box">
        <div class="cue-title">💡 Petunjuk Tim Pembasuh (Pengurus &amp; Kakak Abang)</div>
        • <strong>Aksi:</strong> Berlutut dengan dua lutut menapak lantai. Siramkan air secara lembut, basuh kaki dengan kehangatan kasih, keringkan dengan handuk putih bersih.<br>
        • <strong>Bisikan Berkat:</strong> Tatap matanya dan bisikkan: <em>"Dek, kami dan Tuhan menerima kam dengan kerendahan hati apa adanya. Segala bebanmu Tuhan pulihkan hari ini. Kamu sangat berharga di mata Tuhan, selamat datang di keluarga PERMATA Bogor."</em>
      </div>

      <div class="box lyrics-box">
        <div class="lyrics-title">
          <span>🎵 Teks Lirik Lagu (Sentuh Hatiku)</span>
          <span style="color:var(--gold);">Do = G / A</span>
        </div>
        <div class="lyrics-text"><strong>[Verse 1]</strong>
Betapa kumencintai
Segala yang t'lah terjadi
Tak pernah sendiri jalani hidup ini
Selalu menyertai

<strong>[Verse 2]</strong>
Betapa kumenyadari
Di dalam hidupku ini
Kau s'lalu memberi rancangan terbaik
Oleh karena kasih

<strong>[Chorus]</strong>
Bapa, sentuh hatiku, ubah hidupku
Menjadi yang baru
Bagai emas yang murni
Kau membentuk bejana hatiku

Bapa, ajarku mengerti sebuah kasih
Yang selalu memberi
Bagai air mengalir
Yang tiada pernah berhenti</div>
      </div>

      <div class="box speech-box">
        <div class="speech-title">🎙️ Renungan WL di Sela-Sela Pembasuhan</div>
        <div class="speech-text">"Saat air membasuh kakimu, rasakan bagaimana Tuhan dan saudaramu menerimamu dengan kerendahan hati tanpa syarat. Biarlah segala kepahitan masa lalu, rasa minder yang mengekangmu, dan keletihan jiwa dibasuh bersih oleh kasih Yesus. Katakan di dalam lubuk hatimu kepada-Nya: <em>'Bapa, ini hidupku... sentuh hatiku, ubah hidupku menjadi yang baru seturut kehendak-Mu.'</em>"</div>
      </div>

      <button class="next-session-btn" onclick="stopVideoAndAdvance(5, 11)">
        <span>Selesai Pembasuhan &rarr; Lanjut ke Sesi 11 (Doa Penutup &amp; Berkat)</span>
      </button>
    </div>

    <!-- SESI 11: 51:25 - 55:30 -->
    <div class="section-card" id="session-11">
      <div class="section-header">
        <div>
          <span class="time-badge">51:25 - 55:30 (Durasi: 4 Menit)</span>
          <div class="session-title">Sesi 11: Doa Penutup, Pengurapan &amp; Berkat Imamat</div>
        </div>
        <span class="session-type-badge type-speech">🎙️ Doa Berkat</span>
      </div>

      <div class="box cue-box">
        <div class="cue-title">💡 Petunjuk Acara &amp; Lighting</div>
        • <strong>Pemimpin Doa:</strong> Bang Nuel / BP PERMATA Rg. Bogor / Pendeta Pembina.<br>
        • <strong>Aksi:</strong> Semua peserta dan pengurus berdiri, saling berpegangan tangan erat atau merangkul pundak, menyatukan hati mengucap syukur.<br>
        • <strong>Musik:</strong> Base Song mengalun hangat menopang doa.
      </div>

      <div class="box speech-box">
        <div class="speech-title">🎙️ Pokok Doa Penutup &amp; Pengurapan</div>
        <div class="speech-text">"Tuhan Yesus yang baik, kami mengucap syukur untuk malam yang kudus ini. Engkau telah melawat setiap hati yang lelah dan membasuh kepenatan jiwa kami. Kami serahkan setiap adik-adik kami dan pemuda-pemudi PERMATA Bogor ke dalam tangan-Mu. Kiranya pengurapan Roh Kudus memenuhi kehidupan masa muda kami, agar kami hidup saling mengasihi, merangkul, dan saling menopang.

Selamat datang di rumah persekutuan PERMATA GBKP Runggun Bogor. Kamu berharga, kamu dikasihi, dan kita adalah satu keluarga di dalam Kristus."</div>
      </div>

      <div class="box scripture-box">
        <div class="scripture-title">📖 Doa Berkat Imamat (TB LAI Terverifikasi)</div>
        <div class="scripture-text"><strong>Bilangan 6:24-26</strong> — "TUHAN memberkati engkau dan melindungi engkau; TUHAN menyinari engkau dengan wajah-Nya dan memberi engkau kasih karunia; TUHAN menghadapkan wajah-Nya kepadamu dan memberi engkau damai sejahtera."</div>
      </div>

      <button class="next-session-btn" onclick="scrollToSession(12)">
        <span>Masuk Sukacita Penutup &rarr; Lanjut ke Lagu 6 (Hari Ini Kurasa Bahagia)</span>
      </button>
    </div>

    <!-- SESI 12: LAGU 6 (SUKACITA PENUTUP - HARI INI KURASA BAHAGIA) -->
    <div class="section-card song-session" id="session-12">
      <div class="section-header">
        <div>
          <span class="time-badge">55:30 - 58:44 (SUKACITA PENUTUP)</span>
          <div class="session-title">Sesi 12: Lagu 6 — Hari Ini Kurasa Bahagia</div>
        </div>
        <span class="session-type-badge type-song">🎉 Sorak Sukacita</span>
      </div>

      <div class="box cue-box" style="border-left-color: #eab308; background: rgba(234, 179, 8, 0.1); color: #fef08a;">
        <div class="cue-title" style="color: #eab308;">💡 HIGHLIGHT SUKACITA: SEMUA LAMPU NYALA TERANG!</div>
        • <strong>Lighting:</strong> SEMUA LAMPU RUANGAN DINYALAKAN TERANG PENUH!<br>
        • <strong>Aksi:</strong> Seluruh ruangan berdiri berpegangan tangan, bertepuk tangan, bersorak gembira, dan berpelukan hangat menyambut keluarga baru PERMATA Bogor!
      </div>

      <div class="box speech-box">
        <div class="speech-title">🎙️ Kata-Kata yang Dikeluarkan WL (Deklarasi Sukacita &amp; Sambutan Keluarga Baru)</div>
        <div class="speech-text">"Bagi kita yang sudah dibasuh... hidup kita bukan lagi menjadi orang asing, tetapi hidup kita sekarang sudah berjalan bersama dengan yang benar yaitu Kristus Yesus! Yang lama sudah berlalu, sungguh yang baru sudah datang!

Marilah kita bersukacita dan bergembira bersama di PERMATA Bogor! Karena adik-adik kita, teman-teman kita semua sudah resmi bergabung ke dalam PERMATA Bogor dan menjadi keluarga baru kita!

Mereka sekarang sudah bersama-sama dengan kita! Mari kita bersukacita, bersenang-senang, dan merayakannya bersama dengan tepuk tangan dan sorak-sorai yang paling meriah bagi Tuhan Yesus!"</div>
      </div>

      <div class="video-card">
        <div class="video-card-header">
          <div class="video-card-title">
            <span>🎬 Video Karaoke &amp; Lirik YouTube (Nada Wanita Cis=Do / F / G)</span>
          </div>
          <span class="video-card-badge">Upbeat • 1080p</span>
        </div>
        <video id="video-6" controls playsinline preload="metadata" class="song-video" src="/video/6"></video>
      </div>

      <button class="play-video-cta" onclick="playSongVideo(6)" style="background: linear-gradient(135deg, #16a34a, #22c55e);">
        <span>▶ PUTAR VIDEO &amp; BERNYANYI BERSAMA (LAMPU TERANG)</span>
      </button>

      <div class="box lyrics-box">
        <div class="lyrics-title">
          <span>🎵 Teks Lirik Lagu</span>
          <span style="color:var(--gold);">Do = F / G / Cis</span>
        </div>
        <div class="lyrics-text">Hari ini kurasa bahagia
Berkumpul bersama saudara seiman
Tuhan Yesus mempersatukan kita
Tanpa memandang di antara kita

<strong>[Reff / Chorus]</strong>
Bergandingan tangan dalam kasih
Dalam satu hati
Berjalan dalam terang kasih Tuhan
Kau sahabatku, kau saudaraku
Tiada yang dapat memisahkan kita
Kau sahabatku, kau saudaraku
Tiada yang dapat memisahkan kita!</div>
      </div>

      <div class="box scripture-box">
        <div class="scripture-title">📖 Semboyan PERMATA GBKP</div>
        <div class="scripture-text"><strong>Yosua 24:15c</strong> — "Tetapi aku dan seisi rumahku, kami akan beribadah kepada TUHAN!"<br><br>
<em>"Ersada Arih Man Dibata, Si Sampat-sampaten Ibas Kekelengen &bull; Soli Deo Gloria!"</em></div>
      </div>
    </div>

  </div>

  <!-- Persistent Bottom Control Bar -->
  <div class="bottom-bar">
    <div class="bottom-row-1">
      <button id="base-play-btn" class="base-btn" onclick="toggleBaseSong()">
        <span id="base-btn-icon">▶</span>
        <span id="base-btn-text">Putar Base Ambient</span>
      </button>

      <div class="bottom-status-text" id="status-display">
        🎵 Standby
      </div>
    </div>

    <div class="volume-container">
      <span>Volume Base:</span>
      <input type="range" id="vol-slider" class="volume-slider" min="0" max="1" step="0.05" value="0.4" oninput="setBaseVolume(this.value)">
      <span id="vol-label">40%</span>
    </div>
  </div>

  <script>
    const baseAudio = document.getElementById('base-audio');
    const basePlayBtn = document.getElementById('base-play-btn');
    const baseBtnIcon = document.getElementById('base-btn-icon');
    const baseBtnText = document.getElementById('base-btn-text');
    const statusDisplay = document.getElementById('status-display');
    const statusBadge = document.getElementById('status-badge');
    const badgeText = document.getElementById('badge-text');
    const volSlider = document.getElementById('vol-slider');
    const volLabel = document.getElementById('vol-label');

    let currentBaseVolume = 0.4;
    baseAudio.volume = currentBaseVolume;
    let fadeInterval = null;

    // Toggle Base Song
    function toggleBaseSong() {
      if (baseAudio.paused) {
        pauseAllVideos();
        fadeInBase(currentBaseVolume);
      } else {
        fadeOutBase();
      }
    }

    function setBaseVolume(val) {
      currentBaseVolume = parseFloat(val);
      volLabel.innerText = Math.round(currentBaseVolume * 100) + '%';
      if (!baseAudio.paused) {
        baseAudio.volume = currentBaseVolume;
      }
    }

    // Smooth Fade Out
    function fadeOutBase(callback) {
      clearInterval(fadeInterval);
      fadeInterval = setInterval(() => {
        let v = baseAudio.volume;
        v = Math.max(0, v - 0.05);
        baseAudio.volume = v;
        if (v <= 0.01) {
          clearInterval(fadeInterval);
          baseAudio.pause();
          updateUI(false);
          if (callback) callback();
        }
      }, 40);
    }

    // Smooth Fade In
    function fadeInBase(targetVol) {
      clearInterval(fadeInterval);
      if (!targetVol) targetVol = currentBaseVolume;
      baseAudio.volume = 0;
      baseAudio.play().then(() => {
        updateUI(true);
        fadeInterval = setInterval(() => {
          let v = baseAudio.volume;
          v = Math.min(targetVol, v + 0.05);
          baseAudio.volume = v;
          if (v >= targetVol - 0.01) {
            clearInterval(fadeInterval);
            baseAudio.volume = targetVol;
          }
        }, 40);
      }).catch(err => {
        console.log('Autoplay policy:', err);
      });
    }

    function updateUI(isPlayingBase) {
      if (isPlayingBase) {
        basePlayBtn.classList.add('playing');
        baseBtnIcon.innerText = '❚❚';
        baseBtnText.innerText = 'Jeda Base';
        statusDisplay.innerText = '🎵 Base Ambient: Mengalun Lembut';
        statusBadge.className = 'status-badge badge-ambient';
        badgeText.innerText = 'BASE AMBIENT AKTIF';
      } else {
        basePlayBtn.classList.remove('playing');
        baseBtnIcon.innerText = '▶';
        baseBtnText.innerText = 'Putar Base Ambient';
        if (isAnyVideoPlaying()) {
          statusDisplay.innerText = '🎬 Video Karaoke Sedang Diputar';
          statusBadge.className = 'status-badge badge-video';
          badgeText.innerText = 'VIDEO KARAOKE AKTIF';
        } else {
          statusDisplay.innerText = '⏸ Standby';
          statusBadge.className = 'status-badge badge-paused';
          badgeText.innerText = 'STANDBY';
        }
      }
    }

    function isAnyVideoPlaying() {
      let any = false;
      document.querySelectorAll('.song-video').forEach(v => {
        if (!v.paused) any = true;
      });
      return any;
    }

    function pauseAllVideos() {
      document.querySelectorAll('.song-video').forEach(v => {
        if (!v.paused) v.pause();
      });
    }

    // Play Song Video with smart auto-fade of Base Song
    function playSongVideo(songNum) {
      const vid = document.getElementById('video-' + songNum);
      if (!vid) return;

      // Pause any other video
      document.querySelectorAll('.song-video').forEach(v => {
        if (v !== vid && !v.paused) v.pause();
      });

      // Highlight active session
      highlightSession('session-' + (songNum * 2));

      // Fade out Base Song and start video
      fadeOutBase(() => {
        vid.scrollIntoView({ behavior: 'smooth', block: 'center' });
        vid.play().then(() => {
          updateUI(false);
        }).catch(err => console.log('Video play error:', err));
      });
    }

    // When video ends or user advances
    function stopVideoAndAdvance(songNum, nextSessionNum) {
      const vid = document.getElementById('video-' + songNum);
      if (vid && !vid.paused) {
        vid.pause();
      }
      fadeInBase(currentBaseVolume);
      scrollToSession(nextSessionNum);
    }

    function scrollToSession(num) {
      const card = document.getElementById('session-' + num);
      if (card) {
        highlightSession('session-' + num);
        card.scrollIntoView({ behavior: 'smooth', block: 'start' });
        if (baseAudio.paused) {
          fadeInBase(currentBaseVolume);
        }
      }
    }

    function highlightSession(id) {
      document.querySelectorAll('.section-card').forEach(c => c.classList.remove('active-session'));
      const target = document.getElementById(id);
      if (target) target.classList.add('active-session');
    }

    // Video Event Listeners
    document.querySelectorAll('.song-video').forEach(vid => {
      vid.addEventListener('play', () => {
        fadeOutBase();
        document.querySelectorAll('.song-video').forEach(other => {
          if (other !== vid && !other.paused) other.pause();
        });
      });
      vid.addEventListener('ended', () => {
        fadeInBase(currentBaseVolume);
      });
    });

    // Filter implementation
    function setFilter(type, el) {
      document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
      el.classList.add('active');

      const cards = document.querySelectorAll('.section-card');
      cards.forEach(card => {
        if (type === 'all') {
          card.style.display = 'block';
        } else if (type === 'songs') {
          card.style.display = card.classList.contains('song-session') ? 'block' : 'none';
        } else if (type === 'speeches') {
          card.style.display = card.querySelector('.speech-box') ? 'block' : 'none';
        } else if (type === 'scriptures') {
          card.style.display = card.querySelector('.scripture-box') ? 'block' : 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/base-song')
def stream_base_song():
    if not os.path.exists(BASE_SONG_FILE):
        return "Base song file not found", 404
    return send_file(BASE_SONG_FILE, mimetype="audio/mpeg", conditional=True)

@app.route('/video/<int:song_num>')
def stream_video(song_num):
    vid_path = get_video_path(song_num)
    if not vid_path or not os.path.exists(vid_path):
        return "Video not found", 404
    return send_file(vid_path, mimetype="video/mp4", conditional=True)

@app.route('/download-guide')
def download_guide():
    guide_path = os.path.join(AUDIO_DIR, "Buku_Panduan_Liturgi_Pembasuhan_MAPER_Bogor.pdf")
    if not os.path.exists(guide_path):
        return "Guide PDF not found", 404
    return send_file(guide_path, as_attachment=True, download_name="Buku_Panduan_Liturgi_Pembasuhan_MAPER_Bogor.pdf", mimetype="application/pdf")

@app.route('/download-pdf')
def download_pdf():
    if not os.path.exists(PDF_FILE):
        return "PDF not found", 404
    return send_file(PDF_FILE, as_attachment=True, download_name="Buku_Lirik_Lagu_Pembasuhan_MAPER_Bogor.pdf", mimetype="application/pdf")

if __name__ == '__main__':
    port = 8080
    ips = get_all_ips()
    print("=" * 65)
    print("  SMART WEB CONDUCTOR & COMPANION MAPER PERMATA BOGOR")
    print("  PILIHAN 1: BASE SONG AMBIENT + FULL HD VIDEO KARAOKE MP4")
    print("=" * 65)
    print("  Server Berhasil Dijalankan di Laptop!")
    print("")
    print("  👉 Buka di Browser HP Anda (Chrome / Safari):")
    for ip in ips:
        print(f"     http://{ip}:{port}")
    print("=" * 65)
    app.run(host='0.0.0.0', port=port, threaded=True)
