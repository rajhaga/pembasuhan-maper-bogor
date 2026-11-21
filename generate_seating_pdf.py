# -*- coding: utf-8 -*-
"""
Script to generate the official Seating Plot PDF (A4 Landscape)
for Pembasuhan Kaki MAPER PERMATA GBKP Runggun Bogor.
Grid: 6 Baris ke Belakang x 5 Kolom ke Samping (30 Kursi).
Memuat PLOTTING PENDOA (Sesi 5) dan PLOTTING PEMBASUH (Sesi 10).
Segregasi Gender 100%: Laki-laki membasuh Laki-laki, Perempuan membasuh Perempuan.
"""

import os
from playwright.sync_api import sync_playwright

# Data Grid 6 Baris x 5 Kolom (30 Peserta)
# Rows 1 to 6, Columns 1 to 5
grid_data_6x5 = [
    # Baris 1
    [
        {"seat": "B1-K1", "name": "Natasya Nizura Febina Br Sinulingga", "cd": False, "pendoa": "Barby Maretta", "pembasuh": "dea", "gen": "P"},
        {"seat": "B1-K2", "name": "Renate Callysta Ginting", "cd": True, "pendoa": "Barby Maretta", "pembasuh": "dea", "gen": "P"},
        {"seat": "B1-K3", "name": "Melvina Nathania Sembiring", "cd": True, "pendoa": "Barby Maretta", "pembasuh": "dea", "gen": "P"},
        {"seat": "B1-K4", "name": "Kelvin Immanuel P", "cd": False, "pendoa": "Marshall Bangun", "pembasuh": "raj", "gen": "L"},
        {"seat": "B1-K5", "name": "Geraldo Oktovian Sinura", "cd": True, "pendoa": "Marshall Bangun", "pembasuh": "raj", "gen": "L"},
    ],
    # Baris 2
    [
        {"seat": "B2-K1", "name": "Irene Johanna Aginta Sitepu", "cd": True, "pendoa": "Febi Ginting", "pembasuh": "cindy", "gen": "P"},
        {"seat": "B2-K2", "name": "Elsa Natalita br Bangun", "cd": False, "pendoa": "Febi Ginting", "pembasuh": "cindy", "gen": "P"},
        {"seat": "B2-K3", "name": "Kimberly Angelina Kembaren", "cd": False, "pendoa": "Febi Ginting", "pembasuh": "cindy", "gen": "P"},
        {"seat": "B2-K4", "name": "Setenly Ekel Timanta Sembiring", "cd": False, "pendoa": "Evan PK", "pembasuh": "raj", "gen": "L"},
        {"seat": "B2-K5", "name": "Hozael Jeremia Sembiring", "cd": False, "pendoa": "Paskal Jesaya Mori Sitepu", "pembasuh": "raj", "gen": "L"},
    ],
    # Baris 3
    [
        {"seat": "B3-K1", "name": "Margaretta Br Sembiring Depari", "cd": False, "pendoa": "Lia PK", "pembasuh": "chantika", "gen": "P"},
        {"seat": "B3-K2", "name": "Elvira Faulita", "cd": False, "pendoa": "Lia PK", "pembasuh": "chantika", "gen": "P"},
        {"seat": "B3-K3", "name": "Jessica Lysia Br Tarigan", "cd": False, "pendoa": "Lia PK", "pembasuh": "chantika", "gen": "P"},
        {"seat": "B3-K4", "name": "Dave Berenta Pinem", "cd": False, "pendoa": "Paskal Jesaya Mori Sitepu", "pembasuh": "amori", "gen": "L"},
        {"seat": "B3-K5", "name": "Nathan Bastanta Ginting", "cd": True, "pendoa": "Daniel Tarigan", "pembasuh": "amori", "gen": "L"},
    ],
    # Baris 4
    [
        {"seat": "B4-K1", "name": "Chiara Fiorenza Nathania br Pandia", "cd": True, "pendoa": "Winda Meysara", "pembasuh": "yohebet", "gen": "P"},
        {"seat": "B4-K2", "name": "Agustina br Ginting", "cd": False, "pendoa": "Winda Meysara", "pembasuh": "yohebet", "gen": "P"},
        {"seat": "B4-K3", "name": "Aurel Anastasya Sinulingga", "cd": False, "pendoa": "Winna Amelia Sembiring", "pembasuh": "yohebet", "gen": "P"},
        {"seat": "B4-K4", "name": "Ryando Alwirasesa Rumbo Sitepu", "cd": False, "pendoa": "Daniel Tarigan", "pembasuh": "amori", "gen": "L"},
        {"seat": "B4-K5", "name": "Bellian Casey Ginting", "cd": True, "pendoa": "Marvel banngun", "pembasuh": "amori", "gen": "L"},
    ],
    # Baris 5
    [
        {"seat": "B5-K1", "name": "Bianca Noella Vemy Ulina Surbakti", "cd": False, "pendoa": "Winda Meysara", "pembasuh": "leora", "gen": "P"},
        {"seat": "B5-K2", "name": "Allegra Luweenda Surbakti", "cd": False, "pendoa": "Winna Amelia Sembiring", "pembasuh": "leora", "gen": "P"},
        {"seat": "B5-K3", "name": "Nicole Alvara Larasati Ginting", "cd": False, "pendoa": "Winna Amelia Sembiring", "pembasuh": "leora", "gen": "P"},
        {"seat": "B5-K4", "name": "Gideon Ginting", "cd": False, "pendoa": "Evan PK", "pembasuh": "amori", "gen": "L"},
        {"seat": "B5-K5", "name": "Tiffany Christabel Br Perangin-angin", "cd": False, "pendoa": "Franz Surya Kembaren", "pembasuh": "ella", "gen": "P"},
    ],
    # Baris 6
    [
        {"seat": "B6-K1", "name": "Judith Serafica Bregina", "cd": True, "pendoa": "Sonya Tarigan", "pembasuh": "audrey", "gen": "P"},
        {"seat": "B6-K2", "name": "Voofea kembaren", "cd": False, "pendoa": "Sonya Tarigan", "pembasuh": "audrey", "gen": "P"},
        {"seat": "B6-K3", "name": "Meka Suriyangi Br Brahmana", "cd": False, "pendoa": "Sonya Tarigan", "pembasuh": "audrey", "gen": "P"},
        {"seat": "B6-K4", "name": "Agitta Ria br Tarigan", "cd": True, "pendoa": "Marvel banngun", "pembasuh": "ella", "gen": "P"},
        {"seat": "B6-K5", "name": "Cheesya Avira Aurelya Manik", "cd": True, "pendoa": "Franz Surya Kembaren", "pembasuh": "ella", "gen": "P"},
    ],
]

# Rekap Pembasuh (Sesi 10)
pembasuh_summary = [
    # Pria
    {"pembasuh": "raj", "gen": "Laki-Laki", "jumlah": "4 Peserta (L)", "kursi": ["B1-K4 (Kelvin)", "B1-K5 (Geraldo [CD])", "B2-K4 (Setenly)", "B2-K5 (Hozael)"], "area": "Baris 1 & 2 (Kanan)"},
    {"pembasuh": "amori", "gen": "Laki-Laki", "jumlah": "5 Peserta (L)", "kursi": ["B3-K4 (Dave)", "B3-K5 (Nathan [CD])", "B4-K4 (Ryando)", "B4-K5 (Bellian [CD])", "B5-K4 (Gideon)"], "area": "Baris 3, 4, 5 (Kanan)"},
    # Wanita
    {"pembasuh": "dea", "gen": "Perempuan", "jumlah": "3 Peserta (P)", "kursi": ["B1-K1 (Natasya)", "B1-K2 (Renate [CD])", "B1-K3 (Melvina [CD])"], "area": "Baris 1 (Kiri)"},
    {"pembasuh": "cindy", "gen": "Perempuan", "jumlah": "3 Peserta (P)", "kursi": ["B2-K1 (Irene [CD])", "B2-K2 (Elsa)", "B2-K3 (Kimberly)"], "area": "Baris 2 (Kiri)"},
    {"pembasuh": "chantika", "gen": "Perempuan", "jumlah": "3 Peserta (P)", "kursi": ["B3-K1 (Margaretta)", "B3-K2 (Elvira)", "B3-K3 (Jessica)"], "area": "Baris 3 (Kiri)"},
    {"pembasuh": "yohebet", "gen": "Perempuan", "jumlah": "3 Peserta (P)", "kursi": ["B4-K1 (Chiara [CD])", "B4-K2 (Agustina)", "B4-K3 (Aurel)"], "area": "Baris 4 (Kiri)"},
    {"pembasuh": "leora", "gen": "Perempuan", "jumlah": "3 Peserta (P)", "kursi": ["B5-K1 (Bianca)", "B5-K2 (Allegra)", "B5-K3 (Nicole)"], "area": "Baris 5 (Kiri)"},
    {"pembasuh": "audrey", "gen": "Perempuan", "jumlah": "3 Peserta (P)", "kursi": ["B6-K1 (Judith [CD])", "B6-K2 (Voofea)", "B6-K3 (Meka)"], "area": "Baris 6 (Kiri)"},
    {"pembasuh": "ella", "gen": "Perempuan", "jumlah": "3 Peserta (P)", "kursi": ["B5-K5 (Tiffany)", "B6-K4 (Agitta [CD])", "B6-K5 (Cheesya [CD])"], "area": "Baris 5 & 6 (Kanan)"},
]

# Rekap Pendoa (Sesi 5)
pendoa_summary = [
    {"pendoa": "Barby Maretta", "baris": "Baris 1 (Kiri)", "target": "3 Wanita", "seats": ["B1-K1 (Natasya)", "B1-K2 (Renate [CD])", "B1-K3 (Melvina [CD])"]},
    {"pendoa": "Marshall Bangun", "baris": "Baris 1 (Kanan)", "target": "2 Pria", "seats": ["B1-K4 (Kelvin)", "B1-K5 (Geraldo [CD])"]},
    {"pendoa": "Febi Ginting", "baris": "Baris 2 (Kiri)", "target": "3 Wanita", "seats": ["B2-K1 (Irene [CD])", "B2-K2 (Elsa)", "B2-K3 (Kimberly)"]},
    {"pendoa": "Lia PK", "baris": "Baris 3 (Kiri)", "target": "3 Wanita", "seats": ["B3-K1 (Margaretta)", "B3-K2 (Elvira)", "B3-K3 (Jessica)"]},
    {"pendoa": "Paskal Jesaya Mori Sitepu", "baris": "Baris 2 & 3 (Kanan)", "target": "2 Pria", "seats": ["B2-K5 (Hozael)", "B3-K4 (Dave)"]},
    {"pendoa": "Daniel Tarigan", "baris": "Baris 3 & 4 (Kanan)", "target": "2 Pria", "seats": ["B3-K5 (Nathan [CD])", "B4-K4 (Ryando)"]},
    {"pendoa": "Evan PK", "baris": "Baris 2 & 5 (Kanan)", "target": "2 Pria", "seats": ["B2-K4 (Setenly)", "B5-K4 (Gideon)"]},
    {"pendoa": "Winda Meysara", "baris": "Baris 4 & 5 (Kiri)", "target": "3 Wanita", "seats": ["B4-K1 (Chiara [CD])", "B4-K2 (Agustina)", "B5-K1 (Bianca)"]},
    {"pendoa": "Winna Amelia Sembiring", "baris": "Baris 4 & 5 (Kiri)", "target": "3 Wanita", "seats": ["B4-K3 (Aurel)", "B5-K2 (Allegra)", "B5-K3 (Nicole)"]},
    {"pendoa": "Sonya Tarigan", "baris": "Baris 6 (Kiri)", "target": "3 Wanita", "seats": ["B6-K1 (Judith [CD])", "B6-K2 (Voofea)", "B6-K3 (Meka)"]},
    {"pendoa": "Franz Surya Kembaren", "baris": "Baris 5 & 6 (Kanan)", "target": "2 Wanita", "seats": ["B5-K5 (Tiffany)", "B6-K5 (Cheesya [CD])"]},
    {"pendoa": "Marvel banngun", "baris": "Baris 4 & 6 (Kanan)", "target": "1 Pria + 1 Wanita", "seats": ["B4-K5 (Bellian [CD])", "B6-K4 (Agitta [CD])"]},
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
      padding: 6mm 10mm 5mm 10mm;
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
      padding-bottom: 2.5px;
      margin-bottom: 3.5px;
    }}
    .header-left .tag {{
      font-size: 6.8pt;
      font-weight: 700;
      color: #2563eb;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .header-left .title {{
      font-size: 12.5pt;
      font-weight: 800;
      color: #0f172a;
      margin: 0;
      text-transform: uppercase;
      letter-spacing: -0.2px;
      line-height: 1.1;
    }}
    .header-left .subtitle {{
      font-size: 7.2pt;
      color: #475569;
      font-weight: 600;
    }}
    .header-badges {{
      display: flex;
      gap: 5px;
    }}
    .h-badge {{
      padding: 2.5px 6.5px;
      border-radius: 4px;
      font-size: 6.8pt;
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
      padding: 3px 0;
      font-size: 7.5pt;
      font-weight: 800;
      letter-spacing: 1.2px;
      border-radius: 4px;
      margin-bottom: 3.5px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.06);
    }}

    /* Grid layout */
    .grid-container {{
      display: flex;
      flex-direction: column;
      gap: 3px;
      flex-grow: 1;
    }}
    .grid-row {{
      display: grid;
      grid-template-columns: 24mm 1fr 1fr 1fr 7mm 1fr 1fr;
      gap: 3.5px;
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
      font-size: 6.5pt;
      font-weight: 700;
      color: #334155;
    }}
    .row-header-label strong {{
      font-size: 7.8pt;
      color: #0f172a;
    }}

    .aisle-divider {{
      display: flex;
      justify-content: center;
      align-items: center;
      writing-mode: vertical-rl;
      text-orientation: mixed;
      font-size: 5.2pt;
      font-weight: 700;
      letter-spacing: 1px;
      color: #64748b;
      background: #f8fafc;
      border: 1px dashed #cbd5e1;
      border-radius: 3px;
    }}

    /* Seat Card */
    .seat-card {{
      border-radius: 4px;
      padding: 2.5px 4.5px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1.2px solid #cbd5e1;
      position: relative;
      background: #ffffff;
      min-height: 22mm;
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
      margin-bottom: 1px;
    }}
    .seat-id {{
      font-size: 6.4pt;
      font-weight: 800;
      color: #475569;
    }}
    .seat-badges {{
      display: flex;
      gap: 2.5px;
    }}
    .badge-gen {{
      font-size: 5.5pt;
      font-weight: 800;
      padding: 0.5px 3px;
      border-radius: 2.5px;
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
      font-size: 5.5pt;
      font-weight: 800;
      padding: 0.5px 3px;
      border-radius: 2.5px;
      letter-spacing: 0.2px;
    }}

    .participant-name {{
      font-size: 7.1pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.15;
      margin: 1px 0 2px 0;
      word-break: break-word;
    }}
    .female .participant-name {{
      color: #831843;
    }}
    .male .participant-name {{
      color: #1e3a8a;
    }}

    /* Roles Section on Seat Card */
    .roles-container {{
      display: flex;
      flex-direction: column;
      gap: 1.5px;
      margin-top: auto;
    }}
    .role-row {{
      display: flex;
      align-items: center;
      padding: 1px 3.5px;
      border-radius: 2.5px;
      font-size: 5.7pt;
      line-height: 1.15;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(0, 0, 0, 0.06);
    }}
    .role-row.pendoa-row {{
      border-left: 2.5px solid #6366f1;
    }}
    .role-row.pembasuh-row {{
      border-left: 2.5px solid #0284c7;
      background: #f0fdfa;
    }}
    .role-label {{
      font-weight: 700;
      color: #475569;
      width: 44px;
      flex-shrink: 0;
      font-size: 5.3pt;
      text-transform: uppercase;
    }}
    .role-value {{
      font-weight: 700;
      color: #0f172a;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .role-row.pembasuh-row .role-value {{
      color: #0369a1;
      text-transform: uppercase;
    }}

    /* Column Headers at top */
    .col-header-row {{
      display: grid;
      grid-template-columns: 24mm 1fr 1fr 1fr 7mm 1fr 1fr;
      gap: 3.5px;
      margin-bottom: 2px;
      text-align: center;
      font-size: 6.5pt;
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
      padding-top: 2px;
      font-size: 6.3pt;
      color: #64748b;
      margin-top: 2.5px;
    }}

    /* Page 2 Styles (Directory Table) */
    .table-section {{
      display: grid;
      grid-template-columns: 1.22fr 0.78fr;
      gap: 10px;
      flex-grow: 1;
    }}
    .sub-table-title {{
      font-size: 7.8pt;
      font-weight: 800;
      color: #1e3a8a;
      text-transform: uppercase;
      margin: 0 0 3px 0;
      border-bottom: 1.5px solid #1e3a8a;
      padding-bottom: 2px;
      display: flex;
      justify-content: space-between;
    }}
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 6.2pt;
    }}
    table.data-table th {{
      background: #1e3a8a;
      color: #ffffff;
      padding: 2.2px 3.5px;
      text-align: left;
      font-weight: 700;
      font-size: 6.2pt;
    }}
    table.data-table td {{
      padding: 1.8px 3.5px;
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
      font-size: 5.6pt;
    }}
    .badge-pembasuh {{
      background: #e0f2fe;
      color: #0369a1;
      font-weight: 800;
      padding: 0.5px 3.5px;
      border-radius: 2px;
      font-size: 5.8pt;
      text-transform: uppercase;
      display: inline-block;
    }}

    .card-rekap {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 3.5px;
      padding: 2.8px 5px;
      margin-bottom: 2.5px;
    }}
    .card-rekap-title {{
      font-size: 6.6pt;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      justify-content: space-between;
      margin-bottom: 1px;
    }}
    .card-rekap-body {{
      font-size: 5.9pt;
      color: #334155;
      line-height: 1.2;
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
        <div class="subtitle">Grid Ruangan 6 Baris &times; 5 Kolom &bull; Total 30 Peserta (21 Perempuan &bull; 9 Laki-Laki) &bull; Dilengkapi Posisi Pendoa (Sesi 5) &amp; Pembasuh (Sesi 10)</div>
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
      <div class="col-header-box male-header">KOLOM 5 (L/P)</div>
    </div>

    <!-- 6 ROWS GRID -->
    <div class="grid-container">
"""

    row_names = [
        "BARIS 1<br><span style='font-size:5.2pt; font-weight:normal; color:#64748b;'>Terdepan</span>",
        "BARIS 2<br><span style='font-size:5.2pt; font-weight:normal; color:#64748b;'>Baris Kedua</span>",
        "BARIS 3<br><span style='font-size:5.2pt; font-weight:normal; color:#64748b;'>Baris Ketiga</span>",
        "BARIS 4<br><span style='font-size:5.2pt; font-weight:normal; color:#64748b;'>Baris Keempat</span>",
        "BARIS 5<br><span style='font-size:5.2pt; font-weight:normal; color:#64748b;'>Baris Kelima</span>",
        "BARIS 6<br><span style='font-size:5.2pt; font-weight:normal; color:#64748b;'>Paling Belakang</span>",
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
          <div class="roles-container">
            <div class="role-row pendoa-row">
              <span class="role-label">Pendoa:</span>
              <span class="role-value">{item['pendoa']}</span>
            </div>
            <div class="role-row pembasuh-row">
              <span class="role-label">Pembasuh:</span>
              <span class="role-value">{item['pembasuh']}</span>
            </div>
          </div>
        </div>
"""
        # Lorong Tengah
        html += """
        <div class="aisle-divider">LORONG</div>
"""
        # Kolom 4 & 5 (Sisi Kanan: 2 Kursi Pria / Pasangan)
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
          <div class="roles-container">
            <div class="role-row pendoa-row">
              <span class="role-label">Pendoa:</span>
              <span class="role-value">{item['pendoa']}</span>
            </div>
            <div class="role-row pembasuh-row">
              <span class="role-label">Pembasuh:</span>
              <span class="role-value">{item['pembasuh']}</span>
            </div>
          </div>
        </div>
"""
        html += """
      </div>
"""

    html += """
    </div>

    <div class="page-footer">
      <span>PERMATA GBKP RUNGGUN BOGOR &bull; MAPER 2026 &bull; PLOTTING TEMPAT DUDUK PEMBASUHAN</span>
      <span>Kiri: Perempuan (Pink) &bull; Kanan: Laki-Laki (Biru) &bull; Emas: CD &bull; Ungu: Pendoa &bull; Biru Muda: Pembasuh &bull; Halaman 1 dari 2</span>
    </div>
  </div>

  <!-- ==================== HALAMAN 2: DIREKTORI LENGKAP & REKAP PERAN ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-left">
        <div class="tag">PERMATA GBKP RUNGGUN BOGOR &bull; PANDUAN PENGURUS &amp; TIM PELAYAN</div>
        <div class="title">TABEL DIREKTORI LENGKAP &amp; REKAP TIM PEMBASUH / PENDOA</div>
        <div class="subtitle">Plotting Lengkap 30 Peserta &bull; Segregasi Gender 100% (Pria membasuh Pria, Wanita membasuh Wanita)</div>
      </div>
      <div class="header-badges">
        <span class="h-badge h-badge-female">21 Perempuan</span>
        <span class="h-badge h-badge-male">9 Laki-Laki</span>
        <span class="h-badge h-badge-cd">9 Pembasuh (2L / 7P)</span>
      </div>
    </div>

    <div class="table-section">
      <!-- Kolom Kiri: Tabel 30 Peserta -->
      <div>
        <div class="sub-table-title">
          <span>Daftar 30 Peserta Menurut Posisi Kursi (6x5)</span>
          <span style="font-weight:600; color:#475569;">Kolom 1-3: Kiri | Kolom 4-5: Kanan</span>
        </div>
        <table class="data-table">
          <thead>
            <tr>
              <th style="width:14px; text-align:center;">No</th>
              <th style="width:34px;">Kursi</th>
              <th>Nama Lengkap Peserta</th>
              <th style="width:16px; text-align:center;">G</th>
              <th style="width:20px; text-align:center;">Ket</th>
              <th>Pendoa (Sesi 5)</th>
              <th style="width:62px;">Pembasuh (S10)</th>
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
              <td><span class="badge-pembasuh">{item['pembasuh']}</span></td>
            </tr>
"""
            count += 1

    html += """
          </tbody>
        </table>
      </div>

      <!-- Kolom Kanan: Rekap Tim Pembasuh & Tim Pendoa -->
      <div style="display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <!-- Rekap Pembasuh Sesi 10 -->
          <div class="sub-table-title" style="color:#0369a1; border-color:#0284c7;">
            <span>💧 Rekap Tim Pembasuh Kaki (Sesi 10)</span>
            <span style="font-size:6pt; font-weight:700;">9 Pembasuh</span>
          </div>
"""

    for pb in pembasuh_summary:
        seats_str = " &bull; ".join(pb["kursi"])
        tag_color = "#1e40af" if pb["gen"] == "Laki-Laki" else "#9d174d"
        html += f"""
          <div class="card-rekap">
            <div class="card-rekap-title">
              <span>💧 <strong>{pb['pembasuh'].upper()}</strong> ({pb['gen']})</span>
              <span style="color:{tag_color}; font-weight:700;">{pb['area']} &bull; {pb['jumlah']}</span>
            </div>
            <div class="card-rekap-body">
              {seats_str}
            </div>
          </div>
"""

    html += """
          <!-- Catatan Pembasuhan -->
          <div style="background:#eff6ff; border-left:3px solid #3b82f6; padding:3px 6px; border-radius:3px; font-size:5.8pt; color:#1e40af; margin-top:4px; line-height:1.2;">
            ✨ <strong>Prinsip Pembasuhan (Sesi 10):</strong><br>
            &bull; <strong>Laki-Laki dengan Laki-Laki:</strong> Raj (4 adik) &amp; Amori (5 adik) di sisi Kanan.<br>
            &bull; <strong>Perempuan dengan Perempuan:</strong> 7 Kakak Pembasuh (masing-masing 3 adik) duduk berurutan rapi per baris di sisi Kiri &amp; Belakang Kanan.
          </div>
        </div>

        <div style="background:#fef9c3; border-left:3px solid #eab308; padding:3px 6px; border-radius:3px; font-size:5.8pt; color:#713f12; margin-top:4px; line-height:1.2;">
          💡 <strong>Sesi 5 (Mendoakan):</strong> Tim Pendoa bergerak mendatangi adik bimbingan sesuai daftar pendoa di samping kiri. Adik bimbingan yang didoakan berada dalam posisi baris yang berdekatan.
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
    # Take screenshot of page 1 and page 2 to verify
    page.screenshot(path="page1_preview.png", full_page=False)
    browser.close()

size_kb = os.path.getsize(pdf_file) / 1024
print(f"SUCCESS! Rendered {pdf_file} ({size_kb:.1f} KB)")
