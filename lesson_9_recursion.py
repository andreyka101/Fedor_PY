
# функция возвращает значение с помощью return 
# def fun_1():
#     return 2
# print(fun_1())

# def fun_2(x):
#     return x * 2
# print(fun_2(4))



# функция возвращает функцию
# def fun_3():
#     print("fun 1")
#     return 0
# def fun_4():
#     print("fun 2")
#     return fun_3()

# print(fun_4())



# функция возвращает функцию и передаёт ей значение
# def fun_5(x):
#     print("fun 5")
#     print(x)
#     return x + 5
# def fun_6(r):
#     print("fun 6")
#     print(r)
#     return fun_5(r + 5)
# print(fun_6(2))



# рекурсия - функция возвращает саму себя
# num_7 = 5
# def fun_7():
#     global num_7
#     print(num_7)
#     num_7 -= 1
#     if(num_7 != 0):
#         return fun_7()
# fun_7()
# print(num_7)



# функция возвращает саму себя и передаёт себе же изменённое значение
# def fun_8(num):
#     if(num != 0):
#         print(num)
#         return fun_8(num - 1)
# fun_8(7)



# тоже саме, но обрабатываем дополнительную переменную value
# def fun_9(value, index = 5):
#     print(value, index)
#     value *= 2
#     if(index > 0):
#         return fun_9(value, index - 1)
#     else:
#         return value

# print(fun_9(10))




# дз
# номер 1
# Напишите функцию для вычисления факториала числа

# номер 2
# Напишите программу для возведения числа n в степень m. 
# нельзя использовать степень (**)

# номер 3
# напишите функцию которая принимает список и возвращает сумму всех чисел списка

# номер 4
# напишите функцию которая принимает два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, 
# чтобы элементы первого списка были ключами, 
# а элементы второго — соответственно значениями нашего словаря.
# функция возвращает словарь

# номер 5
# Напишите функцию которая принимает список чисел и строк и возвращает список с удалёнными строками





# номер 4
# def creat_dist(arr_key , arr_value , index = 0 , dist_save = {}):
#     if(len(arr_key) != len(arr_value)):
#         return {}
#     dist_save[arr_key[index]] = arr_value[index]
#     print(dist_save)
#     if(len(arr_key) -1 == index):
#         print("=======")
#         return dist_save
#     return creat_dist(arr_key , arr_value , index+1)
    

# print(creat_dist(["1k","2k","3k"] , [1,2,3]))




# num = "4"
# print(type(num))
# if(type(num) == str):
#     print("okkkk")


# номер 6
# написать функцию которая принимает строку и изменять её вставляя после каждого символа строки "^"
# пример: 
    # функция принимает "123456" 
    # функция возвращает "1^2^3^4^5^6"


# номер 7
# написать функцию которая принимает строку и число ,
#  функцию возвращает строку умноженную на число нельзя использовать умножение


# доп задачи:
# (внизу) https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23
# https://w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php





# def func(stroka = '', num = 0 , answer = ""):
#     if num > 0:
#         answer += stroka
#         return func(stroka, num -1 , answer)
#     else: 
#         return answer

# print(func('abc', 5))