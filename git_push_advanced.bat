@echo off
echo.
echo ===== Git Push Helper =====
echo.

if "%1"=="" (
    set /p message="Enter commit message (or press Enter for auto): "
    if "!message!"=="" set message=Auto commit: %date% %time%
) else (
    set message=%*
)

echo.
echo Adding all changes...
git add .

echo Committing with message: "%message%"
git commit -m "%message%"

echo Pushing to GitHub...
git push

echo.
echo ✓ Successfully pushed to GitHub!
echo.
pause
