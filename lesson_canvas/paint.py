from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)

# индикатор нажатия кнопки
num_bool = False


# движение мыши
def fun_b1(event):
    global num_bool
    # print(num_bool)
    # если кнопка нажата
    if(num_bool):
        # создаём oval
        canV.create_oval(event.x , event.y , event.x + 20 , event.y + 20 , fill="#232323" ,width=0 , outline="#1da7e2")
canV.bind("<Motion>" , fun_b1)
# canV.bind("<B1-Motion>" , fun_b1)


# нажатие кнопки
def fun_bPress(event):
    global num_bool
    # print(event.keysym)
    if(event.keysym == "z"):
        num_bool = True
# !!! здесь была моя ошибка
window.bind("<KeyPress>" , fun_bPress)

window.mainloop()