from tkinter import *


def Center(win): # Fonction copié collé pour centrer la fenêtre ptdrr
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def OnClick():
    print("Bouton cliqué !")


# Var
window = Tk()
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
window.minsize(round(sw / 2.4), round(sh / 2.4))
ww = round(sw / 1.28)
wh = round(sh / 1.5)
window.configure(background='black')
window.geometry(f"{ww}x{wh}")

Center(window)
window.update()
btnh = round(window.winfo_height() / 72)
btnw = round(window.winfo_width() / 33.3333333333)
click_button = Button(window, activebackground="#ED553A", activeforeground="#666261", borderwidth=5, background="#E53110", command=OnClick, foreground='#666261',
                      font="Arial", height=btnh, text="Click to Destroy", width=btnw)
click_button.pack()

while True:
    
    if btnh != round(window.winfo_height() / 72):
        btnh = round(window.winfo_height() / 72)
        click_button.destroy()
        click_button = Button(window, activebackground="#ED553A", activeforeground="#666261", borderwidth=5, background="#E53110", command=OnClick, foreground='#666261',
                      font="Arial", height=btnh, text="Click to Destroy", width=btnw)
        click_button.pack()
        
    if btnw != round(window.winfo_width() / 33.3333333333):
        btnw = round(window.winfo_width() / 33.3333333333)
        click_button.destroy()
        click_button = Button(window, activebackground="#ED553A", activeforeground="#666261", borderwidth=5, background="#E53110", command=OnClick, foreground='#666261',
                      font="Arial", height=btnh, text="Click to Destroy", width=btnw)
        click_button.pack()
    
    
    window.update()
