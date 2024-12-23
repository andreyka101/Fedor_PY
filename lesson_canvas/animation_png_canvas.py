from tkinter import *
import time

window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")
window.iconbitmap(r'icon.ico')


canV = Canvas(width=600 , height= 500 , bg="#fff")
canV.place(x=0,y=0)


save_time = int(round(time.time() , 2) * 100)
print(time.time())
print(save_time)
our_time = int(round(time.time() , 2) * 100)
while(save_time+200 != our_time):
    our_time = int(round(time.time() , 2) * 100)
    canV.update()
    # print(int((our_time - save_time)%100)//10)
    canV.create_rectangle(0 , 0 , 600 , 500 , fill="#ffffff"  , width=0)
    image = PhotoImage(file=f"asset/Sprite-0001_p{int((our_time - save_time)%100)//10}.png")
    canV.create_image(50 , 50, image=image)




window.mainloop()