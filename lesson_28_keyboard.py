from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


def fun_press(event):
    print("ok")
    lab_text.config(text=event)


window.bind("<KeyPress>" , fun_press)


lab_text = Label(text="ответ:", bg="#fcf3d9" , fg = "#2e263a")
lab_text.place(x=10 , y=100)


window.mainloop()