from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


obj = {}

def click(event):
    button_element = event.widget
    if(button_element["text"] == 0):
        window.config(bg="#ffffff")
    if(button_element["text"] == 1):
        window.config(bg="#c7c7c7")
    if(button_element["text"] == 2):
        window.config(bg="#858585")
    if(button_element["text"] == 3):
        window.config(bg="#575757")
    if(button_element["text"] == 4):
        window.config(bg="#171717")


for i in range(5):
    obj[f'button_n{i}'] = Button(text=i)
    obj[f'button_n{i}'].place(x = 30 , y=30*i)
    obj[f'button_n{i}'].bind("<Button-1>" , click)



window.mainloop()