from tkinter import *

window = Tk()
window.title("hello")
window.geometry("600x500")




lab_text = Label(text="asryffgvg", bg="#dfc062" , fg = "#6600FF")
lab_text.place(x=10 , y=40 , width=200 , height=20)



lab_text_2 = Label(text="www2" , font= ("MV Boli" , 15))
lab_text_2.place(relx=0.5, rely=0.5 , anchor="center")



num_f_1_glogal = 10
def fun_1():
    print("you click button")
    global num_f_1_glogal
    num_f_1_glogal += 20
    lab_text.place(x=num_f_1_glogal , y=num_f_1_glogal)
button_b1 = Button(text="but click" , command = fun_1)
button_b1.place(x=20 , y=150)



num_f_1_glogal = 10
def fun_2():
    lab_text_2.config(bg="#c64b4b" , fg="white" , text="fff2")
    # lab_text_2.configure

button_b2 = Button(text="but click2" , command = fun_2)
button_b2.place(x=90 , y=150)



def fun_3():
    lab_text_2.config(text=window.geometry())
button_b3 = Button(text="get geometry" , command = fun_3)
button_b3.place(x=200 , y=150)



window.mainloop()