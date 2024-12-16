from tkinter import *
import time

window = Tk()
window.title("clock")
window.geometry("600x600")
window.config(bg="#facca6")
window.resizable(False, False)

canvas = Canvas(width=600, height=600, bg="#000000")
canvas.place(x=0, y=0)

WIDTH = 600
HEIGHT = 600

text_x = 300
text_y = 300
text_x_s = 301
text_y_s = 301

text_shadow = canvas.create_text(text_x_s, text_y_s, text='', font='Times 30')
text = canvas.create_text(text_x, text_y, text='', font='Times 30')

dx = 5

def clock():
    time_2 = time.strftime('%H:%M:%S')
    canvas.itemconfig(text_shadow, text=time_2, font='Times 30', fill="#ff0000")
    canvas.itemconfig(text, text=time_2, font='Times 30', fill="#ffffff")
    window.after(30, clock)

def move():
    global dx
    pos = canvas.coords(text)
    pos_2 = canvas.coords(text_shadow)
    
    if pos[0] and pos_2[0] + 75 >= WIDTH or pos[0] and pos_2[0] - 75 <= 0:
        dx = -dx  

    # canvas.move(text_shadow, dx, 0)
    # canvas.move(text, dx, 0)
    canvas.after(30, move)

clock()
move()

window.mainloop()