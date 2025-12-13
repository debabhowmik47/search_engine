@echo off
REM Run Multi-LLM Search Agent with virtual environment
cd /d "%~dp0"
.\.venv\Scripts\python.exe main.py
pause
