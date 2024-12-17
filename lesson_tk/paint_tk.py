from tkinter import *
from PIL import Image , ImageTk


window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#00de59")



# создаём фото
# image = Image.open("image_1.jpg")
image = Image.open("pho_2.png")
photo = ImageTk.PhotoImage(image)
lab_photo = Label(image=photo)
lab_photo.place(x=0 , y=0)





window.mainloop()