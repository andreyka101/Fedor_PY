from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)

# список координат для квадратов
arr_but = [
    {
        "x1":30,
        "y1":30,
        "x2":70,
        "y2":70,
        "hover":True,
    },
    {
        "x1":200,
        "y1":30,
        "x2":270,
        "y2":100,
        "hover":True,
    },
]

# рисуем квадрат и текст
for el in arr_but:
    canV.create_rectangle(el["x1"] , el["y1"] , el["x2"] , el["y2"], fill="#f21a1a", width=0)
    # canV.create_text(el["x1"] + 30 , el["y1"] + 30  ,text = "Hello" ,font="Boli 15" , fill="#184112" , justify="center")



def fun_b1(event):
    for el in arr_but:
        print(el)
        print("====")
        # при нажатии на квадрат меняем ему цвет
        if((el["x1"] <= event.x and el["x2"] >= event.x) and (el["y1"] <= event.y and el["y2"] >= event.y)):
            canV.create_rectangle(el["x1"] , el["y1"] , el["x2"] , el["y2"], fill="#1aebf2", width=0)
            el["hover"] = False
        # при нажатии на пустое место (вне квадрата) меняем ему цвет обратно 
        if((el["x1"] >= event.x or el["x2"] <= event.x) or (el["y1"] >= event.y or el["y2"] <= event.y)):
            canV.create_rectangle(el["x1"] , el["y1"] , el["x2"] , el["y2"], fill="#f21a1a", width=0)
            el["hover"] = True
canV.bind("<Button-1>" , fun_b1)



def mouse_motion(event):
    window.title(str(event.x) + " / " + str(event.y))
    for el in arr_but:
        # при наведении на квадрат меняем ему цвет если он не нажат
        if(((el["x1"] <= event.x and el["x2"] >= event.x) and (el["y1"] <= event.y and el["y2"] >= event.y)) and el["hover"]):
            canV.create_rectangle(el["x1"] , el["y1"] , el["x2"] , el["y2"], fill="#e7ce44", width=0)
        # при наведении на пустое место (вне квадрата) меняем ему цвет обратно если он не нажат
        if(((el["x1"] >= event.x or el["x2"] <= event.x) or (el["y1"] >= event.y or el["y2"] <= event.y)) and el["hover"]):
            canV.create_rectangle(el["x1"] , el["y1"] , el["x2"] , el["y2"], fill="#f21a1a", width=0)
canV.bind("<Motion>" , mouse_motion)

window.mainloop()