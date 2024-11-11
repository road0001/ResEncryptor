@echo off
echo Running scripts...
Python38\python.exe randomGenerate.py ResEncryptor.py
Python38\python.exe outputVersion.py
echo Building Execute file...
taskkill /f /im ResEncryptor.exe
Python38\python.exe Python38\scripts\pyinstaller.exe -F -i icon.ico ResEncryptor.py
pause