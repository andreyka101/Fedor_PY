
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")



def fun_1():
    # считываем переменную
    lab_text.config(text=numbers.get())
    if(numbers.get() == "b1"):
        lab_text.configure( bg = "#ff1c1c")
    if(numbers.get() == "b2"):
        lab_text.configure( bg = "#ffd500")
    if(numbers.get() == "b3"):
        lab_text.configure( bg = "#51ff00")


# numbers общая переменная для связи трех Radiobutton
numbers = StringVar(value="b1")


# variable - привязка Radiobutton к переменной
but_1 = ttk.Radiobutton(text="123" , value= "b1" , variable= numbers , command=fun_1)
but_1.place(x=10 , y=10)

but_2 = ttk.Radiobutton(text="456" , value= "b2" , variable= numbers , command=fun_1)
but_2.place(x=10 , y=40)

but_3 = ttk.Radiobutton(text="789" , value= "b3" , variable= numbers , command=fun_1)
but_3.place(x=10 , y=70)



lab_text = Label(text="asryffgvg", bg="#dfc062" , fg = "#6600FF")
lab_text.place(x=10 , y=100 , width=200 , height=20)






def fun_2():
    if(background.get() == "back_1"):
        window.config(bg="#747474")
    if(background.get() == "back_2"):
        window.config(bg="#c8fcff")



background = StringVar()

but_4 = ttk.Radiobutton(text="123" , value= "back_1" , variable= background , command=fun_2)
but_4.place(x=80 , y=10)

but_4 = ttk.Radiobutton(text="456" , value= "back_2" , variable= background , command=fun_2)
but_4.place(x=80 , y=40)




window.mainloop()