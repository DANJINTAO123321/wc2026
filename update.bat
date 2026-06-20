@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo === ???? index.html ===
python -X utf8 build.py
echo.
echo === git ?? ===
git status --short
echo.
echo === ???????? main ===
git add .
git diff --cached --quiet || git commit -m "?????????"
git push
echo.
echo === ?? ===
pause
