# Git Push Script
param(
    [string]$message = "Auto commit: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
)

Write-Host "Adding changes..." -ForegroundColor Green
git add .

Write-Host "Committing with message: $message" -ForegroundColor Green
git commit -m $message

Write-Host "Pushing to GitHub..." -ForegroundColor Green
git push

Write-Host "Done! Changes pushed successfully." -ForegroundColor Green
