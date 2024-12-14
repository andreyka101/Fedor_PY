from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#979797")



# ввод данных
inp_enter = Entry()
inp_enter.place(x=20 , y=20 , height=30 , width=200)


def fun_in_1():
    # inp_enter.insert(0, "Hello World") # добавляет "Hello World" в конец
    
    # inp_enter.get() - возвращает текст Entry
    print(inp_enter.get())
    if(inp_enter.get() != ""):
        lab_text.config(text=inp_enter.get())
        lab_text.place(x=10 , y=40)
    else:
        lab_text.place(x=-110 , y=-110)
    
button_in_1 = Button(text="run" , command = fun_in_1)
button_in_1.place(x=10 , y=80)

lab_text = Label(text="none" , fg = "#350184")
lab_text.place(x=10 , y=40)






window.mainloop()