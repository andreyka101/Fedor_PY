
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")



arr = ["python","java","c++","typeScript"]


# Combobox - это совмищение Listbox и Entry
comboBox_1 = ttk.Combobox(values=arr , font= ("MV Boli" , 15))
comboBox_1.place(x = 10 , y = 10)


def fun_1():
    # comboBox_1.get() - получаем значение 
    lab_text.config(text = comboBox_1.get())
button_b1 = Button(text="but click" , command = fun_1)
button_b1.place(x=20 , y=150)


lab_text = Label(text="none", bg="#dfc062" , fg = "#6600FF")
# placе - позиция и размер элемента
lab_text.place(x=10 , y=40 , width=200 , height=20)




window.mainloop()