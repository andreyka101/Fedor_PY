from tkinter import *

window = Tk()
window.title('calculator')
w, h = 285, 360
window.geometry(f"{w}x{h}+{(window.winfo_screenwidth()-w)//2}+{(window.winfo_screenheight()-h)//2}")
window.config(bg = '#bebebe')
window.resizable(False, False)

l_input = Label()
l_input.place(x=30 , y=30 , width= 230 , height=50)


n_1 = Button(text="1" , border=1)
n_1.place(h=50, w=50, x=30 , y= 100)
n_2 = Button(text="2" , border=1)
n_2.place(h=50, w=50, x=90 , y= 100)
n_3 = Button(text="3" , border=1)
n_3.place(h=50, w=50, x=150 , y= 100)
n_4 = Button(text="4" , border=1)
n_4.place(h=50, w=50, x=30 , y= 160)
n_5 = Button(text="5" , border=1)
n_5.place(h=50, w=50, x=90 , y= 160)
n_6 = Button(text="6" , border=1)
n_6.place(h=50, w=50, x=150 , y= 160)
n_7 = Button(text="7" , border=1)
n_7.place(h=50, w=50, x=30 , y= 220)
n_8 = Button(text="8" , border=1)
n_8.place(h=50, w=50, x=90 , y= 220)
n_9 = Button(text="9" , border=1)
n_9.place(h=50, w=50, x=150 , y= 220)
n_0 = Button(text="0" , border=1)
n_0.place(h=50, w=50, x=90 , y= 280)
n_clear = Button(text="C" , border=1, bg = '#ff8282')
n_clear.place(h=50, w=50, x=30 , y= 280)
n_equ = Button(text="=" , border=1, bg = '#9fff82')
n_equ.place(h=50, w=50, x=150 , y= 280)

b_m = Button(text="-" , border=1, bg = '#e8ff82')
b_m.place(h=50, w=50, x=210 , y= 100)
b_p = Button(text="+" , border=1, bg = '#e8ff82')
b_p.place(h=50, w=50, x=210 , y= 160)
b_d = Button(text="/" , border=1, bg = '#e8ff82')
b_d.place(h=50, w=50, x=210 , y= 220)
b_mu = Button(text="*" , border=1, bg = '#e8ff82')
b_mu.place(h=50, w=50, x=210 , y= 280)


text_f = ''
znak = ''

def click(event):
    button_element = event.widget
    l_input.config(text=button_element["text"])
    global text_f
    global znak
    if(button_element["text"] == "1"):
        text_f += '1'
    if(button_element["text"] == "2"):
        text_f += '2'
    if(button_element["text"] == "3"):
        text_f += '3'
    if(button_element["text"] == "4"):
        text_f += '4'
    if(button_element["text"] == "5"):
        text_f += '5'
    if(button_element["text"] == "6"):
        text_f += '6'
    if(button_element["text"] == "7"):
        text_f += '7'
    if(button_element["text"] == "8"):
        text_f += '8'
    if(button_element["text"] == "9"):
        text_f += '9'
    if(button_element["text"] == "0"):
        text_f += '0'
    if(button_element["text"] == "C"):
        text_f = ''
    if(button_element["text"] == "+"):
        znak = '+'
        text_f += '+'
    if(button_element["text"] == "-"):
        znak = '-'
        text_f += '-'
    if(button_element["text"] == "*"):
        znak = '*'
        text_f += '*'
    if(button_element["text"] == "/"):
        znak = '/'
        text_f += '/'

    l_input.config(text = text_f)

    if(button_element["text"] == "="):
        if znak == '+':
            result = text_f.split('+')
            result = [int(x) for x in result]
            result_f = result[0] + result[1]
            l_input.config(text = result_f)
        if znak == '-':
            result = text_f.split('-')
            result = [int(x) for x in result]
            result_f = result[0] - result[1]
            l_input.config(text = result_f)
        if znak == '*':
            result = text_f.split('*')
            result = [int(x) for x in result]
            result_f = result[0] * result[1]
            l_input.config(text = result_f)
        if znak == '/':
            result = text_f.split('/')
            result = [int(x) for x in result]
            result_f = (result[0] / result[1])
            if result[0] % result [1] == 0:
                l_input.config(text = int(result_f)) 
            else:
                l_input.config(text = float(result_f)) 
                
            
n_1.bind("<Button-1>" , click)
n_2.bind("<Button-1>" , click)
n_3.bind("<Button-1>" , click)
n_4.bind("<Button-1>" , click)
n_5.bind("<Button-1>" , click)
n_6.bind("<Button-1>" , click)
n_7.bind("<Button-1>" , click)
n_8.bind("<Button-1>" , click)
n_9.bind("<Button-1>" , click)
n_0.bind("<Button-1>" , click)
n_clear.bind("<Button-1>" , click)
n_equ.bind("<Button-1>" , click)
b_m.bind("<Button-1>" , click)
b_d.bind("<Button-1>" , click)
b_mu.bind("<Button-1>" , click)
b_p.bind("<Button-1>" , click)




window.mainloop()