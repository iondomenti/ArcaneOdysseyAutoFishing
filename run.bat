@echo off
setlocal

REM Detect Python command
where py >nul 2>nul
if %ERRORLEVEL%==0 (
    set PYTHON=py
) else (
    where python >nul 2>nul
    if %ERRORLEVEL%==0 (
        set PYTHON=python
    ) else (
        echo Python not found! Please install Python and add it to PATH.
        exit /b 1
    )
)

REM Create venv if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    %PYTHON% -m venv .venv
)

REM Activate venv
call .venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
pip install -r requirements.txt

REM Run the script
python src\main.py
