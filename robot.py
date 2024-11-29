from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")
window.resizable(False, False)


robot_coordinates = {
    "x" : 0,
    "y" : 0
}

def fun_press(event):
    if(event.keysym != "d" and event.keysym != "a" and event.keysym != "w" and event.keysym != "s"):
        return 
    
    print("ok")
    if(event.keysym == "d" and robot_coordinates["x"] < 550):
        robot_coordinates["x"] += 50
    if(event.keysym == "a" and robot_coordinates["x"] > 0):
        robot_coordinates["x"] -= 50
        
    if(event.keysym == "s" and robot_coordinates["y"] < 450):
        robot_coordinates["y"] += 50
    if(event.keysym == "w" and robot_coordinates["y"] > 0):
        robot_coordinates["y"] -= 50
    robot.place(x=robot_coordinates["x"] , y=robot_coordinates["y"])


# def fun_release(event):
#     print("0")



window.bind("<KeyPress>" , fun_press)
# window.bind("<KeyRelease>" , fun_release)


robot = Label(bg="#360a9c")
robot.place(x=0 , y=0 , width=50 , height=50)


window.mainloop()