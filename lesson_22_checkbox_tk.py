
from tkinter import *

window = Tk()
window.title("window")
# меняем ширину высоту и координаты окна
window.geometry("600x500")
# цвет окна
window.config(bg="#facca6")



def fun_1():
    lab_text.config(text= num_data.get())
    if(num_data.get() == 1) :
        window.config(bg="#ff811b")
    else :
        window.config(bg="#facca6")

num_data = IntVar()
check_box_but = Checkbutton(text="click" , variable = num_data , command=fun_1)
check_box_but.place(x=10 , y=10)


lab_text = Label(text= num_data.get())
lab_text.place(x=10 , y=40)



window.mainloop()

