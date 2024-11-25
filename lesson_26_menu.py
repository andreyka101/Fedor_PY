
from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")



def fun_but_1():
    print("open")


main_menu = Menu()

file_menu = Menu(main_menu , tearoff=0)
file_menu.add_command(label="открыть" , command=fun_but_1)

file_menu.add_separator()
file_menu.add_command(label="выход")
file_menu.add_command(label="новый")


num_check = IntVar()
file_menu.add_checkbutton(label="checkbox" , variable = num_check)


numbers = StringVar(value="b1")
file_menu.add_radiobutton(label="123" , value= "b1" , variable= numbers)
file_menu.add_radiobutton(label="456" , value= "b2" , variable= numbers)
file_menu.add_radiobutton(label="789" , value= "b3" , variable= numbers)





number_menu = Menu(file_menu , tearoff=0)
number_menu.add_command(label="1")
number_menu.add_command(label="2")
number_menu.add_command(label="3")


file_menu.add_cascade(label="number" , menu=number_menu)



main_menu.add_cascade(label="файл" , menu=file_menu)
main_menu.add_cascade(label="number" , menu=number_menu)
window.config(menu=main_menu)


window.mainloop()