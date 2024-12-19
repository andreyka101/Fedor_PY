from tkinter import *
import time

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")


canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)



# анимация простая
# save_time = int(time.time())
# while(save_time+200 != int(time.time())):
#     # print(save_time+20 - int(time.time()))
#     # print(int(time.time()) - save_time)
#     canV.update()
#     canV.create_rectangle(0 , 0 , 600 , 500 , fill="#ffffff"  , width=0)
#     canV.create_rectangle(int(time.time()) - save_time , 5 , int(time.time()) - save_time + 50 , 55 , fill="#ab0606" , outline="#000" )




# анимация с разной скоростью
save_time = int(round(time.time() , 2) * 100)
print(time.time())
print(save_time)
our_time = int(round(time.time() , 2) * 100)
while(save_time+200 != our_time):
    our_time = int(round(time.time() , 2) * 100)
    canV.update()
    canV.create_rectangle(0 , 0 , 600 , 500 , fill="#ffffff"  , width=0)
    canV.create_rectangle(our_time - save_time , 5 , our_time - save_time + 50 , 55 , fill="#ab0606" , outline="#000")




# window.mainloop()