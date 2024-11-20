
from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


# Listbox - 
arr = [1,2,3,4,5]
list_box_lab = Listbox(listvariable = Variable(value=arr))
list_box_lab.place(x=10 , y = 10)

lab_text = Label(text= "none")
lab_text.place(x=10 , y=200)


inp_enter = Entry()
inp_enter.place(x=170 , y=20 , height=30 , width=200)



def fun_get_index():
    lab_text.config(text= list_box_lab.curselection())
button_in_1 = Button(text="get_index" , command = fun_get_index)
button_in_1.place(x=10 , y=230)



def fun_create():
    list_box_lab.insert( 0 , inp_enter.get())
    lab_text.config(text= list_box_lab.curselection())
button_in_2 = Button(text="create" , command = fun_create)
button_in_2.place(x=10 , y=260)





def fun_get_element():
    lab_text.config(text= list_box_lab.get(list_box_lab.curselection()))
button_in_3 = Button(text="get_element" , command = fun_get_element)
button_in_3.place(x=10 , y=290)




def fun_del():
    list_box_lab.delete(list_box_lab.curselection())

button_in_4 = Button(text="del" , command = fun_del)
button_in_4.place(x=10 , y=320)




def fun_change():
    list_box_lab.insert(list_box_lab.curselection() , "=====")
    list_box_lab.delete(list_box_lab.curselection())
    lab_text.config(text= list_box_lab.curselection())
button_in_1 = Button(text="change" , command = fun_change)
button_in_1.place(x=10 , y=350)




window.mainloop()