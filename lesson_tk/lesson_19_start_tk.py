# импортируем библиотеку tkinter
from tkinter import *



# создаём окно 
window = Tk()
# меняем название окна
window.title("hello")
# меняем ширину и высоту окна 
window.geometry("600x500")



# создаём текст через Label
# bg= цвет фона 
# fg= цвет текстам
lab_text = Label(text="asryffgvg", bg="#dfc062" , fg = "#6600FF")
# placе - позиция и размер элемента
lab_text.place(x=10 , y=40 , width=200 , height=20)



# font = шрифт и размер текста 
lab_text_2 = Label(text="www2" , font= ("MV Boli" , 15))
# anchor позиционирование относительно окна
lab_text_2.place(relx=0.5, rely=0.5 , anchor="center")

lab_text_x = Label(text="ebfbfb" , font= ("MV Boli" , 15))
# anchor позиционирование относительно окна
lab_text_x.place(relx=0.5, rely=0.8 , anchor="center")



num_f_1_glogal = 10
def fun_1():
    print("you click button")
    global num_f_1_glogal
    num_f_1_glogal += 20
    # изменяем позиция lab_text
    lab_text.place(x=num_f_1_glogal , y=num_f_1_glogal)
# создаём кнопку command вызывает функцию
button_b1 = Button(text="but click" , command = fun_1)
button_b1.place(x=20 , y=150)



num_f_1_glogal = 10
def fun_2():
    # с помощью метода configure или config можно изменить параметры объекта 
    lab_text_2.config(bg="#c64b4b" , fg="white" , text="fff2")
    # lab_text_2.configure

button_b2 = Button(text="but click2" , command = fun_2)
button_b2.place(x=90 , y=150)



def fun_3():
    # window.geometry() выводит ширину высоту и координаты окна 
    lab_text_2.config(text=window.geometry())
button_b3 = Button(text="get geometry" , command = fun_3)
button_b3.place(x=200 , y=150)



window.mainloop()