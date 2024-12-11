from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


# создание элемента Canvas
canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)
# рисуем в Canvas с помощью методов



# create_line - создать линию
# fill = цвет
# width = толщина линии
# canV.create_line(10, 10, 300, 300 , 45 , 100 , fill="#a16c00" , width=10)



# create_line - создать квадрат
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
# canV.create_rectangle(20 , 40 , 200 , 250 , fill="#f21a1a"  , width=10 , outline="#1da7e2")



# create_line - создать многоугольник
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
canV.create_polygon(20 , 40 , 200 , 250 , 400 , 300 , 20,400 , fill="#af1bbc" ,width=10 , outline="#1da7e2")



# очистка Canvas
# canV.create_rectangle(0 , 0 , 600 , 500 , fill="#ffffff"  , width=0)



# create_line - создать овал или круг
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
# canV.create_oval(40 , 40 , 250 , 250 , fill="#e9f71f" ,width=0 , outline="#1da7e2")



# create_line - создать текст
# fill = цвет
# font = размер и шрифт
# text = текст
# justify = выравнивание текста
# canV.create_text(300 , 300,text = "Hello eofkek eeff\n iriri\nrreufheuhfeuhf" ,font="Boli 15" , fill="#5e0909" , justify="center")







window.mainloop()