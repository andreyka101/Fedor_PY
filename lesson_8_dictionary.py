#FIXME - создание словаря
obj = {
    "key":50,
    "qwert":"w",
    4:90,
    "5":"0=",
}


#FIXME - получаем значение по ключу
print(obj["key"])
print(obj["5"])
print(obj[4])


#FIXME - словарь это список
obj_arr = {
    0:2,
    1:3,
    2:4,
    3:5,
}
print(obj_arr[2])


#NOTE - metods

#FIXME - очищает словарь
obj_arr_2 = obj_arr.copy() 


#FIXME - возвращает копию словаря
obj_arr.clear()
print(obj_arr)


#FIXME - возвращает значение ключа, но если его нет возвращает None
print(obj.get("5"))
# print(obj["7"])
print(obj.get("7"))
if(obj.get("5") != None):
    print("ok")


#FIXME - возвращает список ключей
print(obj.keys())


#FIXME - возвращает список значений
print(obj.values())


#FIXME - удаляет по ключ и возвращает значение
# num = obj.pop("5")
# print(num)
# print(obj)


#FIXME - удаляет последнюю пару и возвращает её
# print(obj.popitem())
# print(obj)


#FIXME - obj.setdefault(key, val) - возвращает значение key, но если его нет создает key со значением val или None
# obj.setdefault("7",888)
# print(obj)


#FIXME - obj.update(dist) - обновляет словарь obj, добавляя пары словаря dist
obj.update({"5":555})
print(obj)




#NOTE - способ использования словаря
str_num = input("__")

# if(str_num == "q"):
#     print("ok q")
# elif(str_num == "w"):
#     print("ok w")
# elif(str_num == "e"):
#     print("ok e")
# elif(str_num == "r"):
#     print("ok r")
# elif(str_num == "t"):
#     print("ok t")



print(str_num)
if_dist_obj = {
    "q": "ok q",
    "w": "ok w",
    "e": "ok e",
    "r": "ok r",
    "t": "ok t",
}
if(obj.get(str_num) != None):
    print(if_dist_obj[str_num])



#REVIEW - забыл рассказать
#FIXME - создание ключ, значения через []
print(if_dist_obj)
# если в квадратных скобках написать ключ которого нет то он создаётся 
if_dist_obj["new_key"] = 999
print(if_dist_obj)

# также можно менять значение в существующих ключах
if_dist_obj["r"] = "67r76"
print(if_dist_obj)




#NOTE - дз
# лёгкая сложность задание 1
# создайте два словаря объедените их и выведите в консоль


# средняя сложность задание 2
# Создайте словарь, в котором ключами будут числа от 1 до 10, 
# а значениями эти же числа, возведенные в куб


# средняя сложность задание 3
# Создайте словарь из строки 'pythonist' следующим образом: 
# в качестве ключей возьмите символ строки, 
# а значениями пусть будет индекс символа


# сложная сложность задание 4
# Даны два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, 
# чтобы элементы первого списка были ключами, 
# а элементы второго — соответственно значениями нашего словаря.
