from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)


old_x = -10
old_y = -10

# движение мыши
def fun_b1(event):
    global old_x , old_y
    if(old_x == -10):
        old_x = event.x
        old_y = event.y
    
    canV.create_line(old_x ,old_y , event.x ,event.y , fill="#232323" ,width=5)
    old_x = event.x
    old_y = event.y


canV.bind("<B1-Motion>" , fun_b1)



# движение мыши
def fun_b2(event):
    # print(num_bool)
    # создаём oval
    canV.create_oval(event.x - 50/2 , event.y - 50/2 , event.x + 50 , event.y + 50 , fill="#ffffff" ,width=0 , outline="#1da7e2")

canV.bind("<B3-Motion>" , fun_b2)




window.mainloop()