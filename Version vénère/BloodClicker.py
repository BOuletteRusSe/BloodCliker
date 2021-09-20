import psutil, os, time, ctypes, sys
from tkinter import *


def is_admin(): # Fonction pour vérifier si l'utilisateur est administrateur
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin(): # Si l'utilisateur est administrateur
    
    os.system("@ECHO OFF")
    os.system("start on_click.exe")
    time.sleep(2.5)
    
    while True:
        if "on_click.exe" not in (p.name() for p in psutil.process_iter()):
            os.system("start on_click.exe")
            time.sleep(1.5)
 
   
else: # Sinon relancer le launcher en administrateur
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
