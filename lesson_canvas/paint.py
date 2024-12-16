from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)

num_bool = False

def fun_b1(e):
    global num_bool
    if(num_bool):
        canV.create_oval(e.x , e.y , e.x + 20 , e.y + 20 , fill="#232323" ,width=0 , outline="#1da7e2")
canV.bind("<Motion>" , fun_b1)

def fun_bPress(event):
    global num_bool
    if(event.keysym == "z"):
        num_bool = True
canV.bind("<KeyPress>" , fun_bPress)

window.mainloop()