@echo off
REM Check if Python is installed
python -m http.server 3000 --bind 0.0.0.0
pause
