from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)

square_obj = {
    "x1":0,
    "y1":0,
    "x2":50,
    "y2":50,
}



def fun_press(event):
    if(event.keysym != "d" and event.keysym != "a" and event.keysym != "w" and event.keysym != "s"):
        return 
    
    print("ok")
    if(event.keysym == "d"):
        square_obj["x1"] += 50
        square_obj["x2"] += 50
    if(event.keysym == "a"):
        square_obj["x1"] -= 50
        square_obj["x2"] -= 50
    if(event.keysym == "s"):
        square_obj["y1"] += 50
        square_obj["y2"] += 50
    if(event.keysym == "w"):
        square_obj["y1"] -= 50
        square_obj["y2"] -= 50
    canV.create_rectangle(0 , 0 , 600 , 500 , fill="#ffffff"  , width=0)
    canV.create_rectangle(square_obj["x1"] , square_obj["y1"] , square_obj["x2"] , square_obj["y2"] , fill="#f21a1a"  , width=0)


# def fun_release(event):
#     print("0")



window.bind("<KeyPress>" , fun_press)
window.mainloop()