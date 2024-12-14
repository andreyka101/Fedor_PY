from tkinter import *

window = Tk()
window.title("window")
# меняем ширину высоту и координаты окна
window.geometry("600x500+200+300")
# цвет окна
window.config(bg="#facca6")



# пример удаления Label
lab = Label(text="asryffgvg", bg="#dfc062" , fg = "#6600FF")
lab.place(x=10 , y=40)
def fun_del():
    # del lab
    lab.place(x=-100 , y=-100)
button_del = Button(text="delete Label" , command = fun_del)
button_del.place(x=10 , y=80)





inp_enter = Entry()
inp_enter.place(x=20 , y=200)

def fun_in_1():
    print(inp_enter.get())
    window.geometry(inp_enter.get())
    
    
button_in_1 = Button(text="run" , command = fun_in_1)
button_in_1.place(x=20 , y=230)





inp_enter_color = Entry()
inp_enter_color.place(x=200 , y=200)

def fun_in_2():
    print(inp_enter_color.get())
    # меняем ширину высоту и координаты окна через Entry
    window.config(bg=inp_enter_color.get())
    
    
button_in_2 = Button(text="run color" , command = fun_in_2 )
button_in_2.place(x=200 , y=230)







window.mainloop()