
from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")



main_menu = Menu()

file_menu = Menu(main_menu , tearoff=0)
# file_menu.add_command(label="открыть" , command=)
file_menu.add_command(label="новый")
file_menu.add_command(label="выход")


main_menu.add_cascade(label="файл" , menu=file_menu)
window.config(menu=main_menu)


window.mainloop()