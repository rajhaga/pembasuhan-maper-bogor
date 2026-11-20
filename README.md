# Smart Web Conductor & Companion — Pembasuhan MAPER PERMATA GBKP Runggun Bogor

Aplikasi pemandu liturgi dan kendali multimedia otomatis untuk sesi Pembasuhan Kaki MAPER (Masa Pengenalan Anggota Baru) PERMATA GBKP Runggun Bogor (Durasi 60 Menit).

---

## 🌟 Fitur Utama
1. **Interactive Conductor & Rundown Real-Time:** Naskah WL lengkap, petunjuk teknis operator multimedia, aba-aba fasilitator kakak-abang, dan alur per menit (Sesi 1 s/d 12).
2. **Base Song Ambient Stream:** Audio ambient mengalun terus di latar belakang dengan kontrol volume terpusat (auto loop).
3. **Player Video Karaoke MP4 (1080p):** Dilengkapi tombol *Play* pada tiap sesi lagu rohani. Saat video diputar, Base Song otomatis mengecil (*fade out*), dan saat video selesai/berpindah, Base Song perlahan mengalun kembali (*fade in*).
4. **Distribusi Lembar Panduan Digital:**
   - 📘 **Buku Panduan Liturgi & Naskah WL (PDF 6 Halaman A4)**
   - 🎵 **Buku Lirik Lagu Jemaat & Peserta (PDF 3 Halaman A4)**
5. **Responsif Multi-Device:** Dapat diakses oleh laptop operator maupun smartphone pengurus/fasilitator melalui jaringan Wi-Fi lokal.

---

## 🚀 Cara Menjalankan di Laptop Lain

### 1. Prasyarat
- **Python 3.9+** terinstall di laptop ([Download Python](https://www.python.org/downloads/)). Pastikan opsi *"Add Python to PATH"* dicentang saat instalasi.
- Koneksi Wi-Fi yang sama antara laptop dan HP pengurus.

### 2. Instalasi Dependensi
Buka terminal / Command Prompt di folder ini, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Server
Cukup klik ganda (double-click) file **`run.bat`**, atau ketik di terminal:
```bash
python audio_server.py
```

### 4. Membuka di Browser
- **Di Laptop Operator:** Buka `http://localhost:8080` atau `http://127.0.0.1:8080`
- **Di HP Pengurus / Fasilitator:** Buka alamat IP laptop operator yang muncul di layar terminal (contoh: `http://192.168.0.xxx:8080`).

---

## 🎵 Daftar Lagu & Media MP4
1. **Lagu 1:** *Seperti Rusa yang Rindu Sungai-Mu* (Do = D)
2. **Lagu 2:** *Sejauh Timur Dari Barat* (Do = C / D)
3. **Lagu 3:** *Sujud Di Altar-Nya* (Do = D / E)
4. **Lagu 4:** *Hati Sebagai Hamba* (Do = C / D)
5. **Lagu 5:** *Sentuh Hatiku* (Do = G / A) — *Puncak Pembasuhan Kaki*
6. **Lagu 6:** *Hari Ini Kurasa Bahagia* (Do = F / G) — *Sukacita Penutup*

---
*Soli Deo Gloria — PERMATA GBKP Runggun Bogor*
