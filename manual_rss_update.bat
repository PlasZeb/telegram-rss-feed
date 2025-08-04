@echo off
echo.
echo ===== Manual RSS Update =====
echo.
echo Running Python RSS generator...
"C:/Users/Milán/AppData/Local/Programs/Python/Python39/python.exe" rss_telegram.py
echo.
echo Pushing to GitHub...
git add rss_feed.json
git commit -m "Manual RSS update: %date% %time%"
git push
echo.
echo ✓ RSS feed updated and pushed to GitHub!
echo.
pause
