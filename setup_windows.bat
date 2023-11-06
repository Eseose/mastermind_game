@echo off
echo Creating Virtual Environment called mastermind_venv
python -m venv mastermind_venv

echo Activating Virtual Environment called mastermind_venv
call "mastermind_venv\Scripts\activate"

echo Installing Pip requirements into Virtual Environment called mastermind_venv
pip3 install -r requirements.txt

pause