@echo off
chcp 65001 >nul
echo Checking Git configuration...
echo.

echo ===== Global core.autocrlf setting =====
git config --global core.autocrlf

echo.
echo ===== Local core.autocrlf setting =====
git config --local core.autocrlf

echo.
echo ===== Checking gradlew file format =====
powershell -Command "$bytes = [System.IO.File]::ReadAllBytes('gradlew'); $crlf = 0; $lf = 0; for($i=0; $i -lt $bytes.Length-1; $i++) { if($bytes[$i] -eq 13 -and $bytes[$i+1] -eq 10) { $crlf++ } elseif($bytes[$i] -eq 10) { $lf++ } }; Write-Host 'CRLF (Windows): ' $crlf; Write-Host 'LF (Unix): ' $lf"

echo.
echo ===== Fetch latest from GitHub and compare =====
git fetch origin main
git diff origin/main:gradlew gradlew

echo.
pause
