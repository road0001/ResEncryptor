@echo off
echo Running scripts...
randomGenerate.py ResEncryptor.py
outputVersion.py
echo Building Execute file...
pyinstaller -F -i icon.ico ResEncryptor.py
pause