from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


# создание элемента Canvas
canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)
# рисуем в Canvas с помощью методов


# canV.create_arc(50 , 50 , 200 , 200, fill="#701717" , start = 50 , extent = 410 )
# canV.create_arc(50 , 50 , 200 , 200, fill="#ffffff" , start = 40 , extent = 410)


window.mainloop()