from tkinter import *
window = Tk()
window.geometry("600x500")


button_1 = Button(text="button 1")
button_1.place(x=30 , y= 30)
button_2 = Button(text="button 2")
button_2.place(x=30 , y= 60)
button_3 = Button(text="button 3")
button_3.place(x=30 , y= 90)
button_4 = Button(text="button 4")
button_4.place(x=30 , y= 120)

lab_text_1 = Label(text="text" , font= ("" , 14))
lab_text_1.place(x=20 , y=200)
lab_text_2 = Label(text="efefe" , font= ("" , 14))
lab_text_2.place(x=20 , y=250)


num=0
def click(event):
    # lab_text_1.config(text=event.widget)
    button_element = event.widget
    lab_text_1.config(text=button_element["text"])
    global num
    if(button_element["text"] == "button 1"):
        num += 1
    if(button_element["text"] == "button 2"):
        num += 2
    if(button_element["text"] == "button 3"):
        num += 3
    if(button_element["text"] == "button 4"):
        num += 4
    lab_text_2.config(text=num)



button_1.bind("<Button-1>" , click)
button_2.bind("<Button-1>" , click)
button_3.bind("<Button-1>" , click)
button_4.bind("<Button-1>" , click)





window.mainloop()