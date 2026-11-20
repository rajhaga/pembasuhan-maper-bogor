# -*- coding: utf-8 -*-
"""
Script to generate the Official Shareable Songbook PDF:
'Buku Lirik & Panduan Lagu Ibadah Pembasuhan MAPER PERMATA GBKP Runggun Bogor'
Features:
- Clean 3-Page A4 design optimized for mobile sharing (WhatsApp) & physical printing.
- Complete canonical lyrics, musical keys (nada dasar), biblical references, and spiritual functions.
- Fully synchronized with the 60-Minute Master MP3 and Web Teleprompter.
"""

import os
from playwright.sync_api import sync_playwright

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>BUKU LIRIK LAGU PEMBASUHAN MAPER PERMATA GBKP BOGOR</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 0;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      color: #0f172a;
      background: #ffffff;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    .page {
      width: 210mm;
      height: 297mm;
      padding: 13mm 15mm 13mm 15mm;
      position: relative;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: #ffffff;
    }
    
    /* Top Header */
    .top-header {
      border-bottom: 2px solid #1e3a8a;
      padding-bottom: 6px;
      margin-bottom: 8px;
    }
    .org-badge {
      font-size: 8pt;
      font-weight: 800;
      letter-spacing: 1px;
      color: #2563eb;
      text-transform: uppercase;
    }
    .main-title {
      font-size: 15.5pt;
      font-weight: 800;
      color: #1e3a8a;
      letter-spacing: -0.2px;
      margin: 1px 0;
      text-transform: uppercase;
    }
    .sub-title {
      font-size: 8.5pt;
      font-weight: 600;
      color: #475569;
    }

    /* Summary Table on Page 1 */
    .summary-box {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      padding: 6px 10px;
      margin-bottom: 9px;
    }
    .summary-title {
      font-size: 8.2pt;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: flex;
      justify-content: space-between;
    }
    .summary-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 7.2pt;
    }
    .summary-table th {
      background: #e2e8f0;
      color: #1e293b;
      font-weight: 700;
      text-align: left;
      padding: 3px 6px;
      border: 1px solid #cbd5e1;
    }
    .summary-table td {
      padding: 2.5px 6px;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .summary-table tr:nth-child(even) {
      background: #ffffff;
    }

    /* Song Section Card */
    .song-box {
      border: 1.5px solid #cbd5e1;
      border-radius: 6px;
      margin-bottom: 9px;
      overflow: hidden;
      background: #ffffff;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
      display: flex;
      flex-direction: column;
    }
    .song-box-header {
      background: #1e293b;
      color: #ffffff;
      padding: 5px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .song-box-title {
      font-size: 10pt;
      font-weight: 800;
      color: #f8fafc;
      letter-spacing: 0.2px;
    }
    .song-badges {
      display: flex;
      gap: 5px;
      align-items: center;
    }
    .badge-key {
      background: #f59e0b;
      color: #000000;
      font-size: 7.5pt;
      font-weight: 800;
      padding: 1.5px 6px;
      border-radius: 10px;
    }
    .badge-time {
      background: #3b82f6;
      color: #ffffff;
      font-size: 7pt;
      font-weight: 700;
      padding: 1.5px 6px;
      border-radius: 10px;
    }

    .song-meta-bar {
      background: #f1f5f9;
      border-bottom: 1px solid #e2e8f0;
      padding: 3.5px 10px;
      display: flex;
      justify-content: space-between;
      font-size: 7.3pt;
      color: #475569;
    }
    .song-meta-item strong {
      color: #0f172a;
    }

    .song-content {
      padding: 8px 12px;
      font-size: 8.2pt;
      line-height: 1.35;
      color: #1e293b;
    }
    .verse-block {
      margin-bottom: 6px;
    }
    .verse-block:last-child {
      margin-bottom: 0;
    }
    .verse-tag {
      font-size: 7.5pt;
      font-weight: 800;
      color: #b91c1c;
      text-transform: uppercase;
      margin-right: 4px;
    }
    .chorus-block {
      background: #eff6ff;
      border-left: 3.5px solid #2563eb;
      padding: 4.5px 8px;
      border-radius: 0 4px 4px 0;
      margin: 5px 0;
      font-weight: 600;
      color: #1e3a8a;
    }
    .chorus-tag {
      font-size: 7.5pt;
      font-weight: 800;
      color: #1d4ed8;
      text-transform: uppercase;
      margin-right: 4px;
    }
    .bridge-block {
      background: #fdf4ff;
      border-left: 3.5px solid #c084fc;
      padding: 4.5px 8px;
      border-radius: 0 4px 4px 0;
      margin: 5px 0;
      font-size: 8pt;
      color: #581c87;
    }

    .song-guide {
      background: #fefce8;
      border-top: 1px dashed #fde047;
      padding: 4px 10px;
      font-size: 7.2pt;
      font-style: italic;
      color: #854d0e;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    /* Page-specific highlight banner */
    .banner-session {
      background: #e0f2fe;
      border-left: 4px solid #0284c7;
      padding: 4px 8px;
      font-size: 7.6pt;
      font-weight: 700;
      color: #0369a1;
      margin-bottom: 7px;
      border-radius: 0 3px 3px 0;
    }

    /* Scriptural Blessing Box on Page 3 */
    .blessing-box {
      background: #f0fdf4;
      border: 1.5px solid #86efac;
      border-radius: 5px;
      padding: 6px 10px;
      margin-top: 2px;
      text-align: center;
    }
    .blessing-title {
      font-size: 8pt;
      font-weight: 800;
      color: #166534;
      text-transform: uppercase;
      margin-bottom: 2px;
    }
    .blessing-text {
      font-size: 7.6pt;
      font-style: italic;
      color: #15803d;
      line-height: 1.3;
    }

    /* Footer */
    .page-footer {
      position: absolute;
      bottom: 7mm;
      left: 15mm;
      right: 15mm;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid #cbd5e1;
      padding-top: 4px;
      font-size: 7.2pt;
      color: #64748b;
    }
  </style>
</head>
<body>

  <!-- ================= PAGE 1 ================= -->
  <div class="page">
    <div class="top-header">
      <div class="org-badge">PERMATA GBKP RUNGGUN BOGOR &bull; MAPER 2026</div>
      <div class="main-title">BUKU LIRIK &amp; PANDUAN LAGU PEMBASUHAN KAKI</div>
      <div class="sub-title">Kompilasi 6 Pujian &amp; Penyembahan Ibadah Sakral Pembasuhan Kaki (60 Menit Reflektif)</div>
    </div>

    <!-- Ringkasan Lagu -->
    <div class="summary-box">
      <div class="summary-title">
        <span>Tabel Ringkasan Lagu Ibadah Pembasuhan</span>
        <span style="font-weight:600; color:#475569; text-transform:none;">Total: 6 Lagu</span>
      </div>
      <table class="summary-table">
        <thead>
          <tr>
            <th style="width: 28px;">No</th>
            <th>Judul Lagu</th>
            <th style="width: 80px;">Nada Dasar</th>
            <th style="width: 85px;">Waktu Rundown</th>
            <th>Fungsi Rohani Liturgi</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:700; text-align:center;">1</td>
            <td><strong>Seperti Rusa yang Rindu Sungai-Mu</strong></td>
            <td>Do = D</td>
            <td>03:30 - 08:00</td>
            <td>Pembuka &bull; Hadirat Allah &amp; Kehausan Jiwa</td>
          </tr>
          <tr>
            <td style="font-weight:700; text-align:center;">2</td>
            <td><strong>Sejauh Timur Dari Barat</strong></td>
            <td>Do = C / D</td>
            <td>10:00 - 15:35</td>
            <td>Pengakuan Dosa &bull; Kasih Pengampunan Bapa</td>
          </tr>
          <tr>
            <td style="font-weight:700; text-align:center;">3</td>
            <td><strong>Sujud Di Altar-Nya</strong></td>
            <td>Do = D / E</td>
            <td>20:00 - 25:35</td>
            <td>Penyerahan Beban &bull; Saling Mendoakan</td>
          </tr>
          <tr>
            <td style="font-weight:700; text-align:center;">4</td>
            <td><strong>Hati Sebagai Hamba</strong></td>
            <td>Do = C / D</td>
            <td>28:30 - 33:18</td>
            <td>Transisi Pembasuhan &bull; Komitmen Bersimpuh</td>
          </tr>
          <tr>
            <td style="font-weight:700; text-align:center;">5</td>
            <td><strong>Sentuh Hatiku</strong></td>
            <td>Do = G / A</td>
            <td>35:00 - 51:25</td>
            <td>Puncak Pembasuhan Kaki (Looped Ambient)</td>
          </tr>
          <tr>
            <td style="font-weight:700; text-align:center;">6</td>
            <td><strong>Hari Ini Kurasa Bahagia</strong></td>
            <td>Do = F / G (Cis)</td>
            <td>55:30 - 58:44</td>
            <td>Penutup &bull; Sukacita Persaudaraan (Lampu Terang)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="banner-session">
      BAGIAN I: PEMBUKAAN, KERINDUAN JIWA &amp; PENGAKUAN DOSA (00:00 - 15:35)
    </div>

    <!-- LAGU 1 -->
    <div class="song-box">
      <div class="song-box-header">
        <span class="song-box-title">1. Seperti Rusa yang Rindu Sungai-Mu (As the Deer)</span>
        <div class="song-badges">
          <span class="badge-key">Nada: Do = D</span>
          <span class="badge-time">03:30 - 08:00</span>
        </div>
      </div>
      <div class="song-meta-bar">
        <span class="song-meta-item"><strong>Pencipta:</strong> Martin J. Nystrom (1981)</span>
        <span class="song-meta-item"><strong>Ayat Kunci:</strong> Mazmur 42:2</span>
        <span class="song-meta-item"><strong>Suasana:</strong> Solo Piano Lembut &amp; Sangat Tenang</span>
      </div>
      <div class="song-content">
        <div class="verse-block">
          <span class="verse-tag">[Bait 1]</span>
          S'perti rusa rindu sungai-Mu, jiwaku rindu Engkau<br>
          Kaulah Tuhan hasrat hatiku, kurindu menyembah-Mu.
        </div>
        <div class="verse-block">
          <span class="verse-tag">[Bait 2]</span>
          Engkau kekuatan dan perisaiku, kepada-Mu rohku berserah<br>
          Kaulah Tuhan hasrat hatiku, kurindu menyembah-Mu.
        </div>
        <div class="chorus-block">
          <span class="chorus-tag">[Chorus / Reff]</span>
          Yesus, Yesus, Kau berarti bagiku<br>
          Yesus, Yesus, Kau segalanya bagiku.
        </div>
      </div>
      <div class="song-guide">
        💡 <strong>Panduan WL &amp; Singer:</strong> Dinyanyikan setelah WL membuka hati adik-adik. Kakak/abang merangkul pundak adik di sampingnya. Di akhir lagu, hening sejenak untuk doa pembuka hadirat Roh Kudus.
      </div>
    </div>

    <!-- LAGU 2 -->
    <div class="song-box">
      <div class="song-box-header">
        <span class="song-box-title">2. Sejauh Timur Dari Barat</span>
        <div class="song-badges">
          <span class="badge-key">Nada: Do = C &rarr; D</span>
          <span class="badge-time">10:00 - 15:35</span>
        </div>
      </div>
      <div class="song-meta-bar">
        <span class="song-meta-item"><strong>Pencipta:</strong> Jonathan Prawira</span>
        <span class="song-meta-item"><strong>Ayat Kunci:</strong> Mazmur 103:12 &bull; Yesaya 1:18</span>
        <span class="song-meta-item"><strong>Suasana:</strong> Pengakuan Dosa &amp; Haru Kelegaan</span>
      </div>
      <div class="song-content">
        <div class="verse-block">
          <span class="verse-tag">[Bait]</span>
          Sejauh timur dari barat, Engkau membuang dosaku<br>
          Tiada Kau ingat lagi pelanggaranku<br>
          Jauh ke dalam tubir laut, Kau melemparkan dosaku<br>
          Tiada Kau perhitungkan kesalahanku.
        </div>
        <div class="chorus-block">
          <span class="chorus-tag">[Chorus / Reff]</span>
          Betapa besar kasih pengampunan-Mu Tuhan<br>
          Tak Kau pandang hina hati yang hancur<br>
          Ku berterima kasih kepada-Mu ya Tuhan<br>
          Pengampunan yang Kau beri pulihkanku.
        </div>
      </div>
      <div class="song-guide">
        💡 <strong>Panduan WL &amp; Singer:</strong> Dimulai setelah Liturgis membacakan Yesaya 1:18. Ajak peserta menyadari kasih pengampunan Kristus. Jangan ada rasa tertuduh; salib Kristus menyucikan segala dosa.
      </div>
    </div>

    <div class="page-footer">
      <span>BUKU LIRIK LAGU PEMBASUHAN MAPER &bull; PERMATA GBKP RG. BOGOR</span>
      <span>Halaman 1 dari 3</span>
    </div>
  </div>

  <!-- ================= PAGE 2 ================= -->
  <div class="page">
    <div class="top-header">
      <div class="org-badge">PERMATA GBKP RUNGGUN BOGOR &bull; MAPER 2026</div>
      <div class="main-title">BUKU LIRIK &amp; PANDUAN LAGU PEMBASUHAN KAKI</div>
      <div class="sub-title">Bagian II: Penyerahan Beban, Saling Mendoakan &amp; Meneladani Kasih Hamba Kristus</div>
    </div>

    <div class="banner-session">
      BAGIAN II: HENING DOA PRIBADI &amp; KOMITMEN MELAYANI (15:35 - 33:18)
    </div>

    <!-- LAGU 3 -->
    <div class="song-box">
      <div class="song-box-header">
        <span class="song-box-title">3. Sujud Di Altar-Nya</span>
        <div class="song-badges">
          <span class="badge-key">Nada: Do = D &rarr; E</span>
          <span class="badge-time">20:00 - 25:35</span>
        </div>
      </div>
      <div class="song-meta-bar">
        <span class="song-meta-item"><strong>Pencipta:</strong> Ir. Djohan E. Handojo</span>
        <span class="song-meta-item"><strong>Ayat Kunci:</strong> Matius 11:28 &bull; Yakobus 5:16</span>
        <span class="song-meta-item"><strong>Suasana:</strong> Haru, Pasrah &amp; Momen Saling Menopang</span>
      </div>
      <div class="song-content">
        <div class="verse-block">
          <span class="verse-tag">[Bait 1]</span>
          Bila hati terasa berat, tak seorang pun mengerti bebanku<br>
          Kutanya Yesus apa yang harus kubuat.
        </div>
        <div class="verse-block">
          <span class="verse-tag">[Bait 2]</span>
          Dia berfirman: "Mari datanglah", Dia selalu pedulikan aku<br>
          Kudatang Yesus, Dia pikul segala bebanku.
        </div>
        <div class="chorus-block">
          <span class="chorus-tag">[Chorus / Reff]</span>
          Sujud di altar-Nya, kubawa hidupku, kuterima anugerah-Nya<br>
          Dia ampuniku dan bebaskanku, Dia ubah hidupku, baharui hatiku<br>
          Sesuatu terjadi saat datang di altar-Nya.
        </div>
        <div class="bridge-block">
          <span class="chorus-tag" style="color:#581c87;">[Bridge / Peneguhan]</span><br>
          Pemulihan terjadi, mukjizat terjadi<br>
          Kemenangan terjadi saat datang di altar-Nya!
        </div>
      </div>
      <div class="song-guide">
        💡 <strong>Panduan WL &amp; Singer:</strong> Dilakukan setelah hening 2 menit (tangan di dada). Kakak/abang mendoakan adik di sampingnya, memegang pundak dan menopang beban pergumulan studinya/keluarganya.
      </div>
    </div>

    <!-- LAGU 4 -->
    <div class="song-box">
      <div class="song-box-header">
        <span class="song-box-title">4. Hati Sebagai Hamba</span>
        <div class="song-badges">
          <span class="badge-key">Nada: Do = C &rarr; D</span>
          <span class="badge-time">28:30 - 33:18</span>
        </div>
      </div>
      <div class="song-meta-bar">
        <span class="song-meta-item"><strong>Pencipta:</strong> Jonathan Prawira</span>
        <span class="song-meta-item"><strong>Ayat Kunci:</strong> Filipi 2:5-7 &bull; Ayub 1:21</span>
        <span class="song-meta-item"><strong>Suasana:</strong> Kerendahan Hati, Bersimpuh, Air Kendi Dituang</span>
      </div>
      <div class="song-content">
        <div class="verse-block">
          <span class="verse-tag">[Verse / Bait]</span>
          Ku tak membawa apapun juga saat ku datang ke dunia<br>
          Ku tinggal semua pada akhirnya saat ku kembali ke surga.
        </div>
        <div class="chorus-block">
          <span class="chorus-tag">[Chorus / Reff]</span>
          Inilah yang ku punya: hati s'bagai hamba<br>
          Yang mau taat dan setia pada-Mu Bapa<br>
          Kemanapun ku bawa hati yang menyembah<br>
          Dalam Roh dan kebenaran sampai s'lamanya.
        </div>
        <div class="bridge-block">
          <span class="chorus-tag" style="color:#581c87;">[Bridge]</span>
          Bagaimana ku membalas kasih-Mu? S'gala yang ku punya itu milik-Mu... itu milik-Mu, oh...
        </div>
      </div>
      <div class="song-guide">
        💡 <strong>Panduan Khusus Pengurus:</strong> Dinyanyikan saat lampu utama dipadamkan (hanya spotlight kendi). Seluruh Badan Pengurus &amp; kakak-abang bersimpuh di depan peserta sebagai tanda siap melayani.
      </div>
    </div>

    <div class="page-footer">
      <span>BUKU LIRIK LAGU PEMBASUHAN MAPER &bull; PERMATA GBKP RG. BOGOR</span>
      <span>Halaman 2 dari 3</span>
    </div>
  </div>

  <!-- ================= PAGE 3 ================= -->
  <div class="page">
    <div class="top-header">
      <div class="org-badge">PERMATA GBKP RUNGGUN BOGOR &bull; MAPER 2026</div>
      <div class="main-title">BUKU LIRIK &amp; PANDUAN LAGU PEMBASUHAN KAKI</div>
      <div class="sub-title">Bagian III: Puncak Pembasuhan Kaki, Doa Pengurapan &amp; Sorak Sukacita Penutup</div>
    </div>

    <div class="banner-session" style="background:#fef3c7; border-left-color:#f59e0b; color:#92400e;">
      BAGIAN III: PUNCAK SAKRAL PEMBASUHAN KAKI &amp; SUKACITA PERSAUDARAAN (33:18 - 58:44)
    </div>

    <!-- LAGU 5 -->
    <div class="song-box">
      <div class="song-box-header" style="background:#047857;">
        <span class="song-box-title">5. Sentuh Hatiku (Puncak Pembasuhan Kaki)</span>
        <div class="song-badges">
          <span class="badge-key" style="background:#fbbf24;">Nada: Do = G &rarr; A</span>
          <span class="badge-time" style="background:#065f46;">35:00 - 51:25</span>
        </div>
      </div>
      <div class="song-meta-bar">
        <span class="song-meta-item"><strong>Pencipta:</strong> Jason Irwanto Chang</span>
        <span class="song-meta-item"><strong>Ayat Kunci:</strong> Yohanes 13:14-15 &bull; Yeremia 18:6</span>
        <span class="song-meta-item"><strong>Durasi:</strong> 16 Menit 25 Detik (Ambient Loop Khidmat)</span>
      </div>
      <div class="song-content">
        <div class="verse-block">
          <span class="verse-tag">[Verse 1]</span>
          Betapa kumencintai segala yang t'lah terjadi<br>
          Tak pernah sendiri jalani hidup ini, selalu menyertai.
        </div>
        <div class="verse-block">
          <span class="verse-tag">[Verse 2]</span>
          Betapa kumenyadari di dalam hidupku ini<br>
          Kau s'lalu memberi rancangan terbaik oleh karena kasih.
        </div>
        <div class="chorus-block" style="background:#ecfdf5; border-left-color:#10b981; color:#064e3b;">
          <span class="chorus-tag" style="color:#047857;">[Chorus / Reff]</span>
          Bapa sentuh hatiku, ubah hidupku menjadi yang baru<br>
          Bagai emas yang murni, Kau membentuk bejana hatiku<br>
          Bapa ajarku mengerti sebuah kasih yang selalu memberi<br>
          Bagai air mengalir yang tiada pernah berhenti.
        </div>
      </div>
      <div class="song-guide">
        💡 <strong>Prosesi Pembasuhan Kaki:</strong> Kakak/abang membasuh kaki adik-adik dengan air hangat, mengeringkannya dengan handuk bersih, lalu memeluk dan membisikkan kata penguatan: <em>"Adikku, kamu berharga di mata Tuhan dan di PERMATA Bogor."</em>
      </div>
    </div>

    <!-- LAGU 6 -->
    <div class="song-box">
      <div class="song-box-header" style="background:#b91c1c;">
        <span class="song-box-title">6. Hari Ini Kurasa Bahagia</span>
        <div class="song-badges">
          <span class="badge-key" style="background:#fef08a; color:#854d0e;">Nada: Do = F &rarr; G / Cis</span>
          <span class="badge-time" style="background:#991b1b;">55:30 - 58:44</span>
        </div>
      </div>
      <div class="song-meta-bar">
        <span class="song-meta-item"><strong>Pencipta:</strong> Pdt. Dr. Stephen Tong</span>
        <span class="song-meta-item"><strong>Ayat Kunci:</strong> Mazmur 133:1 &bull; 1 Yohanes 4:11</span>
        <span class="song-meta-item"><strong>Suasana:</strong> Upbeat Ceria, Bertepuk Tangan, Berdiri Bersama</span>
      </div>
      <div class="song-content">
        <div class="verse-block">
          <span class="verse-tag">[Bait]</span>
          Hari ini ku rasa bahagia berkumpul bersama saudara seiman<br>
          Tuhan Yesus mempersatukan kita tanpa memandang di antara kita.
        </div>
        <div class="chorus-block" style="background:#fef2f2; border-left-color:#ef4444; color:#991b1b;">
          <span class="chorus-tag" style="color:#b91c1c;">[Chorus / Reff]</span>
          Bergandingan tangan dalam kasih, dalam satu hati<br>
          Berjalan dalam terang kasih Tuhan<br>
          Kau sahabatku, kau saudaraku<br>
          Tiada yang dapat memisahkan kita!
        </div>
      </div>
      <div class="song-guide">
        💡 <strong>Aba-aba Lampu &amp; Operator:</strong> SEMUA LAMPU NYALA TERANG! Seluruh ruangan berdiri tegak, bergandengan tangan membentuk lingkaran besar keluarga PERMATA GBKP Bogor, bertepuk tangan dan bersorak penuh sukacita.
      </div>
    </div>

    <!-- Berkat Imamat & Penutup -->
    <div class="blessing-box">
      <div class="blessing-title">DOA BERKAT &amp; PENGURAPAN PERMATA GBKP BOGOR (Bilangan 6:24-26)</div>
      <div class="blessing-text">
        "TUHAN memberkati engkau dan melindungi engkau; TUHAN menyinari engkau dengan wajah-Nya dan memberi engkau kasih karunia; TUHAN menghadapkan wajah-Nya kepadamu dan memberi engkau damai sejahtera. Amin! Soli Deo Gloria!"
      </div>
    </div>

    <div class="page-footer">
      <span>BUKU LIRIK LAGU PEMBASUHAN MAPER &bull; PERMATA GBKP RG. BOGOR</span>
      <span>Halaman 3 dari 3</span>
    </div>
  </div>

</body>
</html>
"""

def generate_pdf():
    # Save destinations
    output_dir_1 = r"d:\Downloads\web presentation data - Copy (1)\web presentation data - Copy"
    output_dir_2 = r"D:\Downloads\Lagu pembasuhan"
    
    file_name = "Buku_Lirik_Lagu_Pembasuhan_MAPER_Bogor.pdf"
    path_1 = os.path.join(output_dir_1, file_name)
    path_2 = os.path.join(output_dir_2, file_name)

    html_temp_path = os.path.join(output_dir_1, "temp_songbook.html")
    with open(html_temp_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Rendering Songbook PDF using Playwright...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file:///{os.path.abspath(html_temp_path).replace(os.sep, '/')}")
        page.wait_for_load_state("networkidle")
        
        pdf_bytes = page.pdf(
            format="A4",
            print_background=True,
            margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"}
        )
        browser.close()

    with open(path_1, "wb") as f:
        f.write(pdf_bytes)
    print(f"Generated successfully: {path_1} ({len(pdf_bytes)} bytes)")

    try:
        with open(path_2, "wb") as f:
            f.write(pdf_bytes)
        print(f"Generated copy successfully: {path_2}")
    except Exception as e:
        print(f"Could not write to second path: {e}")

    if os.path.exists(html_temp_path):
        os.remove(html_temp_path)

if __name__ == "__main__":
    generate_pdf()
