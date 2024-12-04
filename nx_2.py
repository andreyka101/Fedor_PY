from tkinter import *
from random import *

window = Tk()
window.title('aim_train')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.config(bg = '#bebebe')
window.resizable(False, False)

def mouse_b1(event):
    target.place(w = 50, h = 50, x=(randint(50,screen_width-100)), y=(randint(50,screen_height-100)))
    

def mouse_pressed(event):
    target.config(bg = 'red')

def mouse_release(event):
    target.config(bg = 'black')

target = Label()
target.config(bg = "#000000")
target.place(w = 50, h = 50, x=(randint(50,screen_width-50)), y=(randint(50,screen_height-50)))



target.bind("<Button-1>" , mouse_b1)
target.bind("<ButtonPress>", mouse_pressed)
target.bind("<ButtonRelease>", mouse_release)






window.mainloop()