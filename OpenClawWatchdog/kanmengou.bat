@echo off
chcp 65001 >nul
title OpenClaw Watchdog

:menu
cls
echo ========================================
echo    OpenClaw Watchdog
echo ========================================
echo.
call :show_config
echo.
echo [1] Start Watchdog
echo [2] Change Interval
echo [3] Check Port
echo [4] View Config
echo [0] Exit
echo.
echo ========================================
set /p choice=Enter choice (0-4): 

if "%choice%"=="1" goto start
if "%choice%"=="2" goto change
if "%choice%"=="3" goto check
if "%choice%"=="4" goto view
if "%choice%"=="0" goto exit
goto menu

:start
echo.
echo Starting watchdog...
cd /d "%~dp0"
call :watchdog_loop
pause
goto menu

:watchdog_loop
call :load_config

:check_loop
call :check_port
if %ERRORLEVEL% EQU 0 (
    echo [%TIME%] OK - Port 18789 listening
) else (
    echo [%TIME%] ERROR - Port not listening
    echo [%TIME%] Starting Gateway...
    start /B cmd /c "node F:\npm-global\node_modules\openclaw\openclaw.mjs gateway"
    ping -n 11 127.0.0.1 >nul
)
ping -n %CHECK_INTERVAL% 127.0.0.1 >nul
goto check_loop

:check_port
netstat -ano | findstr ":18789" >nul 2>&1
exit /b %ERRORLEVEL%

:change
echo.
echo Current: %CURRENT_INTERVAL% seconds
echo.
echo [1] 10 seconds
echo [2] 30 seconds
echo [3] 60 seconds
echo [4] 300 seconds
echo [5] Custom
echo.
set /p p=Select (1-5): 
if "%p%"=="1" set n=10&goto save
if "%p%"=="2" set n=30&goto save
if "%p%"=="3" set n=60&goto save
if "%p%"=="4" set n=300&goto save
if "%p%"=="5" set /p n=Enter seconds: &goto save
goto menu

:save
echo # OpenClaw Watchdog Config> "%~dp0watchdog_config.txt"
echo CHECK_INTERVAL=%n%>> "%~dp0watchdog_config.txt"
echo Saved! Interval: %n% seconds
pause
goto menu

:check
cls
echo ========================================
echo    Port Status
echo ========================================
netstat -ano | findstr ":18789"
if %ERRORLEVEL% EQU 0 (
    echo Status: Gateway running
) else (
    echo Status: Gateway not running
)
echo ========================================
pause
goto menu

:view
cls
echo ========================================
echo    Config File
echo ========================================
type "%~dp0watchdog_config.txt"
echo ========================================
pause
goto menu

:exit
cls
echo.
echo Exited
echo.
exit /b

:load_config
set CHECK_INTERVAL=30
for /f "tokens=2 delims==" %%a in ('findstr /i "^CHECK_INTERVAL=" "%~dp0watchdog_config.txt" 2^>nul') do set CURRENT_INTERVAL=%%a
if "%CURRENT_INTERVAL%"=="" set CURRENT_INTERVAL=30
set CHECK_INTERVAL=%CURRENT_INTERVAL%
goto :eof

:show_config
call :load_config
echo Check Interval: %CURRENT_INTERVAL% seconds
goto :eof
