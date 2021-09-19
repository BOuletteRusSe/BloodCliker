@ECHO OFF
cls
title PY to EXE
color 4a
echo INIT 1/2
pyinstaller --onefile --windowed BloodClicker.py
echo INIT 2/2
pyinstaller --onefile on_click.py
rmdir /S /Q build
rmdir /S /Q __pycache__
del BloodClicker.spec
del on_click.spec