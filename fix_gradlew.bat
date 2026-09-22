@echo off
chcp 65001 >nul
echo Converting gradlew to LF line endings...

rem Use PowerShell to convert CRLF to LF
powershell -Command "$content = Get-Content -Path 'gradlew' -Raw; $content = $content -replace \"`r`n\", \"`n\"; [System.IO.File]::WriteAllText('gradlew', $content, [System.Text.Encoding]::UTF8)"

echo Checking git status...
git status

echo.
echo Adding and committing changes...
git add gradlew
git commit -m "将gradlew转换为Unix LF换行符"

echo.
echo Pushing to GitHub...
git push origin main

echo.
echo Force pushing tag to trigger build...
git push origin v1.0.0 --force

echo.
echo Done! Check GitHub Actions at:
echo https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame/actions
pause
