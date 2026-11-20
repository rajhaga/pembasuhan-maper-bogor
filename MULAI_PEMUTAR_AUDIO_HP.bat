@echo off
title Pemutar Audio Pembasuhan MAPER PERMATA Bogor
cd /d "%~dp0"
cls
echo ============================================================
echo   PEMUTAR AUDIO PEMBASUHAN MAPER PERMATA BOGOR
echo ============================================================
echo   Menjalankan server streaming lokal...
echo ============================================================
python audio_server.py
pause
