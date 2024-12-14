from tkinter import *
from tkinter import ttk

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")



# num_scale - значение Scale
def fun(num_scale):
    num_x =int(float(num_scale))
    lab_text.config(text= "ответ: " + str(num_x))
    lab_text.place(x=num_x)
    



# ползунок
# length = длина ползунока
# from_ = старт
# to = конец
# value = значение по умолчанию
scale_1 = ttk.Scale(orient=VERTICAL , length=200 , from_= 1 , to= 300 , value = 50 ,command=fun)
scale_1.place(x=20 , y=20)


lab_text = Label(text="ответ:", bg="#dfc062" , fg = "#6600FF")
lab_text.place(x=10 , y=100 , width=200 , height=20)


window.mainloop()
