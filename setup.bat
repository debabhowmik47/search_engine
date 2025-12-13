@echo off
REM Quick setup script for Multi-LLM Search Agent (Windows)

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup complete!
echo Run the agent with: .\.venv\Scripts\python.exe main.py
echo Or activate venv: .\.venv\Scripts\Activate.ps1
pause
