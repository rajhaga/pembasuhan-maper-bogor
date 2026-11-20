# -*- coding: utf-8 -*-
"""
Script to generate the official 6-page A4 PDF for Pembasuhan MAPER PERMATA GBKP Rg. Bogor.
Incorporates:
- Updated canonical lyrics for all 6 songs (Seperti Rusa, Sejauh Timur dari Barat, Sujud di Altar-Nya, Hati Sebagai Hamba, Sentuh Hatiku, Hari Ini Kurasa Bahagia)
- Verified Bible Scriptures (TB LAI: Yesaya 1:18, Yeremia 29:11-12, Yakobus 5:16, Filipi 2:3,5-7, Yohanes 13:14-15, 1 Yohanes 1:9, Yosua 24:15, Bilangan 6:24-26)
- Exact 6-page A4 format with page-breaks matching the church retreat liturgy.
"""

import os
from playwright.sync_api import sync_playwright

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>PEMBASUHAN MAPER PERMATA GBKP BOGOR</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 0;
    }
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      background: #ffffff;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    .page {
      width: 210mm;
      height: 297mm;
      padding: 13mm 16mm 14mm 16mm;
      position: relative;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: #ffffff;
    }
    
    /* Header typography */
    .header-tag {
      font-size: 8pt;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: #334155;
      text-transform: uppercase;
      margin-bottom: 2px;
    }
    .main-title {
      font-size: 16.5pt;
      font-weight: 800;
      color: #1d3557;
      letter-spacing: -0.2px;
      margin: 0 0 2px 0;
      text-transform: uppercase;
    }
    .subtitle {
      font-size: 8.6pt;
      font-weight: 600;
      color: #2563eb;
      margin: 0 0 6px 0;
    }
    .divider-line {
      border: none;
      height: 1.5px;
      background: #1d3557;
      margin: 0 0 7px 0;
    }

    /* Boxes */
    .tusar-box {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      padding: 6.5px 10px;
      font-size: 7.9pt;
      line-height: 1.32;
      color: #1e293b;
      margin-bottom: 7px;
    }
    .tusar-box strong {
      color: #0f172a;
    }

    .section-bar {
      font-size: 8.5pt;
      font-weight: 800;
      color: #0f172a;
      text-transform: uppercase;
      letter-spacing: 0.2px;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 2px;
      margin: 5px 0 5px 0;
    }
    .section-bar:first-of-type {
      margin-top: 0;
    }

    /* Speeches */
    .speaker-label {
      font-size: 8.2pt;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 2px;
    }
    .speaker-text {
      font-size: 7.9pt;
      line-height: 1.3;
      color: #334155;
      margin: 0 0 5.5px 0;
    }

    /* Yellow highlight box */
    .callout-yellow {
      background: #fef9c3;
      border-left: 3.5px solid #eab308;
      padding: 5px 8.5px;
      border-radius: 2px;
      font-size: 7.8pt;
      font-weight: 600;
      color: #713f12;
      margin: 5px 0;
      line-height: 1.28;
    }

    /* Pink / Rose Scripture box */
    .callout-pink {
      background: #fdf2f8;
      border-left: 3.5px solid #f472b6;
      padding: 5px 8.5px;
      border-radius: 2px;
      font-size: 7.8pt;
      line-height: 1.28;
      color: #831843;
      margin: 5px 0;
    }
    .callout-pink strong {
      color: #9d174d;
    }

    /* Blue Highlight Banner */
    .banner-blue {
      background: #0284c7;
      color: #ffffff;
      text-align: center;
      font-weight: 800;
      font-size: 8.2pt;
      padding: 4px 8px;
      letter-spacing: 0.5px;
      border-radius: 3px;
      margin: 0 0 5.5px 0;
    }

    /* Technical Cyan Box */
    .callout-cyan {
      background: #f0f9ff;
      border: 1px solid #7dd3fc;
      border-radius: 4px;
      padding: 5.5px 9.5px;
      font-size: 7.5pt;
      line-height: 1.27;
      color: #0c4a6e;
      margin-bottom: 6px;
    }
    .callout-cyan strong {
      color: #0369a1;
    }

    /* Green Alert Box */
    .callout-green {
      background: #dcfce7;
      border-left: 3.5px solid #22c55e;
      padding: 5.5px 9px;
      border-radius: 2px;
      font-size: 7.9pt;
      font-weight: 700;
      color: #15803d;
      margin: 5.5px 0;
      line-height: 1.28;
    }

    /* Lavender Checklist Box */
    .callout-lavender {
      background: #f5f3ff;
      border: 1px solid #ddd6fe;
      border-radius: 4px;
      padding: 5.5px 9.5px;
      font-size: 7.5pt;
      line-height: 1.27;
      color: #4c1d95;
      margin-top: 5.5px;
    }
    .callout-lavender strong {
      color: #5b21b6;
    }

    /* Dashed Prayer Box */
    .dashed-box {
      border: 1.5px dashed #94a3b8;
      background: #f8fafc;
      border-radius: 4px;
      padding: 6px 9px;
      text-align: center;
      font-size: 7.6pt;
      line-height: 1.28;
      color: #475569;
      margin: 5.5px 0;
    }
    .dashed-box strong {
      color: #1e293b;
      display: block;
      margin-bottom: 2px;
    }

    /* Song Box */
    .song-card {
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 5.5px 9.5px;
      background: #ffffff;
      margin: 5px 0;
    }
    .song-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 3.5px;
      padding-bottom: 2.5px;
      border-bottom: 1px dashed #e2e8f0;
    }
    .song-title-group {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .song-title {
      font-size: 8.5pt;
      font-weight: 800;
      color: #b91c1c;
      margin: 0;
    }
    .song-badges {
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .song-badge {
      background: #e0f2fe;
      border: 1px solid #7dd3fc;
      color: #0369a1;
      font-size: 7.1pt;
      font-weight: 700;
      padding: 1px 5px;
      border-radius: 10px;
    }
    .song-yt-link {
      background: #fee2e2;
      border: 1px solid #fca5a5;
      color: #b91c1c;
      font-size: 7.1pt;
      font-weight: 700;
      padding: 1px 5px;
      border-radius: 10px;
      text-decoration: none;
    }
    .song-lyrics {
      font-size: 7.55pt;
      line-height: 1.3;
      color: #334155;
    }
    .song-lyrics strong {
      color: #0f172a;
    }

    .song-note {
      font-size: 7pt;
      font-style: italic;
      color: #64748b;
      margin-top: 2.5px;
      padding-top: 2px;
      border-top: 1px dotted #cbd5e1;
    }

    .soli-deo {
      text-align: center;
      font-size: 7.5pt;
      font-weight: 700;
      letter-spacing: 1px;
      color: #64748b;
      margin-top: 6px;
    }

    /* Footer */
    .page-footer {
      position: absolute;
      bottom: 7mm;
      left: 16mm;
      right: 16mm;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid #cbd5e1;
      padding-top: 3px;
      font-size: 7.5pt;
      color: #64748b;
    }
  </style>
</head>
<body>

  <!-- ================= PAGE 1 ================= -->
  <div class="page">
    <div class="header-tag">MINGGU, PERIODE PEMBINAAN &bull; EDISI TERBARU MAPER BOGOR</div>
    <div class="main-title">PEMBASUHAN MAPER PERMATA GBKP</div>
    <div class="subtitle">Panduan Liturgi, Sesi Reflektif 60 Menit &amp; Naskah Lengkap Pemimpin Pujian (WL) &bull; Rg. Bogor</div>
    <hr class="divider-line">

    <div class="tusar-box">
      <strong>Tusar (Tujuan Sasaran):</strong> Peserta dapat merasakan damai sejahtera lewat penyembahan yang mendalam sehingga sesi ini menjadi media reflektif untuk menyadari betapa pentingnya Tuhan dalam hidupnya, mengalami kasih dan kerendahan hati Kristus lewat pembasuhan kaki oleh pengurus/kakak-abang, serta tergerak untuk menyerahkan diri dan aktif bersama keluarga PERMATA GBKP Bogor.
    </div>

    <div class="section-bar">IRINGAN MUSIK (INTRO LEMBUT &ndash; BASE SONG AMBIENT DO = D)</div>

    <div class="speaker-label">WL: Pengantar Santai &amp; Menyiapkan Hati Masuk Hadirat Tuhan</div>
    <div class="speaker-text">
      "Syalom PERMATA! Gimana makannya hari ini? Enak ya?<br>
      Yuk, sekarang kita ambil posisi duduk yang paling santai dan paling nyaman&hellip; Letakkan tas di samping, dan simpan dulu handphone atau gadget kita masing-masing.<br>
      Mari sejenak kita semua diam&hellip; Tarik napas panjang, tenangkan pikiran dari segala keramaian dan kesibukan di luar sana. Di sini, kita tidak perlu berpura-pura tegar atau memakai topeng. Biarkan hati kita benar-benar hening di hadapan Tuhan."
    </div>

    <div class="callout-yellow">
      <strong>Kakak abang yg bertugas:</strong> Silakan perlahan mendekat, duduk di samping adik-adiknya, rangkul pundak mereka dengan kehangatan kasih persaudaraan sejati.
    </div>

    <div class="speaker-label">WL: Membuka Sembahan dengan Kerinduan Jiwa</div>
    <div class="speaker-text">
      "Di tengah rasa lelah dan kekeringan yang mungkin kita rasakan, mari buka hati kita&hellip; Rasakan betapa jiwa kita merindukan jamahan dan pelukan Tuhan yang memulihkan. Mari bersama-sama kita menyembah Dia."
    </div>

    <div class="song-card">
      <div class="song-header">
        <div class="song-title-group">
          <span class="song-title">1. Seperti Rusa yang Rindu Sungai-Mu</span>
        </div>
        <div class="song-badges">
          <span class="song-badge">Do = D</span>
          <a class="song-yt-link" href="https://www.youtube.com/watch?v=ggU3kDvN0RE" target="_blank">&#9658; YouTube</a>
        </div>
      </div>
      <div class="song-lyrics">
        <strong>[Bait 1]</strong> S'perti rusa rindu sungai-Mu, jiwaku rindu Engkau &bull; Kaulah Tuhan hasrat hatiku, kurindu menyembah-Mu<br>
        <strong>[Bait 2]</strong> Engkau kekuatan dan perisaiku, kepada-Mu rohku berserah &bull; Kaulah Tuhan hasrat hatiku, kurindu menyembah-Mu<br>
        <strong>[Chorus / Reff]</strong> Yesus, Yesus, Kau berarti bagiku &bull; Yesus, Yesus, Kau segalanya bagiku
      </div>
      <div class="song-note">
        (Musik solo piano jernih. Setelah Reff dinyanyikan berulang dengan khusyuk, vokal berhenti &rarr; WL memimpin doa pembuka singkat memohon hadirat Roh Kudus menguasai ruangan.)
      </div>
    </div>

    <div class="page-footer">
      <span>PEMBASUHAN MAPER PERMATA GBKP BOGOR &bull; RUNDOWN REFLEKTIF</span>
      <span>Halaman 1 dari 6</span>
    </div>
  </div>

  <!-- ================= PAGE 2 ================= -->
  <div class="page">
    <div class="section-bar">IRINGAN MUSIK (REFLEKSI KERAPUHAN HIDUP &amp; PENGAKUAN DOSA)</div>

    <div class="speaker-label">WL: Pengantar Mengambil Sikap Berdoa &amp; Refleksi Diri</div>
    <div class="speaker-text">
      "Teman-teman sekalian, jika kita ada di tempat ini hari ini, tidak ada yang kebetulan. Ada maksud dan rancangan kekal Tuhan di balik keberadaan kita. Di masa muda ini, di balik senyuman kita, seringkali ada kepahitan yang kita telan sendiri, luka masa kecil, kekecewaan mendalam, dan rasa hampa yang membayangi.<br>
      Banyak hal dalam hidup mungkin tidak kita pahami, tetapi satu hal yang pasti: langkah kaki kecil kita tidak pernah sedetik pun hilang dari pandangan kasih Tuhan. Namun mari kita jujur di hadapan Bapa yang Mahatahu&hellip; berapa sering kaki kita justru melangkah menjauhi-Nya? Berapa sering keegoisan, amarah terpendam, kesombongan, dan dosa mengotori kekudusan hidup kita? Kita merasa bersalah, merasa kotor, dan merasa tidak layak lagi datang kepada-Nya&hellip;"
    </div>

    <div class="callout-pink">
      <strong>Putri/Liturgis (Yesaya 1:18 - Terjemahan Baru LAI [Terverifikasi]):</strong><br>
      "Marilah, baiklah kita beperkara! &ndash; firman TUHAN &ndash; Sekalipun dosamu merah seperti kirmizi, akan menjadi putih seperti salju; sekalipun berwarna merah seperti kain kesumba, akan menjadi putih seperti bulu domba."
    </div>

    <div class="speaker-label">WL: Meneguhkan Pengampunan Allah yang Sempurna</div>
    <div class="speaker-text">
      "Dengarlah panggilan Bapa&hellip; Siapa di antara kita yang tidak pernah melakukan dosa? Kita semua pernah tersandung, pernah melanggar perintah Tuhan, dan pernah melukai orang lain. Tetapi bersyukurlah, Tuhan kita bukanlah Allah yang suka menghakimi, mempermalukan, atau mengungkit masa lalu kita! Di atas kayu salib Golgota, kasih dan darah-Nya telah tercurah untuk membasuh segala cela kita. Di hadapan salib, tidak ada dosa yang terlalu hitam yang tak sanggup diputihkan oleh anugerah-Nya. Jangan takut, jangan bersembunyi lagi&hellip; datanglah pada pelukan-Nya saat ini."
    </div>

    <div class="callout-yellow">
      <strong>Kakak abang yg bertugas:</strong> Silakan merangkul peserta, pegang tangan mereka dengan tulus dan alirkan rasa aman sejati tanpa penghakiman.
    </div>

    <div class="song-card">
      <div class="song-header">
        <div class="song-title-group">
          <span class="song-title">2. Sejauh Timur Dari Barat</span>
        </div>
        <div class="song-badges">
          <span class="song-badge">Do = C / D</span>
          <a class="song-yt-link" href="https://youtu.be/AiO90i4Rybk" target="_blank">&#9658; YouTube</a>
        </div>
      </div>
      <div class="song-lyrics">
        <strong>[Bait 1]</strong> Sejauh timur dari barat, Engkau membuang dosaku, tiada Kau ingat lagi pelanggaranku<br>
        <strong>[Bait 2]</strong> Jauh ke dalam tubir laut, Kau melemparkan dosaku, tiada Kau perhitungkan kesalahanku<br>
        <strong>[Reff / Chorus]</strong> Betapa besar kasih pengampunan-Mu Tuhan, tak Kau pandang hina hati yang hancur<br>
        Ku berterima kasih kepada-Mu ya Tuhan, pengampunan yang Kau beri pulihkanku
      </div>
    </div>

    <div class="speaker-label">WL: Ajakan Meletakkan Tangan di Dada &amp; Keheningan Doa Pribadi</div>
    <div class="speaker-text">
      "1 Yohanes 1:9 meneguhkan kita: <em>'Jika kita mengaku dosa kita, maka Ia adalah setia dan adil, sehingga Ia akan mengampuni segala dosa kita dan menyucikan kita dari segala kejahatan.'</em><br>
      Saat ini, mari kita semua menundukkan kepala&hellip; <strong>Boleh perlahan letakkan tangan kananmu di dada sebelah kirimu.</strong> Rasakan detak jantungmu. Di balik dadamu yang berdetak ini, ada hati yang mungkin sedang sangat lelah, ada luka yang tak pernah kau ceritakan pada siapapun, ada penyesalan dan kesalahan masa lalu yang kau simpan sendiri. Rasakan nafas hidup yang masih Tuhan berikan. Tanggalkan segala topeng dan gengsimu, bicaralah kepada Tuhan dalam lubuk hatimu yang terdalam&hellip; Dia mendengarkan setiap detak hatimu."
    </div>

    <div class="dashed-box">
      <strong>&mdash;&mdash;&mdash; WAKTU REFLEKSI PRIBADI &amp; HENING TOTAL (SEKITAR 2 MENIT) &mdash;&mdash;&mdash;</strong>
      (Semua peserta tetap meletakkan tangan di dada dalam doa hening pribadi. Base song berbunyi amat teduh. WL dan Singer hening agar peserta fokus bergumul secara personal bersama Tuhan.)
    </div>

    <div class="page-footer">
      <span>PEMBASUHAN MAPER PERMATA GBKP BOGOR &bull; RUNDOWN REFLEKTIF</span>
      <span>Halaman 2 dari 6</span>
    </div>
  </div>

  <!-- ================= PAGE 3 ================= -->
  <div class="page">
    <div class="speaker-label">WL: Deklarasi Pelepasan dan Damai Sejahtera</div>
    <div class="speaker-text">
      "Percayalah di dalam imanmu bahwa Tuhan sungguh mengampuni dan mencurahkan kelegaan sejati. Demi nama Yesus, yang terikat hari ini dilepaskan, yang terbelenggu rasa bersalah dan kutuk masa lalu dibebaskan! Hari ini darah Kristus menyucikan nurani kita, dan damai sejahtera Allah melingkupi hatimu."
    </div>

    <div class="section-bar">IRINGAN MUSIK (PENGANTAR MENDOAKAN BEBAN &amp; PERGUMULAN HIDUP)</div>

    <div class="callout-pink">
      <strong>Putri/Liturgis (Yeremia 29:11-12 &amp; Yakobus 5:16 - TB LAI [Terverifikasi]):</strong><br>
      &bull; <em>"Sebab Aku ini mengetahui rancangan-rancangan apa yang ada pada-Ku mengenai kamu, demikianlah firman TUHAN, yaitu rancangan damai sejahtera dan bukan rancangan kecelakaan, untuk memberikan kepadamu hari depan yang penuh harapan. Dan apabila kamu berseru dan datang untuk berdoa kepada-Ku, maka Aku akan mendengarkan kamu."</em> (Yer. 29:11-12)<br>
      &bull; <em>"Hendaklah kamu saling mengaku dosamu dan saling mendoakan, supaya kamu sembuh. Doa orang yang benar, bila dengan yakin didoakan, sangat besar kuasanya."</em> (Yak. 5:16)
    </div>

    <div class="speaker-label">WL: Mengajak Saling Menguatkan dalam Pergumulan</div>
    <div class="speaker-text">
      "Tetaplah dalam sikap berdoa&hellip; Teman-teman, kita tahu menjalani masa muda di zaman sekarang ini sungguh tidak mudah. Ada tekanan kuliah atau pekerjaan yang menumpuk, konflik di dalam keluarga yang membuat hatimu tertekan, rasa sepi di tengah keramaian, atau kekhawatiran tentang masa depan yang membuatmu sulit tidur di malam hari.<br>
      Tuhan melihat setiap butir air mata yang jatuh di bantalmu saat engkau menangis sendirian. Dan ketahuilah, Tuhan menghadirkan kakak-abangmu di PERMATA ini bukan sekadar teman biasa, tetapi keluarga seiman yang diutus untuk menopangmu dalam doa. Engkau tidak perlu bertarung sendirian lagi. Sebutkan pergumulanmu kepada Tuhan, dan izinkan saudaramu membantumu membawanya ke takhta anugerah."
    </div>

    <div class="callout-yellow">
      <strong>Kakak abang yg bertugas:</strong> Rangkul peserta dengan penuh kelembutan, tanyakan dengan berbisik lembut dari hati ke hati: <strong>"Apa beban atau pokok doa yang paling berat saat ini, dek? Bicaralah, kakak ada di sini untuk mendengarkan dan mendoakanmu."</strong> Pimpin doa bersama bagi adik-adiknya secara intim.
    </div>

    <div class="song-card">
      <div class="song-header">
        <div class="song-title-group">
          <span class="song-title">3. Sujud Di Altar-Nya</span>
        </div>
        <div class="song-badges">
          <span class="song-badge">Do = D / E</span>
          <a class="song-yt-link" href="https://www.youtube.com/watch?v=uNXLkMSAWKc" target="_blank">&#9658; YouTube</a>
        </div>
      </div>
      <div class="song-lyrics">
        <strong>[Bait 1]</strong> Bila hati terasa berat, tak seorang pun mengerti bebanku &bull; Kutanya Yesus: apa yang harus kubuat?<br>
        Dia berfirman: mari datanglah, Dia selalu pedulikan aku &bull; Kudatang Yesus, Dia pikul segala bebanku<br>
        <strong>[Reff]</strong> Sujud di altar-Nya, kubawa hidupku, kuterima anugerah-Nya &bull; Dia ampuniku dan bebaskanku<br>
        Dia ubah hidupku, baharui hatiku, sesuatu terjadi saat datang di altar-Nya<br>
        <strong>[Kemenangan]</strong> Pemulihan terjadi, mukjizat terjadi, kemenangan terjadi, saat datang di altar-Nya!
      </div>
      <div class="song-note">
        (Lagu Sujud di Altar-Nya dinyanyikan mengalir lembut berulang-ulang mengiringi momen kakak-abang mendoakan adik-adiknya hingga suasana dipenuhi keharuan dan kelegaan batin.)
      </div>
    </div>

    <div class="page-footer">
      <span>PEMBASUHAN MAPER PERMATA GBKP BOGOR &bull; RUNDOWN REFLEKTIF</span>
      <span>Halaman 3 dari 6</span>
    </div>
  </div>

  <!-- ================= PAGE 4 ================= -->
  <div class="page">
    <div class="banner-blue">&bull;&bull;&bull; HIGHLIGHT UTAMA: PROSESI KEDATANGAN AIR PEMBASUHAN &bull;&bull;&bull;</div>

    <div class="callout-cyan">
      <strong>PETUNJUK TEKNIS PANGGUNG, PENCAHAYAAN &amp; TATA SUARA (SOUND OF WATER):</strong><br>
      1. <strong>Lighting:</strong> Lampu ruangan diredupkan perlahan (<em>warm ambient</em>). Sorotan lembut tertuju ke arah kendi dan salib.<br>
      2. <strong>Musik:</strong> Vokal berhenti total. Keyboard hanya menahan satu nada pad lembut yang mengambang teduh.<br>
      3. <strong>Prosesi:</strong> Dua orang pengurus berjalan perlahan dan khidmat membawa kendi air bersih, baskom pembasuhan, dan handuk putih.<br>
      4. <strong>HIGHLIGHT SUARA AIR:</strong> Di hadapan peserta, air dituangkan perlahan dari kendi ke baskom dari ketinggian sedang. Suara gemericik aliran air (<em>sound of pouring water</em>) harus terdengar jernih dan meditatif memenuhi keheningan ruangan.
    </div>

    <div class="speaker-label">WL: Narasi Teladan Yesus Membasuh Kaki (Yohanes 13:1-17)</div>
    <div class="speaker-text" style="font-style: italic; color: #475569; margin-bottom: 4px;">
      (Biarkan suara gemericik air mengalir terdengar selama 5-7 detik dalam keheningan total yang kudus&hellip;)
    </div>
    <div class="speaker-text">
      "Dengarkanlah&hellip; suara gemericik air yang mengalir itu&hellip;<br>
      Dua ribu tahun yang lalu, di sebuah ruang atas di Yerusalem, sebelum kayu salib ditegakkan, Yesus &ndash; Tuhan semesta alam &ndash; melakukan hal yang meruntuhkan keangkuhan dunia. Dia melepaskan jubah kemuliaan-Nya. Dia mengambil sehelai kain lenan, mengikatkannya di pinggang-Nya, dan menuangkan air bersih ke dalam baskom.<br>
      Raja segala raja itu berlutut di tanah berdebu, tepat di bawah telapak kaki murid-murid-Nya. Kaki yang kotor oleh debu perjalanan, kaki yang lelah, kaki yang kerap kali salah melangkah. Yesus membasuh kaki mereka satu per satu dengan tangan penuh kasih, lalu menyekanya dengan kain lenan-Nya.<br>
      Saat Petrus menolak karena merasa tidak layak, Yesus memandangnya dan berkata: <em>'Jikalau Aku tidak membasuh engkau, engkau tidak mendapat bagian dalam-Ku.'</em> (Yohanes 13:8)"
    </div>

    <div class="callout-pink">
      <strong>Putri/Liturgis (Filipi 2:3, 5-7 - TB LAI [Terverifikasi]):</strong><br>
      "Hendaklah dengan rendah hati yang seorang menganggap yang lain lebih utama dari pada dirinya sendiri&hellip; Hendaklah kamu dalam hidupmu bersama, menaruh pikiran dan perasaan yang terdapat juga dalam Kristus Yesus, yang walaupun dalam rupa Allah, tidak menganggap kesetaraan dengan Allah itu sebagai milik yang harus dipertahankan, melainkan telah mengosongkan diri-Nya sendiri, dan mengambil rupa seorang hamba, dan menjadi sama dengan manusia."
    </div>

    <div class="speaker-label">WL: Makna Pelayanan di PERMATA GBKP Bogor</div>
    <div class="speaker-text">
      "Air yang ada di hadapan kita hari ini adalah simbol kerendahan hati dan kasih pemulihan Kristus. Kami pengurus dan kakak-abangmu di PERMATA Bogor bukanlah orang-orang yang tanpa cela. Kami pun orang berdosa yang telah ditebus oleh anugerah. Tetapi hari ini, dengan hati seorang hamba, kami rindu menanggalkan keangkuhan kami untuk melayani kalian. Kami rindu membasuh kakimu, sebagai tanda bahwa engkau diterima seutuhnya dalam pelukan persaudaraan PERMATA Bogor."
    </div>

    <div class="song-card">
      <div class="song-header">
        <div class="song-title-group">
          <span class="song-title">4. Hati Sebagai Hamba</span>
        </div>
        <div class="song-badges">
          <span class="song-badge">Do = C / D</span>
          <a class="song-yt-link" href="https://www.youtube.com/watch?v=DFQ_OBbmDxk" target="_blank">&#9658; YouTube</a>
        </div>
      </div>
      <div class="song-note" style="margin-top: 0; margin-bottom: 3px; border-top: none;">
        (Bait dinyanyikan khusus oleh PENGURUS &amp; PELAYAN sebagai ikrar kerendahan hati bersimpuh, lalu jemaat masuk di Reff)
      </div>
      <div class="song-lyrics">
        <strong>[Verse]</strong> Ku tak membawa apapun juga saat ku datang ke dunia, ku tinggal semua pada akhirnya saat ku kembali ke surga<br>
        <strong>[Chorus]</strong> Inilah yang kupunya: hati s'bagai hamba, yang mau taat dan setia pada-Mu Bapa &bull; Kemanapun kubawa hati yang menyembah, dalam Roh dan kebenaran sampai s'lamanya<br>
        <strong>[Bridge]</strong> Bagaimana ku membalas kasih-Mu? S'gala yang kupunya itu milik-Mu, itu milik-Mu oh...
      </div>
    </div>

    <div class="page-footer">
      <span>PEMBASUHAN MAPER PERMATA GBKP BOGOR &bull; RUNDOWN REFLEKTIF</span>
      <span>Halaman 4 dari 6</span>
    </div>
  </div>

  <!-- ================= PAGE 5 ================= -->
  <div class="page">
    <div class="section-bar">SESI BASUH &ndash; PENERIMAAN DENGAN KERENDAHAN HATI (IRINGAN MUSIK)</div>

    <div class="speaker-label">WL: Naskah Penyambutan Kasih, Persahabatan &amp; Ajakan Basuh Kaki</div>
    <div class="speaker-text">
      "Teman-teman sekalian, pembasuhan ini merupakan salah satu teladan yang dilakukan oleh Tuhan kita Yesus Kristus kepada para murid yang terkasih. Di sini kami pengurus PERMATA &ndash; segenap keluarga PERMATA &ndash; akan melakukan pembasuhan kaki dari tiap-tiap di antara kamu, sebagai bentuk kami menyambut rasa kasih yang begitu besar dan menjalin persahabatan yang erat di dalam PERMATA Bogor. Agar teman-teman yang nantinya dibasuh kakinya akan terus berdiri bersama dengan Tuhan, berdiri bersama kami, dan mari sama-sama kita mengalami pemulihan dari Tuhan. Semoga apa yang sudah teman-teman doakan tadi dan lewat pembasuhan kaki ini, kita merasakan betapa besarnya kasih Tuhan bagaimana Dia mengampuni kita. Oleh sebab itu, mari adik-adik kami yang akan dibasuh kakinya untuk bisa duduk, dan seluruh setiap dari pengurus PERMATA untuk berada di depan adik-adik atau teman-teman PERMATA lainnya."
    </div>

    <div class="speaker-label">WL: Doa Syukur di Awal Sesi Basuh (Iringan Musik)</div>
    <div class="speaker-text">
      "Kami bersyukur Tuhan untuk menyambut adik-adik kami, teman-teman kami untuk bersama-sama menikmati masa muda dalam PERMATA. Ini kami anak-anak Tuhan, kami butuh Engkau dan kiranya Tuhan berkenan untuk kami saling merangkul."
    </div>

    <div class="callout-yellow">
      <strong>Tim Pembasuh (Pengurus &amp; Kakak Abang):</strong> Berlututlah dengan kedua lutut menapak lantai di hadapan peserta. Siramkan air secara lembut ke kaki mereka, basuh dengan kehangatan kasih, lalu keringkan dengan handuk putih. Sambil membasuh, doakan dalam hati, tatap matanya, dan bisikkan kata berkat personal: <strong>"Dek, kami dan Tuhan menerima kam dengan kerendahan hati apa adanya. Segala bebanmu Tuhan Yesus pulihkan hari ini. Kamu sangat berharga di mata Tuhan, selamat datang di rumah keluarga PERMATA Bogor."</strong>
    </div>

    <div class="song-card">
      <div class="song-header">
        <div class="song-title-group">
          <span class="song-title">5. Sentuh Hatiku</span>
        </div>
        <div class="song-badges">
          <span class="song-badge">Do = G</span>
          <a class="song-yt-link" href="https://www.youtube.com/watch?v=-3cEhTJkiSc" target="_blank">&#9658; YouTube</a>
        </div>
      </div>
      <div class="song-lyrics">
        <strong>[Verse 1]</strong> Betapa kumencintai, segala yang t'lah terjadi &bull; Tak pernah sendiri jalani hidup ini, selalu menyertai<br>
        <strong>[Verse 2]</strong> Betapa kumenyadari, di dalam hidupku ini &bull; Kau s'lalu memberi rancangan terbaik, oleh karena kasih<br>
        <strong>[Chorus]</strong> Bapa, sentuh hatiku, ubah hidupku menjadi yang baru &bull; Bagai emas yang murni, Kau membentuk bejana hatiku<br>
        Bapa, ajarku mengerti sebuah kasih yang selalu memberi &bull; Bagai air mengalir yang tiada pernah berhenti
      </div>
      <div class="song-note">
        (Lagu Sentuh Hatiku diputar solo piano berulang-ulang selama 16.5 menit mengiringi seluruh prosesi pembasuhan kaki hingga tuntas.)
      </div>
    </div>

    <div class="speaker-label">WL: Renungan &amp; Pengantar Doa Penutup di Sela Pembasuhan Kaki</div>
    <div class="speaker-text">
      "Saat air membasuh kakimu, rasakan bagaimana Tuhan dan saudaramu menerimamu dengan kerendahan hati tanpa syarat. Biarlah segala kepahitan masa lalu, rasa minder yang mengekangmu, dan keletihan jiwa dibasuh bersih oleh kasih Yesus. Katakan di dalam lubuk hatimu kepada-Nya: <em>'Bapa, ini hidupku... sentuh hatiku, ubah hidupku menjadi yang baru seturut kehendak-Mu.'</em>"
    </div>

    <div class="dashed-box">
      <strong>&mdash;&mdash;&mdash; DOA PENUTUP PEMBASUHAN OLEH PEMBINA / PENDETA / BP PERMATA BOGOR &mdash;&mdash;&mdash;</strong>
      (Semua peserta dan pengurus berdiri bersama, saling berpegangan tangan erat atau merangkul bahu saudara di sampingnya, menyatukan hati mengucap syukur atas pemulihan dan penerimaan di dalam Kristus.)
    </div>

    <div class="page-footer">
      <span>PEMBASUHAN MAPER PERMATA GBKP BOGOR &bull; RUNDOWN REFLEKTIF</span>
      <span>Halaman 5 dari 6</span>
    </div>
  </div>

  <!-- ================= PAGE 6 ================= -->
  <div class="page">
    <div class="section-bar">IRINGAN MUSIK (TRANSISI MENUJU SUKACITA &amp; PERSEKUTUAN)</div>

    <div class="speaker-label">WL: Deklarasi Sukacita &amp; Sambutan Keluarga Baru PERMATA Bogor</div>
    <div class="speaker-text">
      "Yosua pernah berkata dengan iman teguh: <em>'Tetapi aku dan seisi rumahku, kami akan beribadah kepada TUHAN!'</em> (Yosua 24:15). Kiranya ini pun menjadi meterai komitmen bagi setiap kita yang ada di ruangan ini!<br><br>
      Bagi kita yang sudah dibasuh, hidup kita bukan lagi menjadi orang asing, tetapi hidup kita sudah berjalan bersama dengan yang benar yaitu Kristus Yesus! Yang lama sudah berlalu, sungguh yang baru sudah datang!<br><br>
      Marilah kita bersukacita dan bergembira bersama di PERMATA Bogor! Karena adik-adik kita, teman-teman kita semua sudah resmi bergabung ke dalam PERMATA Bogor dan menjadi keluarga baru kita! Mereka sekarang sudah bersama-sama dengan kita, mari kita bersenang-senang dan bersorak-sorai yang paling meriah bagi Tuhan Yesus!"
    </div>

    <div class="callout-green">
      Semua lampu ruangan dinyalakan TERANG PENUH! Seluruh ruangan bertepuk tangan, bersorak gembira, saling melempar senyum haru, dan berpelukan hangat menyambut anggota baru PERMATA Bogor.
    </div>

    <div class="song-card">
      <div class="song-header">
        <div class="song-title-group">
          <span class="song-title">6. Hari Ini Kurasa Bahagia (Praise Sukacita)</span>
        </div>
        <div class="song-badges">
          <span class="song-badge">Do = F / G</span>
          <a class="song-yt-link" href="https://www.youtube.com/watch?v=_B42EyQ4vdk" target="_blank">&#9658; YouTube</a>
        </div>
      </div>
      <div class="song-lyrics">
        Hari ini kurasa bahagia, berkumpul bersama saudara seiman<br>
        Tuhan Yesus mempersatukan kita, tanpa memandang di antara kita<br>
        <strong>Reff:</strong><br>
        Bergandingan tangan dalam kasih, dalam satu hati, berjalan dalam terang kasih Tuhan<br>
        Kau sahabatku, kau saudaraku, tiada yang dapat memisahkan kita<br>
        Kau sahabatku, kau saudaraku, tiada yang dapat memisahkan kita!
      </div>
    </div>

    <div class="callout-pink">
      <strong>Doa Berkat &amp; Pengurapan (Bilangan 6:24-26 - TB LAI [Terverifikasi]):</strong><br>
      <em>"TUHAN memberkati engkau dan melindungi engkau; TUHAN menyinari engkau dengan wajah-Nya dan memberi engkau kasih karunia; TUHAN menghadapkan wajah-Nya kepadamu dan memberi engkau damai sejahtera."</em>
    </div>

    <div class="callout-lavender">
      <strong>CHECKLIST OPERASIONAL TIM ACARA &amp; FASILITATOR (PERMATA BOGOR):</strong><br>
      &bull; <strong>Tim Air &amp; Perlengkapan:</strong> Pastikan air dalam kendi bersuhu nyaman (hangat kuku bila ruangan dingin), siapkan handuk bersih kering (1 handuk untuk 2-3 peserta), dan kain pel microfiber untuk lantai.<br>
      &bull; <strong>Operator Multimedia &amp; Sound:</strong> Koordinasikan redupnya lampu saat prosesi kendi air masuk, serta pastikan sensitivitas mic menangkap efek gemericik air saat dituangkan ke baskom secara meditatif.<br>
      &bull; <strong>Tim Fasilitator (Kakak-Abang):</strong> Peka terhadap reaksi batin peserta. Dampingi dengan hangat, siapkan tisu bila ada peserta yang menangis haru, dan jangan meninggalkan peserta sendirian.
    </div>

    <div class="soli-deo">&mdash; SOLI DEO GLORIA &bull; PERMATA GBKP RG. BOGOR &mdash;</div>

    <div class="page-footer">
      <span>PEMBASUHAN MAPER PERMATA GBKP BOGOR &bull; RUNDOWN REFLEKTIF</span>
      <span>Halaman 6 dari 6</span>
    </div>
  </div>

</body>
</html>
"""

with open("pembasuhan_maper.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated pembasuhan_maper.html successfully with revised complete lyrics and verified scriptures.")

# Render to PDF via Playwright
html_path = os.path.abspath("pembasuhan_maper.html")
pdf_path = os.path.abspath("Rundown_Detail_Pembasuhan_Maper_60_Menit.pdf")

print("Rendering to PDF via Playwright...")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_path}")
    page.pdf(path=pdf_path, format="A4", print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    browser.close()

print(f"SUCCESS! Rendered {pdf_path} (Size: {os.path.getsize(pdf_path)/1024:.1f} KB)")
