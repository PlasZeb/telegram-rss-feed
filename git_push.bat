@echo off
echo Pushing changes to GitHub...
git add .
git commit -m "Auto commit: %date% %time%"
git push
echo.
echo Done! Changes pushed to GitHub.
pause
