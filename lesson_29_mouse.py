from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")



def mouse_motion(event):
    # lab_text.config(text=event)
    # lab_text.config(text=str(event.x) + " / " + str(event.y))
    window.title(str(event.x) + " / " + str(event.y))


def mouse_b1(event):
    lab_text.config(text=event)
    window.config(bg="#78ffa5")


def mouse_b2(event):
    lab_text.config(text=event)
    window.config(bg="#facca6")


def mouse_b3(event):
    lab_text.config(text=event)
    window.config(bg="#565656")



window.bind("<Motion>" , mouse_motion)
window.bind("<Button-1>" , mouse_b1)
window.bind("<Button-2>" , mouse_b2)
window.bind("<Button-3>" , mouse_b3)


lab_text = Label(text="ответ:", bg="#fcf3d9" , fg = "#2e263a" , font=("Arial" , 16))
lab_text.place(x=10 , y=100)


window.mainloop()