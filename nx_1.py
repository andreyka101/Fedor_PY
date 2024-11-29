from tkinter import *
import random

window = Tk()
window.title('color')
w, h = 215, 300
window.geometry(f"{w}x{h}+{(window.winfo_screenwidth()-w)//2}+{(window.winfo_screenheight()-h)//2}")
window.config(bg = '#bebebe')
window.resizable(False, False)

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb  
 
def update_color(event=None):
    red = scale_red.get()
    green = scale_green.get()
    blue = scale_blue.get()
    label_color.config(bg=from_rgb((red, green, blue)))

scale_red = Scale(length=200, orient=VERTICAL, from_=0, to=255, command = update_color)
scale_red.place(x=20,y=20)
scale_green = Scale(length=200, orient=VERTICAL, from_=0, to=255, command = update_color)
scale_green.place(x=85,y=20)
scale_blue = Scale(length=200, orient=VERTICAL, from_=0, to=255, command = update_color)
scale_blue.place(x=150,y=20)

label_color = Label()
label_color.place(w=175, h=40, x=20, y=240)
label_color.config(bg=from_rgb((0,0,0)))



window.mainloop()