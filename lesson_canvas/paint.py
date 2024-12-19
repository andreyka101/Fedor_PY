from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)



# движение мыши
def fun_b1(event):
    # print(num_bool)
    # создаём oval
    canV.create_oval(event.x - 20/2 , event.y - 20/2 , event.x + 20 , event.y + 20 , fill="#232323" ,width=0 , outline="#1da7e2")

canV.bind("<B1-Motion>" , fun_b1)



# движение мыши
def fun_b2(event):
    # print(num_bool)
    # создаём oval
    canV.create_oval(event.x - 50/2 , event.y - 50/2 , event.x + 50 , event.y + 50 , fill="#ffffff" ,width=0 , outline="#1da7e2")

canV.bind("<B3-Motion>" , fun_b2)




window.mainloop()