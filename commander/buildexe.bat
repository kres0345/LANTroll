@echo off
del minion.exe
pyinstaller --noconsole -F minion.py
rem -i icon.ico
move %~dp0\dist\minion.exe %cd%
del minion.spec /q 
del dist /q
del build /s /q
timeout 2
rmdir dist
rmdir build\minion
rmdir build