@echo off
chcp 65001 >nul
title OpenClaw Watchdog

echo ========================================
echo Starting OpenClaw Watchdog...
echo ========================================
echo.

if not exist "%~dp0app.hta" (
    echo ERROR: app.hta not found!
    dir "%~dp0*.hta"
    pause
    exit /b 1
)

echo Found app.hta
echo Starting GUI...
echo.

start "" mshta "%~dp0app.hta"

echo.
echo ========================================
echo GUI started!
echo Please check for a new window.
echo ========================================
echo.
echo Press any key to close this window...
pause >nul
