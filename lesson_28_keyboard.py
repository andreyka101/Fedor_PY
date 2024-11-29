from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


def fun_press(event):
    # print("ok")
    # lab_text.config(text=event)
    lab_text.config(text=event.keysym)
    # lab_text.config(text=event.state)
    window.config(bg="#313131")
    if(event.keysym == "z"):
        lab_text.config(bg="#03c5c5")
    if(event.keysym == "z" and event.state == 12):
        lab_text.config(bg="#c5a503")


def fun_release(event):
    # print("ok")
    lab_text.config(text=event)
    window.config(bg="#ffffff")
    if(event.keysym == "z"):
        lab_text.config(bg="#753838")



window.bind("<KeyPress>" , fun_press)
window.bind("<KeyRelease>" , fun_release)


lab_text = Label(text="ответ:", bg="#fcf3d9" , fg = "#2e263a" , font=("Arial" , 16))
lab_text.place(x=10 , y=100)


window.mainloop()