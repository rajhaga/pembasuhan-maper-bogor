# -*- coding: utf-8 -*-
"""
Script to generate the official Seating Plot PDF (A4 Landscape)
for Pembasuhan Kaki MAPER PERMATA GBKP Runggun Bogor.
Grid: 6 Baris ke Belakang x 5 Kolom ke Samping (30 Kursi).
Sisi Kiri: 3 Kolom (Perempuan) | Lorong Tengah | Sisi Kanan: 2 Kolom (Laki-Laki & Pasangan Pendoa).
"""

import os
from playwright.sync_api import sync_playwright

# Data Grid 6 Baris x 5 Kolom
# Rows 1 to 6, Columns 1 to 5
grid_data_6x5 = [
    # Baris 1
    [
        {"seat": "B1-K1", "name": "Natasya Nizura Febina Br Sinulingga", "cd": False, "pendoa": "Barby Maretta", "gen": "P"},
        {"seat": "B1-K2", "name": "Renate Callysta Ginting", "cd": True, "pendoa": "Barby Maretta", "gen": "P"},
        {"seat": "B1-K3", "name": "Melvina Nathania Sembiring", "cd": True, "pendoa": "Barby Maretta", "gen": "P"},
        {"seat": "B1-K4", "name": "Kelvin Immanuel P", "cd": False, "pendoa": "Marshall Bangun", "gen": "L"},
        {"seat": "B1-K5", "name": "Geraldo Oktovian Sinura", "cd": True, "pendoa": "Marshall Bangun", "gen": "L"},
    ],
    # Baris 2
    [
        {"seat": "B2-K1", "name": "Irene Johanna Aginta Sitepu", "cd": True, "pendoa": "Febi Ginting", "gen": "P"},
        {"seat": "B2-K2", "name": "Elsa Natalita br Bangun", "cd": False, "pendoa": "Febi Ginting", "gen": "P"},
        {"seat": "B2-K3", "name": "Kimberly Angelina Kembaren", "cd": False, "pendoa": "Febi Ginting", "gen": "P"},
        {"seat": "B2-K4", "name": "Nathan Bastanta Ginting", "cd": True, "pendoa": "Daniel Tarigan", "gen": "L"},
        {"seat": "B2-K5", "name": "Ryando Alwirasesa Rumbo Sitepu", "cd": False, "pendoa": "Daniel Tarigan", "gen": "L"},
    ],
    # Baris 3
    [
        {"seat": "B3-K1", "name": "Margaretta Br Sembiring Depari", "cd": False, "pendoa": "Lia PK", "gen": "P"},
        {"seat": "B3-K2", "name": "Elvira Faulita", "cd": False, "pendoa": "Lia PK", "gen": "P"},
        {"seat": "B3-K3", "name": "Jessica Lysia Br Tarigan", "cd": False, "pendoa": "Lia PK", "gen": "P"},
        {"seat": "B3-K4", "name": "Hozael Jeremia Sembiring", "cd": False, "pendoa": "Paskal Jesaya Mori Sitepu", "gen": "L"},
        {"seat": "B3-K5", "name": "Dave Berenta Pinem", "cd": False, "pendoa": "Paskal Jesaya Mori Sitepu", "gen": "L"},
    ],
    # Baris 4
    [
        {"seat": "B4-K1", "name": "Chiara Fiorenza Nathania br Pandia", "cd": True, "pendoa": "Winda Meysara", "gen": "P"},
        {"seat": "B4-K2", "name": "Agustina br Ginting", "cd": False, "pendoa": "Winda Meysara", "gen": "P"},
        {"seat": "B4-K3", "name": "Bianca Noella Vemy Ulina Surbakti", "cd": False, "pendoa": "Winda Meysara", "gen": "P"},
        {"seat": "B4-K4", "name": "Setenly Ekel Timanta Sembiring", "cd": False, "pendoa": "Evan PK", "gen": "L"},
        {"seat": "B4-K5", "name": "Gideon Ginting", "cd": False, "pendoa": "Evan PK", "gen": "L"},
    ],
    # Baris 5
    [
        {"seat": "B5-K1", "name": "Judith Serafica Bregina", "cd": True, "pendoa": "Sonya Tarigan", "gen": "P"},
        {"seat": "B5-K2", "name": "Voofea kembaren", "cd": False, "pendoa": "Sonya Tarigan", "gen": "P"},
        {"seat": "B5-K3", "name": "Meka Suriyangi Br Brahmana", "cd": False, "pendoa": "Sonya Tarigan", "gen": "P"},
        {"seat": "B5-K4", "name": "Tiffany Christabel Br Perangin-angin", "cd": False, "pendoa": "Franz Surya Kembaren", "gen": "P"},
        {"seat": "B5-K5", "name": "Cheesya Avira Aurelya Manik", "cd": True, "pendoa": "Franz Surya Kembaren", "gen": "P"},
    ],
    # Baris 6
    [
        {"seat": "B6-K1", "name": "Allegra Luweenda Surbakti", "cd": False, "pendoa": "Winna Amelia Sembiring", "gen": "P"},
        {"seat": "B6-K2", "name": "Nicole Alvara Larasati Ginting", "cd": False, "pendoa": "Winna Amelia Sembiring", "gen": "P"},
        {"seat": "B6-K3", "name": "Aurel Anastasya Sinulingga", "cd": False, "pendoa": "Winna Amelia Sembiring", "gen": "P"},
        {"seat": "B6-K4", "name": "Agitta Ria br Tarigan", "cd": True, "pendoa": "Marvel banngun", "gen": "P"},
        {"seat": "B6-K5", "name": "Bellian Casey Ginting", "cd": True, "pendoa": "Marvel banngun", "gen": "L"},
    ],
]

# Rekap Wilayah Tugas Pendoa (Satu Baris Penuh Bersama)
pendoa_summary = [
    {"pendoa": "Barby Maretta", "baris": "Baris 1 (Kiri)", "target": "3 Wanita", "seats": ["B1-K1 (Natasya)", "B1-K2 (Renate [CD])", "B1-K3 (Melvina [CD])"]},
    {"pendoa": "Marshall Bangun", "baris": "Baris 1 (Kanan)", "target": "2 Pria", "seats": ["B1-K4 (Kelvin)", "B1-K5 (Geraldo [CD])"]},
    {"pendoa": "Febi Ginting", "baris": "Baris 2 (Kiri)", "target": "3 Wanita", "seats": ["B2-K1 (Irene [CD])", "B2-K2 (Elsa)", "B2-K3 (Kimberly)"]},
    {"pendoa": "Daniel Tarigan", "baris": "Baris 2 (Kanan)", "target": "2 Pria", "seats": ["B2-K4 (Nathan [CD])", "B2-K5 (Ryando)"]},
    {"pendoa": "Lia PK", "baris": "Baris 3 (Kiri)", "target": "3 Wanita", "seats": ["B3-K1 (Margaretta)", "B3-K2 (Elvira)", "B3-K3 (Jessica)"]},
    {"pendoa": "Paskal Jesaya Mori Sitepu", "baris": "Baris 3 (Kanan)", "target": "2 Pria", "seats": ["B3-K4 (Hozael)", "B3-K5 (Dave)"]},
    {"pendoa": "Winda Meysara", "baris": "Baris 4 (Kiri)", "target": "3 Wanita", "seats": ["B4-K1 (Chiara [CD])", "B4-K2 (Agustina)", "B4-K3 (Bianca)"]},
    {"pendoa": "Evan PK", "baris": "Baris 4 (Kanan)", "target": "2 Pria", "seats": ["B4-K4 (Setenly)", "B4-K5 (Gideon)"]},
    {"pendoa": "Sonya Tarigan", "baris": "Baris 5 (Kiri)", "target": "3 Wanita", "seats": ["B5-K1 (Judith [CD])", "B5-K2 (Voofea)", "B5-K3 (Meka)"]},
    {"pendoa": "Franz Surya Kembaren", "baris": "Baris 5 (Kanan)", "target": "2 Wanita", "seats": ["B5-K4 (Tiffany)", "B5-K5 (Cheesya [CD])"]},
    {"pendoa": "Winna Amelia Sembiring", "baris": "Baris 6 (Kiri)", "target": "3 Wanita", "seats": ["B6-K1 (Allegra)", "B6-K2 (Nicole)", "B6-K3 (Aurel)"]},
    {"pendoa": "Marvel banngun", "baris": "Baris 6 (Kanan)", "target": "1 Wanita + 1 Pria", "seats": ["B6-K4 (Agitta [CD])", "B6-K5 (Bellian [CD])"]},
]

def render_html():
    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Denah & Plotting Tempat Duduk Pembasuhan MAPER (6 Baris x 5 Kolom)</title>
  <style>
    @page {{
      size: A4 landscape;
      margin: 0;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
      color: #1e293b;
      background: #ffffff;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    .page {{
      width: 297mm;
      height: 210mm;
      padding: 7mm 11mm 6mm 11mm;
      position: relative;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: #ffffff;
    }}

    /* Header */
    .header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #1e3a8a;
      padding-bottom: 3px;
      margin-bottom: 4px;
    }}
    .header-left .tag {{
      font-size: 7pt;
      font-weight: 700;
      color: #2563eb;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .header-left .title {{
      font-size: 13pt;
      font-weight: 800;
      color: #0f172a;
      margin: 0;
      text-transform: uppercase;
      letter-spacing: -0.2px;
    }}
    .header-left .subtitle {{
      font-size: 7.6pt;
      color: #475569;
      font-weight: 600;
    }}
    .header-badges {{
      display: flex;
      gap: 5px;
    }}
    .h-badge {{
      padding: 2.5px 7px;
      border-radius: 4px;
      font-size: 7.2pt;
      font-weight: 700;
    }}
    .h-badge-female {{
      background: #fdf2f8;
      border: 1px solid #f472b6;
      color: #9d174d;
    }}
    .h-badge-male {{
      background: #eff6ff;
      border: 1px solid #60a5fa;
      color: #1e40af;
    }}
    .h-badge-cd {{
      background: #fefce8;
      border: 1px solid #facc15;
      color: #854d0e;
    }}

    /* Stage Banner */
    .stage-banner {{
      background: linear-gradient(135deg, #1e3a8a, #0284c7);
      color: #ffffff;
      text-align: center;
      padding: 3.5px 0;
      font-size: 8pt;
      font-weight: 800;
      letter-spacing: 1.5px;
      border-radius: 4px;
      margin-bottom: 4px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.08);
    }}

    /* Grid layout */
    .grid-container {{
      display: flex;
      flex-direction: column;
      gap: 3.5px;
      flex-grow: 1;
    }}
    .grid-row {{
      display: grid;
      grid-template-columns: 26mm 1fr 1fr 1fr 8mm 1fr 1fr;
      gap: 4px;
      align-items: stretch;
    }}
    .row-header-label {{
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 2px;
      font-size: 6.8pt;
      font-weight: 700;
      color: #334155;
    }}
    .row-header-label strong {{
      font-size: 8.2pt;
      color: #0f172a;
    }}

    .aisle-divider {{
      display: flex;
      justify-content: center;
      align-items: center;
      writing-mode: vertical-rl;
      text-orientation: mixed;
      font-size: 5.5pt;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #64748b;
      background: #f8fafc;
      border: 1px dashed #cbd5e1;
      border-radius: 3px;
    }}

    /* Seat Card */
    .seat-card {{
      border-radius: 4px;
      padding: 3px 5px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1.2px solid #cbd5e1;
      position: relative;
      background: #ffffff;
      min-height: 20mm;
    }}
    .seat-card.female {{
      background: #fdf2f8;
      border-color: #fbcfe8;
    }}
    .seat-card.male {{
      background: #eff6ff;
      border-color: #bfdbfe;
    }}

    .seat-card-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5px;
    }}
    .seat-id {{
      font-size: 6.6pt;
      font-weight: 800;
      color: #475569;
    }}
    .seat-badges {{
      display: flex;
      gap: 3px;
    }}
    .badge-gen {{
      font-size: 5.8pt;
      font-weight: 800;
      padding: 0.5px 3.5px;
      border-radius: 3px;
    }}
    .badge-gen.female {{
      background: #f472b6;
      color: #ffffff;
    }}
    .badge-gen.male {{
      background: #3b82f6;
      color: #ffffff;
    }}
    .badge-cd {{
      background: #facc15;
      color: #713f12;
      font-size: 5.8pt;
      font-weight: 800;
      padding: 0.5px 3.5px;
      border-radius: 3px;
      letter-spacing: 0.3px;
    }}

    .participant-name {{
      font-size: 7.3pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.18;
      margin: 1.5px 0 2px 0;
      word-break: break-word;
    }}
    .female .participant-name {{
      color: #831843;
    }}
    .male .participant-name {{
      color: #1e3a8a;
    }}

    .pendoa-info {{
      font-size: 6.4pt;
      color: #334155;
      background: rgba(255, 255, 255, 0.75);
      border-radius: 3px;
      padding: 1px 3px;
      border: 1px dotted #cbd5e1;
      margin-top: auto;
      line-height: 1.15;
    }}
    .pendoa-info strong {{
      color: #0f172a;
    }}

    /* Column Headers at top */
    .col-header-row {{
      display: grid;
      grid-template-columns: 26mm 1fr 1fr 1fr 8mm 1fr 1fr;
      gap: 4px;
      margin-bottom: 2px;
      text-align: center;
      font-size: 6.8pt;
      font-weight: 800;
      color: #475569;
    }}
    .col-header-box {{
      background: #e2e8f0;
      padding: 2px 0;
      border-radius: 3px;
    }}
    .col-header-box.female-header {{
      background: #fce7f3;
      color: #9d174d;
    }}
    .col-header-box.male-header {{
      background: #dbeafe;
      color: #1e40af;
    }}

    /* Footer */
    .page-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid #cbd5e1;
      padding-top: 2.5px;
      font-size: 6.6pt;
      color: #64748b;
      margin-top: 3px;
    }}

    /* Page 2 Styles (Directory Table) */
    .table-section {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 12px;
      flex-grow: 1;
    }}
    .sub-table-title {{
      font-size: 8.2pt;
      font-weight: 800;
      color: #1e3a8a;
      text-transform: uppercase;
      margin: 0 0 3.5px 0;
      border-bottom: 1.5px solid #1e3a8a;
      padding-bottom: 2px;
    }}
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 6.5pt;
    }}
    table.data-table th {{
      background: #1e3a8a;
      color: #ffffff;
      padding: 2.5px 4px;
      text-align: left;
      font-weight: 700;
      font-size: 6.4pt;
    }}
    table.data-table td {{
      padding: 2px 4px;
      border-bottom: 1px solid #e2e8f0;
      color: #1e293b;
    }}
    table.data-table tr:nth-child(even) {{
      background: #f8fafc;
    }}
    table.data-table tr.highlight-pria {{
      background: #eff6ff;
    }}
    .badge-cd-sm {{
      background: #fef08a;
      color: #854d0e;
      font-weight: 800;
      padding: 0 3px;
      border-radius: 2px;
      font-size: 5.8pt;
    }}

    .card-rekap {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      padding: 3.5px 6.5px;
      margin-bottom: 3.5px;
    }}
    .card-rekap-title {{
      font-size: 7pt;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      justify-content: space-between;
      margin-bottom: 1.5px;
    }}
    .card-rekap-body {{
      font-size: 6.4pt;
      color: #334155;
      line-height: 1.25;
    }}
  </style>
</head>
<body>

  <!-- ==================== HALAMAN 1: DENAH VISUAL 6 BARIS X 5 KOLOM ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-left">
        <div class="tag">PERMATA GBKP RUNGGUN BOGOR &bull; MAPER 2026</div>
        <div class="title">DENAH &amp; PLOTTING TEMPAT DUDUK PEMBASUHAN KAKI</div>
        <div class="subtitle">Grid Ruangan 6 Baris &times; 5 Kolom &bull; Total 30 Peserta (21 Perempuan &bull; 9 Laki-Laki)</div>
      </div>
      <div class="header-badges">
        <span class="h-badge h-badge-female">&female; KIRI: PEREMPUAN (21)</span>
        <span class="h-badge h-badge-male">&male; KANAN: LAKI-LAKI (9)</span>
        <span class="h-badge h-badge-cd">&star; CD: 10 PESERTA</span>
      </div>
    </div>

    <!-- PANGGUNG / MIMBAR -->
    <div class="stage-banner">
      &uarr; &uarr; PANGGUNG DEPAN &bull; MIMBAR &bull; SALIB &bull; PROSESI KENDI AIR PEMBASUHAN &uarr; &uarr;
    </div>

    <!-- KOLOM HEADER -->
    <div class="col-header-row">
      <div>POSISI BARIS</div>
      <div class="col-header-box female-header">KOLOM 1 (P)</div>
      <div class="col-header-box female-header">KOLOM 2 (P)</div>
      <div class="col-header-box female-header">KOLOM 3 (P)</div>
      <div class="col-header-box" style="background:transparent; color:#94a3b8;">&bull;</div>
      <div class="col-header-box male-header">KOLOM 4 (L/P)</div>
      <div class="col-header-box male-header">KOLOM 5 (L)</div>
    </div>

    <!-- 6 ROWS GRID -->
    <div class="grid-container">
"""

    row_names = [
        "BARIS 1<br><span style='font-size:5.5pt; font-weight:normal; color:#64748b;'>Terdepan</span>",
        "BARIS 2<br><span style='font-size:5.5pt; font-weight:normal; color:#64748b;'>Baris Kedua</span>",
        "BARIS 3<br><span style='font-size:5.5pt; font-weight:normal; color:#64748b;'>Baris Ketiga</span>",
        "BARIS 4<br><span style='font-size:5.5pt; font-weight:normal; color:#64748b;'>Baris Keempat</span>",
        "BARIS 5<br><span style='font-size:5.5pt; font-weight:normal; color:#64748b;'>Baris Kelima</span>",
        "BARIS 6<br><span style='font-size:5.5pt; font-weight:normal; color:#64748b;'>Paling Belakang</span>",
    ]

    for r_idx, row in enumerate(grid_data_6x5):
        html += f"""
      <div class="grid-row">
        <div class="row-header-label">
          <strong>{row_names[r_idx]}</strong>
        </div>
"""
        # Kolom 1 to 3 (Sisi Kiri: 3 Kursi Perempuan)
        for c in range(3):
            item = row[c]
            gen_class = "female" if item["gen"] == "P" else "male"
            gen_label = "P" if item["gen"] == "P" else "L"
            cd_html = '<span class="badge-cd">CD</span>' if item["cd"] else ''
            html += f"""
        <div class="seat-card {gen_class}">
          <div class="seat-card-top">
            <span class="seat-id">{item['seat']}</span>
            <div class="seat-badges">
              {cd_html}
              <span class="badge-gen {gen_class}">{gen_label}</span>
            </div>
          </div>
          <div class="participant-name">{item['name']}</div>
          <div class="pendoa-info">Pendoa: <strong>{item['pendoa']}</strong></div>
        </div>
"""
        # Lorong Tengah
        html += """
        <div class="aisle-divider">LORONG</div>
"""
        # Kolom 4 & 5 (Sisi Kanan: 2 Kursi Pria / Pendoa)
        for c in range(3, 5):
            item = row[c]
            gen_class = "female" if item["gen"] == "P" else "male"
            gen_label = "P" if item["gen"] == "P" else "L"
            cd_html = '<span class="badge-cd">CD</span>' if item["cd"] else ''
            html += f"""
        <div class="seat-card {gen_class}">
          <div class="seat-card-top">
            <span class="seat-id">{item['seat']}</span>
            <div class="seat-badges">
              {cd_html}
              <span class="badge-gen {gen_class}">{gen_label}</span>
            </div>
          </div>
          <div class="participant-name">{item['name']}</div>
          <div class="pendoa-info">Pendoa: <strong>{item['pendoa']}</strong></div>
        </div>
"""
        html += """
      </div>
"""

    html += """
    </div>

    <div class="page-footer">
      <span>PERMATA GBKP RUNGGUN BOGOR &bull; MAPER 2026 &bull; PLOTTING TEMPAT DUDUK PEMBASUHAN</span>
      <span>Kiri: Perempuan (Pink) &bull; Kanan: Laki-Laki (Biru) &bull; Emas: Peserta CD &bull; Halaman 1 dari 2</span>
    </div>
  </div>

  <!-- ==================== HALAMAN 2: DIREKTORI LENGKAP & REKAP PENDOA ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-left">
        <div class="tag">PERMATA GBKP RUNGGUN BOGOR &bull; PANDUAN PENGURUS &amp; USHER</div>
        <div class="title">TABEL DIREKTORI LENGKAP PESERTA &amp; REKAP WILAYAH PENDOA</div>
        <div class="subtitle">Layout 6 Baris &times; 5 Kolom &bull; Adik Bimbingan Duduk Berdampingan di Baris yang Sama</div>
      </div>
      <div class="header-badges">
        <span class="h-badge h-badge-female">21 Perempuan</span>
        <span class="h-badge h-badge-male">9 Laki-Laki</span>
        <span class="h-badge h-badge-cd">12 Pendoa</span>
      </div>
    </div>

    <div class="table-section">
      <!-- Kolom Kiri: Tabel 30 Peserta -->
      <div>
        <div class="sub-table-title">Daftar 30 Peserta Menurut Posisi Kursi (6 Baris x 5 Kolom)</div>
        <table class="data-table">
          <thead>
            <tr>
              <th style="width:18px;">No</th>
              <th style="width:36px;">Kursi</th>
              <th>Nama Lengkap Peserta</th>
              <th style="width:24px; text-align:center;">G</th>
              <th style="width:26px; text-align:center;">Ket</th>
              <th>Pendoa / Pembasuh</th>
            </tr>
          </thead>
          <tbody>
"""

    count = 1
    for r in grid_data_6x5:
        for item in r:
            row_highlight = 'class="highlight-pria"' if item["gen"] == "L" else ''
            cd_badge = '<span class="badge-cd-sm">CD</span>' if item["cd"] else '-'
            html += f"""
            <tr {row_highlight}>
              <td style="text-align:center;">{count}</td>
              <td style="font-weight:700;">{item['seat']}</td>
              <td><strong>{item['name']}</strong></td>
              <td style="text-align:center;">{item['gen']}</td>
              <td style="text-align:center;">{cd_badge}</td>
              <td>{item['pendoa']}</td>
            </tr>
"""
            count += 1

    html += """
          </tbody>
        </table>
      </div>

      <!-- Kolom Kanan: Rekap Pendoa -->
      <div>
        <div class="sub-table-title">Rekap Wilayah Tugas Pendoa / Pembasuh</div>
"""

    for p in pendoa_summary:
        seats_str = " &bull; ".join(p["seats"])
        html += f"""
        <div class="card-rekap">
          <div class="card-rekap-title">
            <span>👤 {p['pendoa']}</span>
            <span style="color:#2563eb; font-weight:700;">{p['baris']} &bull; {p['target']}</span>
          </div>
          <div class="card-rekap-body">
            <strong>Posisi Duduk Adik:</strong><br>{seats_str}
          </div>
        </div>
"""

    html += """
        <div style="background:#fef9c3; border-left:3px solid #eab308; padding:4px 7px; border-radius:3px; font-size:6.4pt; color:#713f12; margin-top:5px; line-height:1.25;">
          💡 <strong>Petunjuk Khusus Tim Pendoa (Layout 6x5):</strong><br>
          Semua peserta yang didoakan oleh pendoa yang sama duduk <strong>100% berdampingan dalam satu baris yang sama</strong>. Pendoa cukup melayani langsung di barisannya tanpa perlu berpindah-pindah baris.
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>PERMATA GBKP RUNGGUN BOGOR &bull; MAPER 2026 &bull; PLOTTING TEMPAT DUDUK PEMBASUHAN</span>
      <span>Soli Deo Gloria &bull; Halaman 2 dari 2</span>
    </div>
  </div>

</body>
</html>
"""
    return html

html_content = render_html()
html_file = "ploting_tempat_duduk.html"
pdf_file = "Ploting_Tempat_Duduk_Pembasuhan_MAPER_Bogor.pdf"

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {html_file}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{os.path.abspath(html_file)}")
    page.pdf(
        path=pdf_file,
        format="A4",
        landscape=True,
        print_background=True,
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
    )
    browser.close()

size_kb = os.path.getsize(pdf_file) / 1024
print(f"SUCCESS! Rendered {pdf_file} ({size_kb:.1f} KB)")
