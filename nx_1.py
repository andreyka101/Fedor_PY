

from tkinter import *
import random


window = Tk()
window.title('finder')
w, h = 800, 800
window.geometry(f"{w}x{h}+{(window.winfo_screenwidth()-w)//2}+{(window.winfo_screenheight()-h)//2}")
window.config(bg = '#355aff')
window.resizable(False, False)

# инпут
inp_1 = Entry()
inp_1.place(x=245 , y=80 , height=50 , width=215)

# списки под каждый товар
sps_1 = []
sps_2 = []
sps_3 = []
sps_4 = []

# функции добавления в каждый список по типу товара
def add_1():
    sps_1.append(int(inp_1.get()))
    print(sps_1)
    button_summa= Button(text= 'посчитать', bg = '#57ca5d', command = l)
    button_summa.place(width = 100, height = 115, x = 590, y = 15)

def add_2():
    sps_2.append(int(inp_1.get()))
    print(sps_2)
    button_summa= Button(text= 'посчитать', bg = '#57ca5d', command = l)
    button_summa.place(width = 100, height = 115, x = 590, y = 15)

def add_3():
    sps_3.append(int(inp_1.get()))
    print(sps_3)
    button_summa= Button(text= 'посчитать', bg = '#57ca5d', command = l)
    button_summa.place(width = 100, height = 115, x = 590, y = 15)

def add_4():
    sps_4.append(int(inp_1.get()))
    print(sps_4)
    button_summa= Button(text= 'посчитать', bg = '#57ca5d', command = l)
    button_summa.place(width = 100, height = 115, x = 590, y = 15)

# СМЕНА ТОВАРОВ (подмена кнопок и лейблов)
def tovar_1():
    label_tovar = Label(text = 'введите кол-во гирлянд: ', bg = '#b9b9b9')
    label_tovar.place(x=15 , y=80 , height=50 , width=215)
    button_01 = Button(text = 'добавить', command = add_1, bg = '#632020')
    button_01.place(width = 100, height = 115, x = 475, y = 15)
def tovar_2():
    label_tovar = Label(text = 'введите кол-во петард: ', bg = '#b9b9b9')
    label_tovar.place(x=15 , y=80 , height=50 , width=215)
    button_01 = Button(text = 'добавить', command = add_2, bg = '#632020')
    button_01.place(width = 100, height = 115, x = 475, y = 15)
def tovar_3():
    label_tovar = Label(text = 'введите кол-во звезд: ', bg = '#b9b9b9')
    label_tovar.place(x=15 , y=80 , height=50 , width=215)
    button_01 = Button(text = 'добавить', command = add_3, bg = '#632020')
    button_01.place(width = 100, height = 115, x = 475, y = 15)
def tovar_4():
    label_tovar = Label(text = 'введите кол-во елок: ', bg = '#b9b9b9')
    label_tovar.place(x=15 , y=80 , height=50 , width=215)
    button_01 = Button(text = 'добавить', command = add_4, bg = '#632020')
    button_01.place(width = 100, height = 115, x = 475, y = 15)
    

# кнопка 1 товара
button_1= Button(text= 'гирлянда = 100р', command = tovar_1)
button_1.place(width = 100, height = 50, x = 15, y = 15)
# кнопка 2 товара 
button_2= Button(text= 'петарда = 50р', command = tovar_2)
button_2.place(width = 100, height = 50, x = 130, y = 15)
# кнопка 3 товара
button_3= Button(text= 'звезда = 75р', command = tovar_3)
button_3.place(width = 100, height = 50, x = 245, y = 15)
# кнопка 4 товара
button_4= Button(text= 'елка = 500р', command = tovar_4)
button_4.place(width = 100, height = 50, x = 360, y = 15)

# лейбл с суммой
def l():
    summa = (sum(sps_1) * 100)+(sum(sps_2) * 50)+(sum(sps_3) * 75)+(sum(sps_4) * 500)
    label_sum = Label(text = f'{summa}₽', bg = '#da47b5')
    label_sum.place(width = 100, height = 115, x = 705, y = 15)



window.mainloop()