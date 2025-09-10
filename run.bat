@echo off
setlocal

REM Create venv if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    py -m venv .venv
)

REM Activate venv
call .venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
pip install -r requirements.txt

REM Run the script
python main.py
