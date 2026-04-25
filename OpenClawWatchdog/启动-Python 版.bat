@echo off
chcp 65001 >nul
title OpenClaw Watchdog

echo ========================================
echo OpenClaw Watchdog - Python 版
echo ========================================
echo.

:: 检查 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未找到 Python
    echo 请安装 Python 3: https://www.python.org/
    pause
    exit /b 1
)

:: 检查 tkinter
python -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未找到 tkinter
    echo 请确保安装 Python 时勾选了 tcl/tk 支持
    pause
    exit /b 1
)

:: 启动程序
echo 正在启动...
cd /d "%~dp0"
python watchdog.py

if %errorlevel% neq 0 (
    echo.
    echo [错误] 启动失败
    pause
)
