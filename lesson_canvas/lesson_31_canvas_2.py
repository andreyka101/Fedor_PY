from tkinter import *

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


canV = Canvas(width=600 , height= 500 , bg="#ea0909")
canV.place(x=0,y=0)


# start – начальный угол дуги в градусах;
# extent – размер дуги в градусах. Дуга всегда рисуется в направлении 
# против часовой стрелки;
# fill = цвет
# width = толщина линии дуги
# outline = цвет рамки
# canV.create_arc(50 , 50 , 200 , 200, fill="#701717" , start = 50 , extent = 410, width = 5 , outline ="#b2a511")

# canV.create_arc(50 , 50 , 200 , 200, fill="#701717" , start = 50 , extent = 130  , width = 5 , outline ="#b2a511" ,style ='arc')

# canV.create_arc(50 , 50 , 200 , 200, fill="#701717" , start = 50 , extent = 130  , width = 5 , outline ="#b2a511" ,style ='pieslice')

# canV.create_arc(50 , 50 , 200 , 200, fill="#701717" , start = 50 , extent = 130  , width = 5 , outline ="#b2a511" ,style ='chord')


image = PhotoImage(file="pho_2.png")
canV.create_image(50 , 50, image=image)



window.mainloop()
