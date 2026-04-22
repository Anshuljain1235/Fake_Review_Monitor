@echo off
echo ========================================
echo   Fake Review Monitor - Starting...
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo Dependencies already installed
)

echo.
echo [2/3] Starting Flask server...
echo.
echo ========================================
echo   Server will start at:
echo   http://127.0.0.1:5000
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the Flask app
python app.py

pause
