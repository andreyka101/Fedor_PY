from tkinter import * 
from PIL import ImageTk, Image
import time
import random
import keyboard
import sys
import os
import subprocess
import pygame
import threading


window = Tk()
window.title('game')
window.geometry('600x600')
window.resizable(False, False)
Game_Window = Canvas(window, height = 600, width=600, bg = '#9f9f9f')
Game_Window.place(x=0, y=0)

# счетчик очков 
game_on = True
point = 0

# звуки
pygame.mixer.init()
sound_move = pygame.mixer.Sound('s_m.mp3')
sound_crash = pygame.mixer.Sound('s_cr.mp3')
sound_crash_played = False

def play_sound_crash():
    global sound_crash_played
    if not sound_crash_played:
        sound_crash.play()
        sound_crash_played = True  

def sound_move_play():
    sound_move.play()

# СОЗДАНИЕ АВТОМОБИЛЯ ИГРОКА
# Загружаем первую анимацию (с 2 кадрами)
gif_image_1 = Image.open('self_car_v1_gif.gif')
frames_1 = []
for frame in range(gif_image_1.n_frames):
    gif_image_1.seek(frame)
    frame_image = ImageTk.PhotoImage(gif_image_1.copy())
    frames_1.append(frame_image)
# Загружаем анимацию авто врага(с 2 кадрами)
enemy_image_load = Image.open('enemy_car_v1_gif.gif')
frames_12 = []
for frame in range(enemy_image_load.n_frames):
    enemy_image_load.seek(frame)
    frame_image = ImageTk.PhotoImage(enemy_image_load.copy())
    frames_12.append(frame_image)
# Загружаем вторую анимацию (с 7 кадрами)
gif_image_2 = Image.open('road_gif.gif')
frames_2 = []
for frame in range(gif_image_2.n_frames):
    gif_image_2.seek(frame)
    frame_image = ImageTk.PhotoImage(gif_image_2.copy())
    frames_2.append(frame_image)
# Создаем изображение на холсте для второй гифки (road) - будет находиться внизу
road = Game_Window.create_image(300, 300, image=frames_2[0])
# СОЗДАНИЕ АВТОМОБИЛЕЙ ПРОТИВНИКОВ
enemy_car_1 = Game_Window.create_image(240, 0,image = frames_12[0])
enemy_car_2 = Game_Window.create_image(300, 0,image = frames_12[0])
enemy_car_3 = Game_Window.create_image(360, 0,image = frames_12[0])
# Создаем изображение на холсте для первой гифки (your_car) - будет поверх
your_car = Game_Window.create_image(300, 300, image=frames_1[0])
# Функция для анимации первой гифки
def animate_gif_1(frame=0):
    if game_on is True:
        Game_Window.itemconfig(your_car, image=frames_1[frame])  # Обновляем изображение первой гифки
        next_frame = (frame + 1) % len(frames_1)  # Переход к следующему кадру
        Game_Window.after(100, animate_gif_1, next_frame)  # Повторяем через 100 мс
    else:
        return
def animate_gif_12(frame=0):
    if game_on is True:
        Game_Window.itemconfig(enemy_car_1, image=frames_12[frame])  # Обновляем изображение первой гифки
        Game_Window.itemconfig(enemy_car_2, image=frames_12[frame])  # Обновляем изображение первой гифки
        Game_Window.itemconfig(enemy_car_3, image=frames_12[frame])  # Обновляем изображение первой гифки
        next_frame = (frame + 1) % len(frames_12)  # Переход к следующему кадру
        Game_Window.after(100, animate_gif_12, next_frame)  # Повторяем через 100 мс
    else:
        return
# Функция для анимации второй гифки
def animate_gif_2(frame=0):
    if game_on is True:
        Game_Window.itemconfig(road, image=frames_2[frame])  # Обновляем изображение второй гифки
        next_frame = (frame + 1) % len(frames_2)  # Переход к следующему кадру
        Game_Window.after(100, animate_gif_2, next_frame)  # Повторяем через 100 мс
    else:
        return
# Запускаем анимации обеих гифок
animate_gif_1()
animate_gif_2()
animate_gif_12()
# счетчик очков
p_text = Game_Window.create_text(100,50, text = 0, font='PixelifySans 48')
def Points(): 
    if game_on == True:
        global point 
        point += 1 
        Game_Window.itemconfig(p_text, text = point)
        Game_Window.after(100, Points)
        
Game_Window.after(1, Points)
'''горизонтальные координнаты'''
x1 = 60
y1 = 0
'''вертикальные координнаты'''
x2 = 0
y2 = 50

'''движение по 4 сторонам'''
def Move_Left(a):
    pos = Game_Window.coords(your_car)
    if pos[0] <= 250:
        Game_Window.move(your_car, 0,0)
    else:
        threading.Thread(target=sound_move_play, daemon=True).start()
        Game_Window.move(your_car, -x1, y1)
def Move_Right(d):
    pos = Game_Window.coords(your_car)
    if pos[0] >= 350:
        Game_Window.move(your_car, 0,0)
    else:
        threading.Thread(target=sound_move_play, daemon=True).start()
        Game_Window.move(your_car, x1, y1)
def Move_Forward(w):
    pos = Game_Window.coords(your_car)
    if pos[1] <= 50:
        Game_Window.move(your_car, 0,0)
    else:
        threading.Thread(target=sound_move_play, daemon=True).start()
        Game_Window.move(your_car, x2, -y2)
def Move_Back(s):
    pos = Game_Window.coords(your_car)
    if pos[1] >= 550:
        Game_Window.move(your_car, 0,0)
    else:
        threading.Thread(target=sound_move_play, daemon=True).start()
        Game_Window.move(your_car, x2, y2)

window.bind("<a>", Move_Left)
window.bind("<d>", Move_Right)
window.bind("<w>", Move_Forward)
window.bind("<s>", Move_Back)

'''движение противников по у (speed)'''
enemy_x = 0
enemy_y = 2

# блокируем клаву при окончании игры
def block():
    for key in range(150):
        keyboard.block_key(key)


# УРОВНИ
def Levels():
    global enemy_y
    if point >= 100:
        enemy_y = 3
    if point >= 300:
        enemy_y = 4
    if point >= 500:
        enemy_y = 5
    if point >= 700:
        enemy_y = 6
    if point >= 900:
        enemy_y = 7
    if point >= 1100:
        enemy_y = 8
    if point >= 1300:
        enemy_y = 9
    if point >= 1500:
        enemy_y = 10
    if point >= 1777:
        Game_Complete()
    else:
        return


# кнопка рестарта
def Restart():
    python = sys.executable  # Путь к текущему интерпретатору Python
    script_path = os.path.join(os.getcwd(), "nx_6.py")  # Абсолютный путь к скрипту
    # Запускаем новый процесс
    subprocess.Popen([python, script_path] + sys.argv)
    Game_Window.destroy()
    window.quit()

btn = Button(window, text='restart', width=20, height=3, bd='0', command= Restart)
btn.place(x=-50, y=-50)
canvas_widget = Game_Window.create_window(-50, -50, window=btn)

def Res_But():  
    btn.place(x=425, y=25)
    
# функция конца игры
def Game_Over():
    play_sound_crash()
    block()
    Res_But()
    global enemy_y
    global game_on
    enemy_y = 0
    Game_Window.create_text(300,300, text='game over', font = 'PixelifySans 48')
    game_on = False

# игра пройдена!
def Game_Complete():
    block()
    global enemy_y
    global game_on
    enemy_y = 0
    Game_Window.create_text(300, 300, text='game complete!', font = 'PixelifySans 48')
    game_on = False    

# функция движения противников  
def Enemy_Move():
    pos_1 = Game_Window.coords(enemy_car_1)
    pos_2 = Game_Window.coords(enemy_car_2)
    pos_3 = Game_Window.coords(enemy_car_3)
    c_1 = 100
    c_2 = 1100
    c_3 = 200

    if pos_1[1] >= 700 and pos_2[1] >= 700 and pos_3[1] >= 700 :
        Game_Window.move(enemy_car_1, enemy_x, enemy_y - pos_1[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 1ой машины{Game_Window.coords(enemy_car_1)}')
        Game_Window.move(enemy_car_2, enemy_x, enemy_y - pos_2[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 2ой машины{Game_Window.coords(enemy_car_2)}')
        Game_Window.move(enemy_car_3, enemy_x, enemy_y - pos_3[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 3ой машины{Game_Window.coords(enemy_car_3)}')
    # исключает генерацию машин на одной линии
    if pos_1[1] == pos_2[1] and pos_2[1] == pos_3[1]:
        Game_Window.move(enemy_car_1, enemy_x, enemy_y - pos_1[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 1ой машины{Game_Window.coords(enemy_car_1)}')
        Game_Window.move(enemy_car_2, enemy_x, enemy_y - pos_2[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 2ой машины{Game_Window.coords(enemy_car_2)}')
        Game_Window.move(enemy_car_3, enemy_x, enemy_y - pos_3[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 3ой машины{Game_Window.coords(enemy_car_3)}')
        print('машины на одной линии предотвращены')
    # исключаем другие непроходимые комбинации машин
    if pos_1[1] == pos_2[1] +200 and pos_1[1] == pos_2[1] +400 or pos_1[1] == pos_2[1] -200 and pos_1[1] == pos_2[1] -400 :
        Game_Window.move(enemy_car_1, enemy_x, enemy_y - pos_1[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 1ой машины{Game_Window.coords(enemy_car_1)}')
        Game_Window.move(enemy_car_2, enemy_x, enemy_y - pos_2[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 2ой машины{Game_Window.coords(enemy_car_2)}')
        Game_Window.move(enemy_car_3, enemy_x, enemy_y - pos_3[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 3ой машины{Game_Window.coords(enemy_car_3)}')
        print('первая непроходимая вариация предотвращена')
    if pos_1[1] == pos_2[1] and pos_1[1] == pos_3[1] +200 or pos_1[1] == pos_2[1] and pos_1[1] == pos_3[1] -200 :
        Game_Window.move(enemy_car_1, enemy_x, enemy_y - pos_1[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 1ой машины{Game_Window.coords(enemy_car_1)}')
        Game_Window.move(enemy_car_2, enemy_x, enemy_y - pos_2[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 2ой машины{Game_Window.coords(enemy_car_2)}')
        Game_Window.move(enemy_car_3, enemy_x, enemy_y - pos_3[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 3ой машины{Game_Window.coords(enemy_car_3)}')
        print('вторая непроходимая вариация предотвращена')
    if pos_1[1] == pos_2[1] +200 and pos_1[1] == pos_3[1] +200 or pos_1[1] == pos_2[1] -200 and pos_1[1] == pos_3[1] -200 :
        Game_Window.move(enemy_car_1, enemy_x, enemy_y - pos_1[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 1ой машины{Game_Window.coords(enemy_car_1)}')
        Game_Window.move(enemy_car_2, enemy_x, enemy_y - pos_2[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 2ой машины{Game_Window.coords(enemy_car_2)}')
        Game_Window.move(enemy_car_3, enemy_x, enemy_y - pos_3[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 3ой машины{Game_Window.coords(enemy_car_3)}')
        print('третья непроходимая вариация предотвращена')
    if pos_1[1] == pos_2[1] +200 and pos_1[1] == pos_3[1] or pos_1[1] == pos_2[1] -200 and pos_1[1] == pos_3[1] :
        Game_Window.move(enemy_car_1, enemy_x, enemy_y - pos_1[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 1ой машины{Game_Window.coords(enemy_car_1)}')
        Game_Window.move(enemy_car_2, enemy_x, enemy_y - pos_2[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 2ой машины{Game_Window.coords(enemy_car_2)}')
        Game_Window.move(enemy_car_3, enemy_x, enemy_y - pos_3[1] - ((random.randrange(c_1,c_2,c_3) +enemy_y)))
        print (f'координаты 3ой машины{Game_Window.coords(enemy_car_3)}')
        print('четвертая непроходимая вариация предотвращена')

    # условия конца игры
    your_coords = Game_Window.coords(your_car)
    first_enemy_coords = Game_Window.coords(enemy_car_1)
    second_enemy_coords = Game_Window.coords(enemy_car_2)
    third_enemy_coords = Game_Window.coords(enemy_car_3)
    box_list = [90,-90]
    if your_coords[0] == first_enemy_coords[0] and your_coords[1]  == first_enemy_coords[1] or your_coords[0] == first_enemy_coords[0] and your_coords[1]  == first_enemy_coords[1] + box_list[0] or your_coords[0] == first_enemy_coords[0] and your_coords[1]  == first_enemy_coords[1] + box_list[1]:
        Game_Over()
    if your_coords[0] == second_enemy_coords[0] and your_coords[1]  == second_enemy_coords[1] or your_coords[0] == second_enemy_coords[0] and your_coords[1]  == second_enemy_coords[1] + box_list[0] or your_coords[0] == second_enemy_coords[0] and your_coords[1]  == second_enemy_coords[1] + box_list[1]:
        Game_Over()
    if your_coords[0] == third_enemy_coords[0] and your_coords[1]  == third_enemy_coords[1] or your_coords[0] == third_enemy_coords[0] and your_coords[1]  == third_enemy_coords[1] + box_list[0] or your_coords[0] == third_enemy_coords[0] and your_coords[1]  == third_enemy_coords[1] + box_list[1]:
        Game_Over()
    else:
        Game_Window.move(enemy_car_1, enemy_x, enemy_y)
        Game_Window.move(enemy_car_2, enemy_x, enemy_y)
        Game_Window.move(enemy_car_3, enemy_x, enemy_y)

# что бы все было хорошо     
# Изменение цикла игры
def game_loop():
    if game_on:  # Проверка, если игра все еще идет
        Enemy_Move()  # Двигаем врагов
        Levels()  # Устанавливаем уровни
        window.after(10, game_loop)  # Повторяем функцию через 10 мс

# Запускаем игровой цикл
window.after(10, game_loop)  # Запускаем цикл игры

window.mainloop()  # Основной цикл tkinter