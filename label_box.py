# импортируем библиотеку tkinter
from tkinter import *



window = Tk()
window.geometry("500x500")




lab_box_1 = Label(bg="#28ffd4")
lab_box_1.place(x=0 , y=0 , width= 250 , height=250)
lab_box_2 = Label(bg="#28ffd4")
lab_box_2.place(x=250 , y=0 , width= 250 , height=250)
lab_box_3 = Label(bg="#28ffd4")
lab_box_3.place(x=0 , y=250 , width= 250 , height=250)
lab_box_4 = Label(bg="#28ffd4")
lab_box_4.place(x=250 , y=250 , width= 250 , height=250)

lab_text = Label(text="text" , font= ("" , 14))
lab_text.place(x=20 , y=200)




def but_L(event):
    # lab_text.config(text=window.winfo_pointerxy())
    # print(window.winfo_pointerxy())
    # print(window.winfo_pointerxy()[0])

    x,y = window.winfo_pointerxy()
    lab_text.config(text=window.winfo_containing(x , y))
    element_id = window.winfo_containing(x , y)
    # print(type(window.winfo_containing(x , y)))
    if(str(element_id) == ".!label" or str(element_id) == ".!label2" or str(element_id) == ".!label3" or str(element_id) == ".!label4"):
        element_id.config(bg="#16473d")
    

window.bind("<Button-1>" , but_L)




window.mainloop()