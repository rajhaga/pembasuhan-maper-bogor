# -*- coding: utf-8 -*-
"""
Script to generate the Official PowerPoint Presentation (16:9 Widescreen)
for Ibadah Pembasuhan Kaki MAPER PERMATA GBKP Runggun Bogor 2026.
Contains 12 comprehensive, beautifully styled slides:
1. Cover / Title Slide
2. Tujuan Sasaran & Rundown 60 Menit (12 Sesi)
3. Denah & Plotting Tempat Duduk (6 Baris x 5 Kolom = 30 Kursi)
4. Direktori Tim Pembasuh (Sesi 10) & Tim Pendoa (Sesi 5)
5. Sesi 1: Pembukaan, Keheningan & Menyiapkan Hati (Narasi Lengkap WL)
6. Sesi 2: Lagu 1 — Seperti Rusa yang Rindu Sungai-Mu
7. Sesi 3 & 4: Refleksi Kerapuhan Hidup & Lagu 2 — Sejauh Timur dari Barat
8. Sesi 5 & 6: Saling Mendoakan & Lagu 3 — Sujud di Altar-Nya
9. Sesi 7 & 8: Kedatangan Air Pembasuhan & Lagu 4 — Hati Sebagai Hamba
10. Sesi 9 & 10: PUNCAK — Pembasuhan Kaki & Lagu 5 — Sentuh Hatiku
11. Sesi 11: Doa Penutup, Pengurapan & Berkat Imamat
12. Sesi 12: Sukacita Penutup & Lagu 6 — Hari Ini Kurasa Bahagia
"""

import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_pembasuhan_deck(output_pptx_path):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    BG_DARK = RGBColor(11, 19, 43)        # #0B132B Deep Midnight
    PANEL_DARK = RGBColor(26, 38, 57)     # #1A2639 Card background
    PANEL_BORDER = RGBColor(51, 65, 85)   # #334155 Slate border
    ACCENT_BLUE = RGBColor(37, 99, 235)   # #2563EB Primary Blue
    ACCENT_CYAN = RGBColor(14, 165, 233)  # #0EA5E9 Sky Cyan (Water)
    ACCENT_GOLD = RGBColor(245, 158, 11)  # #F59E0B Warm Amber / Gold
    ACCENT_PINK = RGBColor(236, 72, 153)  # #EC4899 Rose Pink (Perempuan)
    ACCENT_PURPLE = RGBColor(139, 92, 246)# #8B5CF6 Indigo / Purple (Pendoa)
    ACCENT_GREEN = RGBColor(16, 185, 129) # #10B981 Emerald
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_SLATE = RGBColor(203, 213, 225)  # #CBD5E1
    TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background() # no line
        return bg

    def add_header(slide, title_text, category_text="PERMATA GBKP RUNGGUN BOGOR • MAPER 2026"):
        # Category tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category_text.upper()
        p_tag.font.size = Pt(9.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_CYAN

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(20)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

        # Divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.025))
        line.fill.solid()
        line.fill.fore_color.rgb = ACCENT_BLUE
        line.line.fill.background()

    # =========================================================================
    # SLIDE 1: COVER SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_background(s1)

    # Accent decorative gradient band
    band = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.3), Inches(7.5))
    band.fill.solid()
    band.fill.fore_color.rgb = ACCENT_CYAN
    band.line.fill.background()

    # Logo if available
    logo_path = "logo_maper_gbkp_HD_2000px.png"
    if os.path.exists(logo_path):
        s1.shapes.add_picture(logo_path, Inches(1.0), Inches(1.6), width=Inches(2.4), height=Inches(2.4))
        content_left = Inches(3.7)
        content_width = Inches(8.8)
    else:
        content_left = Inches(1.2)
        content_width = Inches(11.0)

    # Cover Title Box
    c_box = s1.shapes.add_textbox(content_left, Inches(1.6), content_width, Inches(4.5))
    tf_c = c_box.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0

    p1 = tf_c.paragraphs[0]
    p1.text = "MAPER 2026 • PERMATA GBKP RUNGGUN BOGOR"
    p1.font.size = Pt(12)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_CYAN

    p2 = tf_c.add_paragraph()
    p2.text = "IBADAH PEMBASUHAN KAKI"
    p2.font.size = Pt(36)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(8)

    p3 = tf_c.add_paragraph()
    p3.text = "Sesi Reflektif 60 Menit • Kerendahan Hati, Pengampunan & Pemulihan Sejati"
    p3.font.size = Pt(16)
    p3.font.color.rgb = ACCENT_GOLD
    p3.space_before = Pt(4)

    p4 = tf_c.add_paragraph()
    p4.text = "Naskah Lengkap Pemimpin Pujian (WL), Panduan Operator, Denah Duduk & Rekap Pelayanan"
    p4.font.size = Pt(11)
    p4.font.color.rgb = TEXT_SLATE
    p4.space_before = Pt(14)

    p5 = tf_c.add_paragraph()
    p5.text = "« Ersada Arih Man Dibata, Si Sampat-sampaten Ibas Kekelengen • Soli Deo Gloria »"
    p5.font.size = Pt(11.5)
    p5.font.italic = True
    p5.font.bold = True
    p5.font.color.rgb = ACCENT_CYAN
    p5.space_before = Pt(18)

    # Badges bar at bottom of cover
    badge_bg = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.7))
    badge_bg.fill.solid()
    badge_bg.fill.fore_color.rgb = PANEL_DARK
    badge_bg.line.color.rgb = PANEL_BORDER

    tf_bb = badge_bg.text_frame
    tf_bb.word_wrap = True
    p_bb = tf_bb.paragraphs[0]
    p_bb.alignment = PP_ALIGN.CENTER
    p_bb.text = "⏱️ DURASI: 60 MENIT   •   👥 30 PESERTA (21 PEREMPUAN & 9 LAKI-LAKI)   •   💧 9 PEMBASUH   •   🙏 12 PENDOA"
    p_bb.font.size = Pt(11)
    p_bb.font.bold = True
    p_bb.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 2: TUJUAN SASARAN & RUNDOWN IKHTISAR 12 SESI
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_background(s2)
    add_header(s2, "Tujuan Sasaran (Tusar) & Rundown 60 Menit (12 Sesi)")

    # Left Column: Tusar Box & 4 Tahapan Utama
    card_tusar = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.4))
    card_tusar.fill.solid()
    card_tusar.fill.fore_color.rgb = PANEL_DARK
    card_tusar.line.color.rgb = ACCENT_CYAN
    tf_tu = card_tusar.text_frame
    tf_tu.word_wrap = True
    tf_tu.margin_left = tf_tu.margin_right = tf_tu.margin_top = tf_tu.margin_bottom = Inches(0.2)

    p_tu1 = tf_tu.paragraphs[0]
    p_tu1.text = "🎯 TUJUAN SASARAN (TUSAR)"
    p_tu1.font.size = Pt(13)
    p_tu1.font.bold = True
    p_tu1.font.color.rgb = ACCENT_GOLD

    p_tu2 = tf_tu.add_paragraph()
    p_tu2.text = "Peserta dapat merasakan damai sejahtera lewat penyembahan yang mendalam sehingga sesi ini menjadi media reflektif untuk menyadari betapa pentingnya Tuhan dalam hidupnya, mengalami kasih dan kerendahan hati Kristus lewat pembasuhan kaki oleh pengurus/kakak-abang, serta tergerak untuk menyerahkan diri dan aktif bersama keluarga PERMATA GBKP Bogor."
    p_tu2.font.size = Pt(10)
    p_tu2.font.color.rgb = TEXT_SLATE
    p_tu2.space_before = Pt(8)

    p_tu3 = tf_tu.add_paragraph()
    p_tu3.text = "🌟 4 FASE UTAMA IBADAH:"
    p_tu3.font.size = Pt(11.5)
    p_tu3.font.bold = True
    p_tu3.font.color.rgb = ACCENT_CYAN
    p_tu3.space_before = Pt(14)

    phases = [
        ("1. Hening & Persiapan Diri", "Melepaskan kebisingan, merapatkan barisan persaudaraan."),
        ("2. Pengakuan & Doa Syafaat", "Mengakui kerapuhan diri, didoakan oleh kakak pembimbing."),
        ("3. Puncak Pembasuhan Kaki", "Teladan Kristus, pembasuhan kaki hening diiringi air kendi."),
        ("4. Pengurapan & Sukacita", "Pemberkatan imamat, komitmen baru & sukacita keluarga.")
    ]
    for ph_title, ph_desc in phases:
        p_ph = tf_tu.add_paragraph()
        p_ph.text = f"• {ph_title}: {ph_desc}"
        p_ph.font.size = Pt(9.2)
        p_ph.font.color.rgb = TEXT_WHITE
        p_ph.space_before = Pt(4)

    # Right Column: 12 Sesi Rundown Grid
    card_rundown = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(1.55), Inches(7.033), Inches(5.4))
    card_rundown.fill.solid()
    card_rundown.fill.fore_color.rgb = PANEL_DARK
    card_rundown.line.color.rgb = PANEL_BORDER
    tf_rd = card_rundown.text_frame
    tf_rd.word_wrap = True
    tf_rd.margin_left = tf_rd.margin_right = tf_rd.margin_top = tf_rd.margin_bottom = Inches(0.2)

    p_rd1 = tf_rd.paragraphs[0]
    p_rd1.text = "⏱️ RUNDOWN DETAIL 12 SESI (TOTAL 60 MENIT)"
    p_rd1.font.size = Pt(13)
    p_rd1.font.bold = True
    p_rd1.font.color.rgb = ACCENT_CYAN

    sessions_data = [
        ("Sesi 1 (00:00 - 06:00)", "Pengantar WL, Hening & Menyiapkan Hati", "Base Ambient Do=D", ACCENT_GOLD),
        ("Sesi 2 (06:00 - 10:30)", "Lagu 1: Seperti Rusa yang Rindu Sungai-Mu", "Penyembahan Mula", ACCENT_CYAN),
        ("Sesi 3 (10:30 - 13:00)", "Refleksi Kerapuhan Hidup & Pengakuan Dosa", "Hening & Doa Pribadi", TEXT_MUTED),
        ("Sesi 4 (13:00 - 17:30)", "Lagu 2: Sejauh Timur dari Barat", "Pengampunan Dosa", ACCENT_CYAN),
        ("Sesi 5 (17:30 - 21:00)", "Saling Mendoakan Beban & Pergumulan", "Tim Pendoa Bergerak", ACCENT_PURPLE),
        ("Sesi 6 (21:00 - 25:30)", "Lagu 3: Sujud di Altar-Nya", "Pemberkatan & Penyerahan", ACCENT_CYAN),
        ("Sesi 7 (25:30 - 28:00)", "Prosesi Kendi Air & Teladan Pembasuhan Kaki", "Air Mengalir Hening", ACCENT_GOLD),
        ("Sesi 8 (28:00 - 32:30)", "Lagu 4: Hati Sebagai Hamba", "Ketaatan & Kerendahan Hati", ACCENT_CYAN),
        ("Sesi 9 (32:30 - 34:00)", "WL Membimbing Peserta Membuka Sepatu", "Persiapan Pembasuhan", TEXT_MUTED),
        ("Sesi 10 (34:00 - 48:00)", "PUNCAK: Pembasuhan Kaki & Lagu 5 (Sentuh Hatiku)", "9 Pembasuh Melayani", ACCENT_GOLD),
        ("Sesi 11 (48:00 - 52:00)", "Doa Penutup, Pengurapan & Berkat Imamat", "Pengurapan Minyak", ACCENT_PURPLE),
        ("Sesi 12 (52:00 - 60:00)", "Sukacita Penutup & Lagu 6 (Hari Ini Kurasa Bahagia)", "Foto & Pelukan Keluarga", ACCENT_GREEN),
    ]

    for s_time, s_name, s_tag, s_color in sessions_data:
        p_s = tf_rd.add_paragraph()
        p_s.text = f"{s_time} | {s_name} — [{s_tag}]"
        p_s.font.size = Pt(8.6)
        p_s.font.color.rgb = s_color
        p_s.space_before = Pt(3)

    # =========================================================================
    # SLIDE 3: DENAH TEMPAT DUDUK 6 BARIS X 5 KOLOM (30 KURSI)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_background(s3)
    add_header(s3, "Denah & Plotting Tempat Duduk (6 Baris x 5 Kolom = 30 Peserta)")

    # Stage Banner at Top
    stage_box = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.45), Inches(11.733), Inches(0.35))
    stage_box.fill.solid()
    stage_box.fill.fore_color.rgb = ACCENT_BLUE
    stage_box.line.fill.background()
    tf_st = stage_box.text_frame
    p_st = tf_st.paragraphs[0]
    p_st.alignment = PP_ALIGN.CENTER
    p_st.text = "↑ ↑ PANGGUNG DEPAN • MIMBAR • SALIB • PROSESI KENDI AIR PEMBASUHAN ↑ ↑"
    p_st.font.size = Pt(9.5)
    p_st.font.bold = True
    p_st.font.color.rgb = TEXT_WHITE

    # Grid Dimensions
    # Left: 3 cols (perempuan) | Aisle | Right: 2 cols (laki-laki + 3 perempuan)
    start_y = Inches(1.9)
    row_height = Inches(0.8)
    row_gap = Inches(0.08)

    col_widths = [Inches(1.8), Inches(1.8), Inches(1.8), Inches(0.6), Inches(2.7), Inches(2.7)]
    col_xs = [
        Inches(0.8),
        Inches(2.65),
        Inches(4.5),
        Inches(6.35), # Lorong
        Inches(7.0),
        Inches(9.75)
    ]

    # Grid Data
    grid_seating = [
        # Baris 1
        [
            ("B1-K1", "Natasya Nizura", "P", False, "Barby M", "dea"),
            ("B1-K2", "Renate Callysta", "P", True, "Barby M", "dea"),
            ("B1-K3", "Melvina Nathania", "P", True, "Barby M", "dea"),
            None,
            ("B1-K4", "Kelvin Immanuel", "L", False, "Marshall B", "raj"),
            ("B1-K5", "Geraldo Oktovian", "L", True, "Marshall B", "raj"),
        ],
        # Baris 2
        [
            ("B2-K1", "Irene Johanna", "P", True, "Febi G", "cindy"),
            ("B2-K2", "Elsa Natalita", "P", False, "Febi G", "cindy"),
            ("B2-K3", "Kimberly Angelina", "P", False, "Febi G", "cindy"),
            None,
            ("B2-K4", "Setenly Ekel", "L", False, "Evan PK", "raj"),
            ("B2-K5", "Hozael Jeremia", "L", False, "Paskal M", "raj"),
        ],
        # Baris 3
        [
            ("B3-K1", "Margaretta Br S", "P", False, "Lia PK", "chantika"),
            ("B3-K2", "Elvira Faulita", "P", False, "Lia PK", "chantika"),
            ("B3-K3", "Jessica Lysia", "P", False, "Lia PK", "chantika"),
            None,
            ("B3-K4", "Dave Berenta", "L", False, "Paskal M", "amori"),
            ("B3-K5", "Nathan Bastanta", "L", True, "Daniel T", "amori"),
        ],
        # Baris 4
        [
            ("B4-K1", "Chiara Fiorenza", "P", True, "Winda M", "yohebet"),
            ("B4-K2", "Agustina br G", "P", False, "Winda M", "yohebet"),
            ("B4-K3", "Aurel Anastasya", "P", False, "Winna A", "yohebet"),
            None,
            ("B4-K4", "Ryando Alwirasesa", "L", False, "Daniel T", "amori"),
            ("B4-K5", "Bellian Casey", "L", True, "Marvel B", "amori"),
        ],
        # Baris 5
        [
            ("B5-K1", "Bianca Noella", "P", False, "Winda M", "leora"),
            ("B5-K2", "Allegra Luweenda", "P", False, "Winna A", "leora"),
            ("B5-K3", "Nicole Alvara", "P", False, "Winna A", "leora"),
            None,
            ("B5-K4", "Gideon Ginting", "L", False, "Evan PK", "amori"),
            ("B5-K5", "Tiffany Christabel", "P", False, "Franz S", "ella"),
        ],
        # Baris 6
        [
            ("B6-K1", "Judith Serafica", "P", True, "Sonya T", "audrey"),
            ("B6-K2", "Voofea kembaren", "P", False, "Sonya T", "audrey"),
            ("B6-K3", "Meka Suriyangi", "P", False, "Sonya T", "audrey"),
            None,
            ("B6-K4", "Agitta Ria", "P", True, "Marvel B", "ella"),
            ("B6-K5", "Cheesya Avira", "P", True, "Franz S", "ella"),
        ],
    ]

    for r_i, r_data in enumerate(grid_seating):
        y_pos = start_y + r_i * (row_height + row_gap)
        for c_i, seat in enumerate(r_data):
            x_pos = col_xs[c_i]
            w_pos = col_widths[c_i]

            if seat is None:
                # Lorong Tengah
                if r_i == 0:
                    aisle_box = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x_pos, start_y, w_pos, Inches(5.2))
                    aisle_box.fill.solid()
                    aisle_box.fill.fore_color.rgb = PANEL_DARK
                    aisle_box.line.color.rgb = PANEL_BORDER
                    tf_ai = aisle_box.text_frame
                    p_ai = tf_ai.paragraphs[0]
                    p_ai.alignment = PP_ALIGN.CENTER
                    p_ai.text = "L\nO\nR\nO\nN\nG"
                    p_ai.font.size = Pt(8.5)
                    p_ai.font.bold = True
                    p_ai.font.color.rgb = TEXT_MUTED
                continue

            seat_id, name, gen, is_cd, pendoa, pembasuh = seat
            # Card shape
            card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_pos, y_pos, w_pos, row_height)
            card.fill.solid()
            if gen == "P":
                card.fill.fore_color.rgb = RGBColor(60, 20, 45) # Deep Rose
                card.line.color.rgb = ACCENT_PINK
            else:
                card.fill.fore_color.rgb = RGBColor(20, 35, 65) # Deep Blue
                card.line.color.rgb = ACCENT_CYAN

            tf_sc = card.text_frame
            tf_sc.word_wrap = True
            tf_sc.margin_left = tf_sc.margin_right = tf_sc.margin_top = tf_sc.margin_bottom = Inches(0.04)

            # Top: ID & Badge
            p_top = tf_sc.paragraphs[0]
            cd_tag = " [CD]" if is_cd else ""
            p_top.text = f"{seat_id} ({gen}){cd_tag}"
            p_top.font.size = Pt(7)
            p_top.font.bold = True
            p_top.font.color.rgb = ACCENT_GOLD if is_cd else (ACCENT_PINK if gen == "P" else ACCENT_CYAN)

            # Name
            p_name = tf_sc.add_paragraph()
            p_name.text = name
            p_name.font.size = Pt(7.8)
            p_name.font.bold = True
            p_name.font.color.rgb = TEXT_WHITE

            # Roles
            p_roles = tf_sc.add_paragraph()
            p_roles.text = f"P: {pendoa} | B: {pembasuh.upper()}"
            p_roles.font.size = Pt(6.8)
            p_roles.font.color.rgb = TEXT_SLATE

    # Footer note on slide 3
    foot_box = s3.shapes.add_textbox(Inches(0.8), Inches(7.15), Inches(11.733), Inches(0.3))
    tf_f = foot_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.alignment = PP_ALIGN.CENTER
    p_f.text = "Kiri: 18 Perempuan (Pink)  •  Kanan: 9 Laki-laki (Biru) + 3 Perempuan (Ella)  •  Emas: Calon Diaken/Pertua [CD]"
    p_f.font.size = Pt(8.5)
    p_f.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 4: DIREKTORI TIM PEMBASUH & TIM PENDOA
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_background(s4)
    add_header(s4, "Direktori Tim Pembasuh Kaki (Sesi 10) & Tim Pendoa (Sesi 5)")

    # Left: Tim Pembasuh (9 Pembasuh)
    card_basuh = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(6.5), Inches(5.4))
    card_basuh.fill.solid()
    card_basuh.fill.fore_color.rgb = PANEL_DARK
    card_basuh.line.color.rgb = ACCENT_CYAN
    tf_ba = card_basuh.text_frame
    tf_ba.word_wrap = True
    tf_ba.margin_left = tf_ba.margin_right = tf_ba.margin_top = tf_ba.margin_bottom = Inches(0.2)

    p_ba1 = tf_ba.paragraphs[0]
    p_ba1.text = "💧 TIM PEMBASUH KAKI (SESI 10) — SEGREGASI GENDER 100%"
    p_ba1.font.size = Pt(11.5)
    p_ba1.font.bold = True
    p_ba1.font.color.rgb = ACCENT_CYAN

    p_ba2 = tf_ba.add_paragraph()
    p_ba2.text = "Laki-laki membasuh Laki-laki (2 Pembasuh) & Perempuan membasuh Perempuan (7 Pembasuh):"
    p_ba2.font.size = Pt(9)
    p_ba2.font.color.rgb = TEXT_SLATE
    p_ba2.space_before = Pt(4)

    pembasuh_data = [
        ("raj (Pria)", "B1-K4, B1-K5, B2-K4, B2-K5", "Kelvin, Geraldo [CD], Setenly, Hozael (4 Adik L)"),
        ("amori (Pria)", "B3-K4, B3-K5, B4-K4, B4-K5, B5-K4", "Dave, Nathan [CD], Ryando, Bellian [CD], Gideon (5 Adik L)"),
        ("dea (Wanita)", "B1-K1, B1-K2, B1-K3", "Natasya, Renate [CD], Melvina [CD] (3 Adik P)"),
        ("cindy (Wanita)", "B2-K1, B2-K2, B2-K3", "Irene [CD], Elsa, Kimberly (3 Adik P)"),
        ("chantika (Wanita)", "B3-K1, B3-K2, B3-K3", "Margaretta, Elvira, Jessica (3 Adik P)"),
        ("yohebet (Wanita)", "B4-K1, B4-K2, B4-K3", "Chiara [CD], Agustina, Aurel (3 Adik P)"),
        ("leora (Wanita)", "B5-K1, B5-K2, B5-K3", "Bianca, Allegra, Nicole (3 Adik P)"),
        ("audrey (Wanita)", "B6-K1, B6-K2, B6-K3", "Judith [CD], Voofea, Meka (3 Adik P)"),
        ("ella (Wanita)", "B5-K5, B6-K4, B6-K5", "Tiffany, Agitta [CD], Cheesya [CD] (3 Adik P)"),
    ]

    for p_name, p_seats, p_members in pembasuh_data:
        p_item = tf_ba.add_paragraph()
        p_item.text = f"• {p_name} [{p_seats}]:\n  → {p_members}"
        p_item.font.size = Pt(8.2)
        p_item.font.color.rgb = TEXT_WHITE
        p_item.space_before = Pt(3)

    # Right: Tim Pendoa (12 Pendoa)
    card_doa = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.5), Inches(1.55), Inches(5.033), Inches(5.4))
    card_doa.fill.solid()
    card_doa.fill.fore_color.rgb = PANEL_DARK
    card_doa.line.color.rgb = ACCENT_PURPLE
    tf_doa = card_doa.text_frame
    tf_doa.word_wrap = True
    tf_doa.margin_left = tf_doa.margin_right = tf_doa.margin_top = tf_doa.margin_bottom = Inches(0.2)

    p_doa1 = tf_doa.paragraphs[0]
    p_doa1.text = "🙏 REKAP TIM PENDOA (SESI 5)"
    p_doa1.font.size = Pt(11.5)
    p_doa1.font.bold = True
    p_doa1.font.color.rgb = ACCENT_PURPLE

    p_doa2 = tf_doa.add_paragraph()
    p_doa2.text = "Mendoakan pergumulan adik bimbingan secara khusus di kursi masing-masing:"
    p_doa2.font.size = Pt(9)
    p_doa2.font.color.rgb = TEXT_SLATE
    p_doa2.space_before = Pt(4)

    pendoa_data = [
        ("Barby Maretta", "Natasya, Renate [CD], Melvina [CD] (Baris 1 Kiri)"),
        ("Marshall Bangun", "Kelvin, Geraldo [CD] (Baris 1 Kanan)"),
        ("Febi Ginting", "Irene [CD], Elsa, Kimberly (Baris 2 Kiri)"),
        ("Lia PK", "Margaretta, Elvira, Jessica (Baris 3 Kiri)"),
        ("Paskal Mori", "Hozael (B2), Dave (B3 Kanan)"),
        ("Daniel Tarigan", "Nathan [CD] (B3), Ryando (B4 Kanan)"),
        ("Evan PK", "Setenly (B2), Gideon (B5 Kanan)"),
        ("Winda Meysara", "Chiara [CD], Agustina (B4), Bianca (B5)"),
        ("Winna Amelia", "Aurel (B4), Allegra, Nicole (B5)"),
        ("Sonya Tarigan", "Judith [CD], Voofea, Meka (Baris 6 Kiri)"),
        ("Franz Surya", "Tiffany (B5), Cheesya [CD] (B6 Kanan)"),
        ("Marvel Bangun", "Bellian [CD] (B4), Agitta [CD] (B6 Kanan)"),
    ]

    for d_name, d_target in pendoa_data:
        p_d = tf_doa.add_paragraph()
        p_d.text = f"• {d_name}: {d_target}"
        p_d.font.size = Pt(7.8)
        p_d.font.color.rgb = TEXT_WHITE
        p_d.space_before = Pt(2.5)

    # =========================================================================
    # SLIDE 5: SESI 1 — PEMBUKAAN, KEHENINGAN & MENYIAPKAN HATI (WL EXTENDED)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_background(s5)
    add_header(s5, "Sesi 1: Pembukaan, Keheningan & Menyiapkan Hati (00:00 - 06:00)")

    # Left: Petunjuk Teknis & Suasana
    c_cue = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(3.8), Inches(5.4))
    c_cue.fill.solid()
    c_cue.fill.fore_color.rgb = PANEL_DARK
    c_cue.line.color.rgb = ACCENT_GOLD
    tf_cue = c_cue.text_frame
    tf_cue.word_wrap = True
    tf_cue.margin_left = tf_cue.margin_right = tf_cue.margin_top = tf_cue.margin_bottom = Inches(0.2)

    p_c1 = tf_cue.paragraphs[0]
    p_c1.text = "💡 PETUNJUK OPERATOR & FASILITATOR"
    p_c1.font.size = Pt(11)
    p_c1.font.bold = True
    p_c1.font.color.rgb = ACCENT_GOLD

    cues_s1 = [
        ("Durasi Sesi", "00:00 - 06:00 (6 Menit Hening & Reflektif)"),
        ("Musik Latar", "Base Song Ambient (Do = D), solo piano/pad lembut, volume 20-30%."),
        ("Tata Lampu", "Ruangan dim / redup bertahap (warm amber). Lilin dan salib menyala di mimbar."),
        ("Aksi Peserta", "Duduk santai, rileks, gadget disimpan/silent, pejamkan mata, tarik napas dalam."),
        ("Aksi Kakak-Abang", "Perlahan mendekat, duduk di samping adik, letakkan tangan dan rangkul pundak dengan hangat."),
        ("Ruang Hening", "Berikan jeda diam 7-10 detik di sela narasi WL agar hadirat Tuhan meresap."),
    ]
    for ct, cd in cues_s1:
        p_ci = tf_cue.add_paragraph()
        p_ci.text = f"• {ct}:\n  {cd}"
        p_ci.font.size = Pt(8.5)
        p_ci.font.color.rgb = TEXT_WHITE
        p_ci.space_before = Pt(6)

    # Right: Naskah Lengkap WL
    c_wl = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(1.55), Inches(7.733), Inches(5.4))
    c_wl.fill.solid()
    c_wl.fill.fore_color.rgb = PANEL_DARK
    c_wl.line.color.rgb = ACCENT_CYAN
    tf_wl = c_wl.text_frame
    tf_wl.word_wrap = True
    tf_wl.margin_left = tf_wl.margin_right = tf_wl.margin_top = tf_wl.margin_bottom = Inches(0.2)

    p_w1 = tf_wl.paragraphs[0]
    p_w1.text = "🎙️ NASKAH LENGKAP PANDUAN WORSHIP LEADER (WL)"
    p_w1.font.size = Pt(11.5)
    p_w1.font.bold = True
    p_w1.font.color.rgb = ACCENT_CYAN

    wl_speech_paragraphs = [
        "\"Syalom teman-teman, adik-adik, dan seluruh rekan-rekan PERMATA yang dikasihi Tuhan... Bagaimana kabarnya hari ini? Gimana makannya tadi? Enak dan mengenyangkan ya? Puji Tuhan...",
        "Yuk, sekarang kita bersama-sama mengambil posisi duduk yang paling santai, paling nyaman, dan paling rileks... Kalau ada tas, jaket, atau barang bawaan, boleh diletakkan di samping atau di bawah kursi masing-masing. Dan untuk sejenak saja, mari kita simpan handphone atau gadget kita... kita silent dulu, kita taruh di dalam tas. Biarkan dunia luar menunggu sejenak. Malam ini adalah waktu khusus yang Tuhan sediakan antara kita, keluarga PERMATA kita, dan Tuhan Yesus.",
        "Mari bersama-sama kita pejamkan mata perlahan... Tarik napas panjang dari hidung... tahan sejenak... dan hembuskan perlahan melalui mulut... (Biarkan hening sejenak 7-10 detik diiringi denting piano lembut...)",
        "Tenangkan detak jantung kita... tenangkan pikiran kita dari segala keramaian, suara bising, dan kesibukan yang selama ini menyita hari-hari kita. Mungkin beberapa hari ini, atau beberapa bulan ke belakang, kepala dan hati kita terasa begitu penuh. Begitu banyak tugas kuliah, tuntutan sekolah, urusan pekerjaan, persoalan keluarga, ekspektasi orang sekitar, atau kebingungan masa depan yang membuat kita letih... letih fisik, dan terlebih lagi letih batin kita.",
        "Di tempat ini, di hadapan Tuhan malam ini, kita tidak perlu lagi berpura-pura kuat. Kita tidak perlu lagi memakai topeng bahwa 'aku baik-baik saja' jika sebenarnya hati kita sedang letih, rapuh, dan terluka. Di hadirat Tuhan, kita boleh menjadi diri kita apa adanya. Tuhan mengenal setiap air mata yang tersembunyi dan setiap pergumulan yang tak sanggup kita ceritakan kepada siapa pun.",
        "[KAKAK-ABANG PERLAHAN MENDEKAT, DUDUK DI SAMPING ADIK-ADIK, DAN MERANGKUL PUNDAK MEREKA DENGAN HANGAT]\nRasakan kehangatan tangan di pundak kita... Tuhan tidak pernah membiarkan kita berjuang sendirian. Di ruangan ini, kita dikelilingi oleh keluarga baru kita—kakak, abang, dan sahabat-sahabat PERMATA yang mengasihi kita, yang siap menopang, mendoakan, dan berjalan bersama kita di dalam Kristus.",
        "Seperti tanah kering menantikan air hujan... seperti rusa dahaga merindukan aliran sungai yang sejuk... demikianlah jiwa kita merindukan jamahan dan hadirat-Mu, ya Tuhan. Buka hati kita lebar-lebar... Mari bersama-sama kita angkat pujian sembahan kita: Seperti Rusa yang Rindu Sungai-Mu...\""
    ]

    for para in wl_speech_paragraphs:
        p_sp = tf_wl.add_paragraph()
        p_sp.text = para
        p_sp.font.size = Pt(8.2)
        p_sp.font.color.rgb = TEXT_WHITE
        p_sp.space_before = Pt(4)

    # Helper for Song Slides
    def add_song_slide(title, session_tag, key_tempo, lyrics_dict, note_text, accent_color=ACCENT_CYAN):
        s = prs.slides.add_slide(blank_layout)
        add_background(s)
        add_header(s, title, session_tag)

        # Meta card at top
        meta_card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.55))
        meta_card.fill.solid()
        meta_card.fill.fore_color.rgb = PANEL_DARK
        meta_card.line.color.rgb = accent_color
        tf_m = meta_card.text_frame
        p_m = tf_m.paragraphs[0]
        p_m.text = f"🎵 NADA DASAR: {key_tempo}   •   PANDUAN MUSIK & LITURGI"
        p_m.font.size = Pt(10)
        p_m.font.bold = True
        p_m.font.color.rgb = accent_color

        # Lyrics container
        card_ly = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(11.733), Inches(3.8))
        card_ly.fill.solid()
        card_ly.fill.fore_color.rgb = PANEL_DARK
        card_ly.line.color.rgb = PANEL_BORDER
        tf_l = card_ly.text_frame
        tf_l.word_wrap = True
        tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = tf_l.margin_bottom = Inches(0.25)

        first = True
        for part_name, part_text in lyrics_dict.items():
            p_lp = tf_l.paragraphs[0] if first else tf_l.add_paragraph()
            first = False
            p_lp.text = f"[{part_name.upper()}]"
            p_lp.font.size = Pt(11)
            p_lp.font.bold = True
            p_lp.font.color.rgb = ACCENT_GOLD
            if not first:
                p_lp.space_before = Pt(6)

            p_lt = tf_l.add_paragraph()
            p_lt.text = part_text
            p_lt.font.size = Pt(12)
            p_lt.font.color.rgb = TEXT_WHITE
            p_lt.space_before = Pt(2)

        # Bottom note card
        note_card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.8))
        note_card.fill.solid()
        note_card.fill.fore_color.rgb = RGBColor(15, 30, 50)
        note_card.line.color.rgb = accent_color
        tf_n = note_card.text_frame
        tf_n.word_wrap = True
        tf_n.margin_left = tf_n.margin_right = tf_n.margin_top = tf_n.margin_bottom = Inches(0.12)
        p_n = tf_n.paragraphs[0]
        p_n.text = f"💡 Catatan Rohani & Alur Liturgi:\n{note_text}"
        p_n.font.size = Pt(8.8)
        p_n.font.color.rgb = TEXT_SLATE
        return s

    # =========================================================================
    # SLIDE 6: SESI 2 — LAGU 1 (SEPERTI RUSA)
    # =========================================================================
    add_song_slide(
        title="Sesi 2: Lagu 1 — Seperti Rusa yang Rindu Sungai-Mu",
        session_tag="SESI 2 (06:00 - 10:30) • PENYEMBAHAN MULA & KERINDUAN HATI",
        key_tempo="Do = D • Tempo: Lambat & Khusyuk (Solo Piano Menenangkan)",
        lyrics_dict={
            "Bait 1": "S'perti rusa rindu sungai-Mu, jiwaku rindu Engkau\nKaulah Tuhan hasrat hatiku, kurindu menyembah-Mu",
            "Bait 2": "Engkau kekuatan dan perisaiku, kepada-Mu rohku berserah\nKaulah Tuhan hasrat hatiku, kurindu menyembah-Mu",
            "Chorus / Reff": "Yesus, Yesus, Kau berarti bagiku\nYesus, Yesus, Kau segalanya bagiku"
        },
        note_text="Musik solo piano jernih. Setelah Reff dinyanyikan berulang dengan khusyuk, vokal perlahan berhenti. WL memimpin doa pembuka singkat memohon hadirat dan pemulihan Roh Kudus menguasai seluruh ruangan.",
        accent_color=ACCENT_CYAN
    )

    # =========================================================================
    # SLIDE 7: SESI 3 & 4 — REFLEKSI KERAPUHAN & LAGU 2 (SEJAUH TIMUR DARI BARAT)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_background(s7)
    add_header(s7, "Sesi 3 & 4: Refleksi Kerapuhan & Lagu 2 — Sejauh Timur dari Barat", "SESI 3 & 4 (10:30 - 17:30) • PENGAKUAN DOSA & PENGAMPUNAN SEJATI")

    # Left: Sesi 3 Narasi Refleksi
    c_s3 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.4))
    c_s3.fill.solid()
    c_s3.fill.fore_color.rgb = PANEL_DARK
    c_s3.line.color.rgb = ACCENT_GOLD
    tf_s3 = c_s3.text_frame
    tf_s3.word_wrap = True
    tf_s3.margin_left = tf_s3.margin_right = tf_s3.margin_top = tf_s3.margin_bottom = Inches(0.2)

    p_s3_1 = tf_s3.paragraphs[0]
    p_s3_1.text = "🕊️ SESI 3: PENGAKUAN DOSA & REFLEKSI"
    p_s3_1.font.size = Pt(11)
    p_s3_1.font.bold = True
    p_s3_1.font.color.rgb = ACCENT_GOLD

    p_s3_2 = tf_s3.add_paragraph()
    p_s3_2.text = "Narasi WL:\n\"Adik-adik dan rekan-rekan terkasih... Sering kali dalam perjalanan hidup, kita merasa gagal. Kita jatuh dalam kesalahan yang sama, kita menyakiti hati orang tua, mengecewakan sahabat, dan melukai hati Tuhan.\n\nAda rasa malu dan rasa bersalah yang mengikat kita. Namun dengarlah firman Tuhan malam ini: Kasih Tuhan jauh lebih besar dari segala dosa dan kegagalan kita. Dia tidak mengingat-ingat kesalahan kita saat kita datang dengan hati yang hancur dan bertobat.\""
    p_s3_2.font.size = Pt(9.2)
    p_s3_2.font.color.rgb = TEXT_WHITE
    p_s3_2.space_before = Pt(8)

    p_s3_3 = tf_s3.add_paragraph()
    p_s3_3.text = "💡 Petunjuk:\nHening total 1-2 menit. Peserta diajak berdoa pribadi mengakui segala beban dan dosa di hadapan Tuhan."
    p_s3_3.font.size = Pt(8.5)
    p_s3_3.font.color.rgb = TEXT_SLATE
    p_s3_3.space_before = Pt(12)

    # Right: Sesi 4 Lirik Lagu 2
    c_s4 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(1.55), Inches(7.033), Inches(5.4))
    c_s4.fill.solid()
    c_s4.fill.fore_color.rgb = PANEL_DARK
    c_s4.line.color.rgb = ACCENT_CYAN
    tf_s4 = c_s4.text_frame
    tf_s4.word_wrap = True
    tf_s4.margin_left = tf_s4.margin_right = tf_s4.margin_top = tf_s4.margin_bottom = Inches(0.2)

    p_s4_1 = tf_s4.paragraphs[0]
    p_s4_1.text = "🎵 SESI 4: LAGU 2 — SEJAUH TIMUR DARI BARAT"
    p_s4_1.font.size = Pt(11)
    p_s4_1.font.bold = True
    p_s4_1.font.color.rgb = ACCENT_CYAN

    p_s4_2 = tf_s4.add_paragraph()
    p_s4_2.text = "Nada Dasar: Do = C / D   •   Tempo: Khidmat & Penuh Rasa Syukur"
    p_s4_2.font.size = Pt(9)
    p_s4_2.font.bold = True
    p_s4_2.font.color.rgb = ACCENT_GOLD
    p_s4_2.space_before = Pt(4)

    lyrics_s2 = [
        ("[Bait 1]", "Sejauh timur dari barat, Engkau membuang dosaku\nTiada Kau ingat lagi pelanggaranku"),
        ("[Bait 2]", "Jauh ke dalam tubir laut, Kau melemparkan dosaku\nTiada Kau perhitungkan kesalahanku"),
        ("[Chorus / Reff]", "Betapa besar kasih pengampunan-Mu Tuhan\nTak Kau pandang hina hati yang hancur\nKu berterima kasih kepada-Mu ya Tuhan\nPengampunan yang Kau beri pulihkanku")
    ]
    for b_title, b_text in lyrics_s2:
        p_bt = tf_s4.add_paragraph()
        p_bt.text = b_title
        p_bt.font.size = Pt(9.5)
        p_bt.font.bold = True
        p_bt.font.color.rgb = ACCENT_GOLD
        p_bt.space_before = Pt(8)

        p_bx = tf_s4.add_paragraph()
        p_bx.text = b_text
        p_bx.font.size = Pt(10.5)
        p_bx.font.color.rgb = TEXT_WHITE
        p_bx.space_before = Pt(2)

    # =========================================================================
    # SLIDE 8: SESI 5 & 6 — SALING MENDOAKAN & LAGU 3 (SUJUD DI ALTAR-NYA)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_background(s8)
    add_header(s8, "Sesi 5 & 6: Saling Mendoakan & Lagu 3 — Sujud di Altar-Nya", "SESI 5 & 6 (17:30 - 25:30) • PENYERAHAN BEBAN HIDUP & TUMPANGAN TANGAN PENDOA")

    # Left: Sesi 5 Gerakan Pendoa
    c_s5 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.4))
    c_s5.fill.solid()
    c_s5.fill.fore_color.rgb = PANEL_DARK
    c_s5.line.color.rgb = ACCENT_PURPLE
    tf_s5 = c_s5.text_frame
    tf_s5.word_wrap = True
    tf_s5.margin_left = tf_s5.margin_right = tf_s5.margin_top = tf_s5.margin_bottom = Inches(0.2)

    p_s5_1 = tf_s5.paragraphs[0]
    p_s5_1.text = "🙏 SESI 5: SALING MENDOAKAN BEBAN"
    p_s5_1.font.size = Pt(11)
    p_s5_1.font.bold = True
    p_s5_1.font.color.rgb = ACCENT_PURPLE

    p_s5_2 = tf_s5.add_paragraph()
    p_s5_2.text = "Gerakan Tim Pendoa:\n\"12 Kakak-Abang Pendoa mendatangi adik-adik bimbingan sesuai denah duduk. Letakkan tangan di pundak atau kepala adik-adiknya, bisikkan doa berkat, dengarkan dan doakan beban pergumulan mereka secara pribadi.\"\n\nNarasi WL:\n\"Bawa segala beban beratmu ke altar Tuhan malam ini... Jangan pulang membawa kepahitan dan kekuatiran. Serahkan semuanya kepada Yesus.\""
    p_s5_2.font.size = Pt(9.2)
    p_s5_2.font.color.rgb = TEXT_WHITE
    p_s5_2.space_before = Pt(8)

    p_s5_3 = tf_s5.add_paragraph()
    p_s5_3.text = "💡 Petunjuk:\nSuasana penuh keharuan. Adik-adik merasakan kehangatan bahwa ada saudara seiman yang tulus menopang dalam doa."
    p_s5_3.font.size = Pt(8.5)
    p_s5_3.font.color.rgb = TEXT_SLATE
    p_s5_3.space_before = Pt(12)

    # Right: Sesi 6 Lirik Lagu 3
    c_s6 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(1.55), Inches(7.033), Inches(5.4))
    c_s6.fill.solid()
    c_s6.fill.fore_color.rgb = PANEL_DARK
    c_s6.line.color.rgb = ACCENT_CYAN
    tf_s6 = c_s6.text_frame
    tf_s6.word_wrap = True
    tf_s6.margin_left = tf_s6.margin_right = tf_s6.margin_top = tf_s6.margin_bottom = Inches(0.2)

    p_s6_1 = tf_s6.paragraphs[0]
    p_s6_1.text = "🎵 SESI 6: LAGU 3 — SUJUD DI ALTAR-NYA"
    p_s6_1.font.size = Pt(11)
    p_s6_1.font.bold = True
    p_s6_1.font.color.rgb = ACCENT_CYAN

    p_s6_2 = tf_s6.add_paragraph()
    p_s6_2.text = "Nada Dasar: Do = C / D   •   Tempo: Khidmat & Menyerahkan Diri"
    p_s6_2.font.size = Pt(9)
    p_s6_2.font.bold = True
    p_s6_2.font.color.rgb = ACCENT_GOLD
    p_s6_2.space_before = Pt(4)

    lyrics_s3 = [
        ("[Bait 1]", "Bila hati terasa berat, tak seorang pun mengerti bebanku\nKu datang ke hadirat-Mu, Yesus memulihkanku"),
        ("[Bait 2]", "Bila jiwa merasa lelah, air mata menetes di pipiku\nKu tahu Engkau pedulikanku, Yesus menyembuhkanku"),
        ("[Chorus / Reff]", "Sujud di altar-Nya, ku bawa hidupku\nKu serahkan beban pergumulanku\nTiada yang mustahil bagi-Mu Tuhan\nSujud di altar-Nya, ku bawa korban syukurku")
    ]
    for b_title, b_text in lyrics_s3:
        p_bt = tf_s6.add_paragraph()
        p_bt.text = b_title
        p_bt.font.size = Pt(9.5)
        p_bt.font.bold = True
        p_bt.font.color.rgb = ACCENT_GOLD
        p_bt.space_before = Pt(8)

        p_bx = tf_s6.add_paragraph()
        p_bx.text = b_text
        p_bx.font.size = Pt(10.5)
        p_bx.font.color.rgb = TEXT_WHITE
        p_bx.space_before = Pt(2)

    # =========================================================================
    # SLIDE 9: SESI 7 & 8 — KEDATANGAN AIR & LAGU 4 (HATI SEBAGAI HAMBA)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_background(s9)
    add_header(s9, "Sesi 7 & 8: Kedatangan Air Pembasuhan & Lagu 4 — Hati Sebagai Hamba", "SESI 7 & 8 (25:30 - 32:30) • PROSESI AIR KENDI & TELADAN KERENDAHAN HATI YESUS")

    # Left: Sesi 7 Prosesi Air
    c_s7 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.4))
    c_s7.fill.solid()
    c_s7.fill.fore_color.rgb = PANEL_DARK
    c_s7.line.color.rgb = ACCENT_CYAN
    tf_s7 = c_s7.text_frame
    tf_s7.word_wrap = True
    tf_s7.margin_left = tf_s7.margin_right = tf_s7.margin_top = tf_s7.margin_bottom = Inches(0.2)

    p_s7_1 = tf_s7.paragraphs[0]
    p_s7_1.text = "💧 SESI 7: PROSESI KENDI AIR PEMBASUHAN"
    p_s7_1.font.size = Pt(11)
    p_s7_1.font.bold = True
    p_s7_1.font.color.rgb = ACCENT_CYAN

    p_s7_2 = tf_s7.add_paragraph()
    p_s7_2.text = "Aksi Liturgis:\n• Petugas membawa kendi air, baskom pembasuhan, dan kain handuk bersih masuk ke ruang ibadah dengan langkah khidmat.\n• Air dituang ke dalam baskom. (Biarkan suara gemericik air terdengar 5-7 detik dalam keheningan total...)\n\nNarasi WL:\n\"Lihatlah air di depanmu... Yesus, Raja di atas segala raja, mengambil rupa seorang hamba, mengikatkan kain lenan di pinggang-Nya, dan membasuh kaki para murid-Nya. Malam ini, kasih yang sama hadir di tengah-tengah kita.\""
    p_s7_2.font.size = Pt(9.2)
    p_s7_2.font.color.rgb = TEXT_WHITE
    p_s7_2.space_before = Pt(8)

    p_s7_3 = tf_s7.add_paragraph()
    p_s7_3.text = "💡 Petunjuk:\nLampu mimbar menyorot kendi air dan salib. Keheningan yang dalam menyelimuti seluruh ruangan."
    p_s7_3.font.size = Pt(8.5)
    p_s7_3.font.color.rgb = TEXT_SLATE
    p_s7_3.space_before = Pt(12)

    # Right: Sesi 8 Lirik Lagu 4
    c_s8 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(1.55), Inches(7.033), Inches(5.4))
    c_s8.fill.solid()
    c_s8.fill.fore_color.rgb = PANEL_DARK
    c_s8.line.color.rgb = ACCENT_CYAN
    tf_s8 = c_s8.text_frame
    tf_s8.word_wrap = True
    tf_s8.margin_left = tf_s8.margin_right = tf_s8.margin_top = tf_s8.margin_bottom = Inches(0.2)

    p_s8_1 = tf_s8.paragraphs[0]
    p_s8_1.text = "🎵 SESI 8: LAGU 4 — HATI SEBAGAI HAMBA"
    p_s8_1.font.size = Pt(11)
    p_s8_1.font.bold = True
    p_s8_1.font.color.rgb = ACCENT_CYAN

    p_s8_2 = tf_s8.add_paragraph()
    p_s8_2.text = "Nada Dasar: Do = C   •   Tempo: Lambat, Menunduk & Khusyuk"
    p_s8_2.font.size = Pt(9)
    p_s8_2.font.bold = True
    p_s8_2.font.color.rgb = ACCENT_GOLD
    p_s8_2.space_before = Pt(4)

    lyrics_s4 = [
        ("[Bait 1]", "Ku tak membawa apa pun juga, saat ku datang ke dunia\nKu tinggal semua pada akhirnya, saat ku kembali ke surga"),
        ("[Chorus / Reff]", "Inilah yang ku punya, hati sebagai hamba\nYang mau taat dan setia pada-Mu Bapa\nKemanapun Kau bawa, kupersembahkan baktiku\nKu mau taat dan setia pada-Mu Bapa"),
        ("[Makna Rohani]", "Meneladani kerendahan hati Kristus yang melayani, bukan untuk dilayani. Menyiapkan hati untuk dibasuh dan saling membasuh.")
    ]
    for b_title, b_text in lyrics_s4:
        p_bt = tf_s8.add_paragraph()
        p_bt.text = b_title
        p_bt.font.size = Pt(9.5)
        p_bt.font.bold = True
        p_bt.font.color.rgb = ACCENT_GOLD
        p_bt.space_before = Pt(8)

        p_bx = tf_s8.add_paragraph()
        p_bx.text = b_text
        p_bx.font.size = Pt(10.5)
        p_bx.font.color.rgb = TEXT_WHITE
        p_bx.space_before = Pt(2)

    # =========================================================================
    # SLIDE 10: SESI 9 & 10 — PUNCAK PEMBASUHAN KAKI & LAGU 5 (SENTUH HATIKU)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_background(s10)
    add_header(s10, "Sesi 9 & 10: PUNCAK — Pembasuhan Kaki & Lagu 5 — Sentuh Hatiku", "SESI 9 & 10 (32:30 - 48:00) • PUNCAK LITURGIS • PEMBASUHAN KAKI & TANGISAN PEMULIHAN")

    # Left: Sesi 9 & 10 Petunjuk Pelaksanaan
    c_s9 = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.4))
    c_s9.fill.solid()
    c_s9.fill.fore_color.rgb = PANEL_DARK
    c_s9.line.color.rgb = ACCENT_GOLD
    tf_s9 = c_s9.text_frame
    tf_s9.word_wrap = True
    tf_s9.margin_left = tf_s9.margin_right = tf_s9.margin_top = tf_s9.margin_bottom = Inches(0.2)

    p_s9_1 = tf_s9.paragraphs[0]
    p_s9_1.text = "💧 PUNCAK PEMBASUHAN KAKI"
    p_s9_1.font.size = Pt(11)
    p_s9_1.font.bold = True
    p_s9_1.font.color.rgb = ACCENT_GOLD

    p_s9_2 = tf_s9.add_paragraph()
    p_s9_2.text = "• Sesi 9 (Buka Sepatu):\nWL membimbing adik-adik membuka sepatu dan kaos kaki dengan tenang. Merendahkan hati di hadapan Tuhan.\n\n• Sesi 10 (Prosesi Pembasuhan):\n9 Kakak Pembasuh (2 Pria & 7 Wanita) berlutut di depan adik-adik bimbingan masing-masing:\n- Menuangkan air hangat ke kaki adik\n- Membasuh dengan lembut kedua belah kaki\n- Mengeringkan kaki dengan handuk bersih\n- Memeluk erat adik-adiknya dalam kasih Kristus."
    p_s9_2.font.size = Pt(9)
    p_s9_2.font.color.rgb = TEXT_WHITE
    p_s9_2.space_before = Pt(6)

    p_s9_3 = tf_s9.add_paragraph()
    p_s9_3.text = "✨ Aturan Emas:\n100% Segregasi Gender. Pria membasuh pria, wanita membasuh wanita. Menjaga kekudusan dan kehangatan sejati."
    p_s9_3.font.size = Pt(8.5)
    p_s9_3.font.bold = True
    p_s9_3.font.color.rgb = ACCENT_CYAN
    p_s9_3.space_before = Pt(8)

    # Right: Sesi 10 Lirik Lagu 5 (Sentuh Hatiku)
    c_s10 = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(1.55), Inches(7.033), Inches(5.4))
    c_s10.fill.solid()
    c_s10.fill.fore_color.rgb = PANEL_DARK
    c_s10.line.color.rgb = ACCENT_CYAN
    tf_s10 = c_s10.text_frame
    tf_s10.word_wrap = True
    tf_s10.margin_left = tf_s10.margin_right = tf_s10.margin_top = tf_s10.margin_bottom = Inches(0.2)

    p_s10_1 = tf_s10.paragraphs[0]
    p_s10_1.text = "🎵 SESI 10: LAGU 5 — SENTUH HATIKU"
    p_s10_1.font.size = Pt(11)
    p_s10_1.font.bold = True
    p_s10_1.font.color.rgb = ACCENT_CYAN

    p_s10_2 = tf_s10.add_paragraph()
    p_s10_2.text = "Nada Dasar: Do = C / G   •   Tempo: Sangat Khusyuk, Mengalir Lembut & Mengharukan"
    p_s10_2.font.size = Pt(9)
    p_s10_2.font.bold = True
    p_s10_2.font.color.rgb = ACCENT_GOLD
    p_s10_2.space_before = Pt(4)

    lyrics_s5 = [
        ("[Bait 1]", "Betapa ku mencintai, segala yang t'lah terjadi\nTak pernah sendiri jalani hidup ini, selalu menyertai"),
        ("[Bait 2]", "Betapa kumenyadari, di dalam hidupku ini\nKau s'lalu memberi rancangan terbaik, oleh karena kasih"),
        ("[Chorus / Reff]", "Bapa, sentuh hatiku, ubah hidupku menjadi yang baru\nBagai emas yang murni, Kau membentuk bejana hatiku\nBapa, ajarku mengerti sebuah kasih yang selalu memberi\nBagai air mengalir, yang tiada pernah berhenti")
    ]
    for b_title, b_text in lyrics_s5:
        p_bt = tf_s10.add_paragraph()
        p_bt.text = b_title
        p_bt.font.size = Pt(9.5)
        p_bt.font.bold = True
        p_bt.font.color.rgb = ACCENT_GOLD
        p_bt.space_before = Pt(8)

        p_bx = tf_s10.add_paragraph()
        p_bx.text = b_text
        p_bx.font.size = Pt(10.5)
        p_bx.font.color.rgb = TEXT_WHITE
        p_bx.space_before = Pt(2)

    # =========================================================================
    # SLIDE 11: SESI 11 — DOA PENUTUP, PENGURAPAN & BERKAT IMAMAT
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_background(s11)
    add_header(s11, "Sesi 11: Doa Penutup, Pengurapan & Berkat Imamat (48:00 - 52:00)", "SESI 11 • PENEGUHAN KOMITMEN, PENGURAPAN & BERKAT IMAMAT TUHAN")

    # Left: Doa Penyerahan & Pengurapan
    c_s11_l = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(5.5), Inches(5.4))
    c_s11_l.fill.solid()
    c_s11_l.fill.fore_color.rgb = PANEL_DARK
    c_s11_l.line.color.rgb = ACCENT_PURPLE
    tf_11l = c_s11_l.text_frame
    tf_11l.word_wrap = True
    tf_11l.margin_left = tf_11l.margin_right = tf_11l.margin_top = tf_11l.margin_bottom = Inches(0.2)

    p_11_1 = tf_11l.paragraphs[0]
    p_11_1.text = "🕊️ DOA PENUTUP & PENGURAPAN"
    p_11_1.font.size = Pt(11.5)
    p_11_1.font.bold = True
    p_11_1.font.color.rgb = ACCENT_PURPLE

    p_11_2 = tf_11l.add_paragraph()
    p_11_2.text = "Doa Penyerahan Diri (WL & Pendeta / Pengurus):\n\"Bapa di dalam surga, terima kasih atas malam yang kudus ini. Engkau telah membasuh hati kami, membasuh kaki kami, dan menyatukan kami dalam ikatan kasih keluarga PERMATA GBKP Runggun Bogor.\n\nKami serahkan 30 adik-adik peserta MAPER ini ke dalam tangan-Mu. Biarlah hati mereka selalu terpaut pada-Mu, bertumbuh dalam iman, dan menjadi berkat di tengah gereja, keluarga, kampus, dan masyarakat.\""
    p_11_2.font.size = Pt(9.5)
    p_11_2.font.color.rgb = TEXT_WHITE
    p_11_2.space_before = Pt(10)

    p_11_3 = tf_11l.add_paragraph()
    p_11_3.text = "Tindakan Liturgis:\nPendeta / Pengurus mengurapi dahi para peserta dengan minyak sebagai tanda peneguhan dan pengudusan hidup baru di dalam Kristus."
    p_11_3.font.size = Pt(9)
    p_11_3.font.color.rgb = TEXT_SLATE
    p_11_3.space_before = Pt(14)

    # Right: Berkat Imamat (Bilangan 6:24-26)
    c_s11_r = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.5), Inches(1.55), Inches(6.033), Inches(5.4))
    c_s11_r.fill.solid()
    c_s11_r.fill.fore_color.rgb = PANEL_DARK
    c_s11_r.line.color.rgb = ACCENT_GOLD
    tf_11r = c_s11_r.text_frame
    tf_11r.word_wrap = True
    tf_11r.margin_left = tf_11r.margin_right = tf_11r.margin_top = tf_11r.margin_bottom = Inches(0.25)

    p_11_b1 = tf_11r.paragraphs[0]
    p_11_b1.text = "📜 BERKAT IMAMAT (BILANGAN 6:24-26)"
    p_11_b1.font.size = Pt(12)
    p_11_b1.font.bold = True
    p_11_b1.font.color.rgb = ACCENT_GOLD

    p_11_b2 = tf_11r.add_paragraph()
    p_11_b2.text = "TUHAN memberkati engkau dan melindungi engkau;\n\nTUHAN menyinari engkau dengan wajah-Nya dan memberi engkau kasih karunia;\n\nTUHAN menghadapkan wajah-Nya kepadamu dan memberi engkau damai sejahtera."
    p_11_b2.font.size = Pt(13)
    p_11_b2.font.bold = True
    p_11_b2.font.color.rgb = TEXT_WHITE
    p_11_b2.space_before = Pt(16)

    p_11_b3 = tf_11r.add_paragraph()
    p_11_b3.text = "Semua Jemaat Menjawab:\n\"AMIN... AMIN... AMIN!\""
    p_11_b3.font.size = Pt(11)
    p_11_b3.font.bold = True
    p_11_b3.font.color.rgb = ACCENT_CYAN
    p_11_b3.space_before = Pt(20)

    # =========================================================================
    # SLIDE 12: SESI 12 — SUKACITA PENUTUP & LAGU 6 (HARI INI KURASA BAHAGIA)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_background(s12)
    add_header(s12, "Sesi 12: Sukacita Penutup & Lagu 6 — Hari Ini Kurasa Bahagia", "SESI 12 (52:00 - 60:00) • SUKACITA KELUARGA BARU PERMATA GBKP BOGOR")

    # Left: Sesi 12 Lirik Lagu 6
    c_s12 = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(7.5), Inches(5.4))
    c_s12.fill.solid()
    c_s12.fill.fore_color.rgb = PANEL_DARK
    c_s12.line.color.rgb = ACCENT_GREEN
    tf_s12 = c_s12.text_frame
    tf_s12.word_wrap = True
    tf_s12.margin_left = tf_s12.margin_right = tf_s12.margin_top = tf_s12.margin_bottom = Inches(0.2)

    p_s12_1 = tf_s12.paragraphs[0]
    p_s12_1.text = "🎵 LAGU 6: HARI INI KURASA BAHAGIA"
    p_s12_1.font.size = Pt(12)
    p_s12_1.font.bold = True
    p_s12_1.font.color.rgb = ACCENT_GREEN

    p_s12_2 = tf_s12.add_paragraph()
    p_s12_2.text = "Nada Dasar: Do = D / F   •   Tempo: Ceria, Bersemangat, Tepuk Tangan & Sukacita"
    p_s12_2.font.size = Pt(9.5)
    p_s12_2.font.bold = True
    p_s12_2.font.color.rgb = ACCENT_GOLD
    p_s12_2.space_before = Pt(4)

    lyrics_s6 = [
        ("[Bait]", "Hari ini kurasa bahagia, berkumpul bersama saudara seiman\nTuhan Yesus t'lah satukan kita, tanpa memandang di antara kita"),
        ("[Bait Tambahan]", "Bergandengan tangan dalam kasih, dalam satu hati\nBerjalan dalam terang kasih Tuhan"),
        ("[Chorus / Reff]", "Kau sahabatku, kau saudaraku\nTiada yang dapat memisahkan kita\nKau sahabatku, kau saudaraku\nTiada yang dapat memisahkan kita")
    ]
    for b_title, b_text in lyrics_s6:
        p_bt = tf_s12.add_paragraph()
        p_bt.text = b_title
        p_bt.font.size = Pt(10)
        p_bt.font.bold = True
        p_bt.font.color.rgb = ACCENT_GOLD
        p_bt.space_before = Pt(8)

        p_bx = tf_s12.add_paragraph()
        p_bx.text = b_text
        p_bx.font.size = Pt(11)
        p_bx.font.color.rgb = TEXT_WHITE
        p_bx.space_before = Pt(2)

    # Right: Penutup, Moto & Salaman
    c_s12_r = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(1.55), Inches(4.033), Inches(5.4))
    c_s12_r.fill.solid()
    c_s12_r.fill.fore_color.rgb = PANEL_DARK
    c_s12_r.line.color.rgb = ACCENT_CYAN
    tf_12r = c_s12_r.text_frame
    tf_12r.word_wrap = True
    tf_12r.margin_left = tf_12r.margin_right = tf_12r.margin_top = tf_12r.margin_bottom = Inches(0.2)

    p_12r_1 = tf_12r.paragraphs[0]
    p_12r_1.text = "🎉 SELAMAT DATANG DI KELUARGA PERMATA!"
    p_12r_1.font.size = Pt(11)
    p_12r_1.font.bold = True
    p_12r_1.font.color.rgb = ACCENT_GOLD

    p_12r_2 = tf_12r.add_paragraph()
    p_12r_2.text = "Aksi Sukacita:\n• Semua peserta dan panitia berdiri, bergandengan tangan, bertepuk tangan, dan menyanyikan lagu dengan sukacita meluap-luap.\n• Saling berjabat tangan dan berpelukan hangat.\n• Sesi foto bersama seluruh peserta MAPER 2026."
    p_12r_2.font.size = Pt(9.2)
    p_12r_2.font.color.rgb = TEXT_WHITE
    p_12r_2.space_before = Pt(8)

    p_12r_3 = tf_12r.add_paragraph()
    p_12r_3.text = "MOTO PERMATA GBKP:\n« Ersada Arih Man Dibata,\nSi Sampat-sampaten Ibas Kekelengen »\n\nSOLI DEO GLORIA!"
    p_12r_3.font.size = Pt(10.5)
    p_12r_3.font.bold = True
    p_12r_3.font.color.rgb = ACCENT_CYAN
    p_12r_3.space_before = Pt(16)

    prs.save(output_pptx_path)
    print(f"SUCCESS! Created PowerPoint presentation at {output_pptx_path}")

if __name__ == "__main__":
    out_path = "Presentasi_Pembasuhan_MAPER_PERMATA_Bogor.pptx"
    create_pembasuhan_deck(out_path)
