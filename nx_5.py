from tkinter import *
import PIL
from PIL import Image, ImageDraw

window = Tk()
window.title("window")
window.geometry("1000x1000")
window.config(bg="#facca6")
window.resizable(False, False)
window.option_add("*tearOff", FALSE)

# функция сохранения 
save_n = 0
def save():
    global save_n
    filename = f'image{save_n}.png'
    image1.save(filename)
    save_n += 1

# функции изменения размеров кисти
size = 20
def size_small():
    global size
    size = 7
def size_medium():
    global size
    size = 20
def size_big():
    global size
    size = 50

# функции изменения цвета кисти
color = '#000000'
def c_black():
    global color
    color = '#000000'
def c_red():
    global color
    color = '#ff0000'
def c_green():
    global color
    color = '#2bff00'

# функция рисования овалом
def brush(a):
    canV.create_oval(a.x , a.y , a.x + size , a.y + size , fill=color ,width=0 , outline="#000000")
    draw.line((a.x, a.y, a.x + size, a.y + size), fill=color, width=10)

# создание общего меню
main_menu = Menu(window) 
window.config(menu=main_menu)
# создание меню ФАЙЛ-СОХРАНИТЬ
file_menu = Menu(main_menu)
file_menu.add_command(label="save png", command = save)
# создание меню КИСТЬ и подменю РАЗМЕР, ЦВЕТ
brush_menu = Menu(main_menu)
size_menu = Menu(brush_menu)
color_menu = Menu(brush_menu)
brush_menu.add_cascade(label='size', menu=size_menu)
brush_menu.add_cascade(label="color", menu=color_menu)
# создание подменю РАЗМЕР - 
numbers = StringVar(value="b2")
size_menu.add_radiobutton(label="small" , value= "b1" , variable= numbers, command = size_small)
size_menu.add_radiobutton(label="medium" , value= "b2" , variable= numbers, command = size_medium)
size_menu.add_radiobutton(label="big" , value= "b3" , variable= numbers, command = size_big)
# создание подменю ЦВЕТ - 
colors = StringVar(value="b1")
color_menu.add_radiobutton(label="black" , value= "b1" , variable= colors, command = c_black)
color_menu.add_radiobutton(label="red" , value= "b2" , variable= colors, command = c_red)
color_menu.add_radiobutton(label="green" , value= "b3" , variable= colors, command = c_green)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Brush", menu=brush_menu)

# cоздание канвас холста
canV = Canvas(width=1000 , height= 1000 , bg="#ffffff")
canV.place(x=0,y=0)

# cохранение рисунка в файл
image1 = PIL.Image.new('RGB', (1000, 1000), 'white')
draw = ImageDraw.Draw(image1)

canV.bind("<B1-Motion>" , brush)


window.mainloop()