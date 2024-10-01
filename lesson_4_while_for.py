# цикл while работает когда значение True
# num=0
# while(num < 10):
#     print("hello")
#     print(num)
#     num+=1
# print("end")
# print("ok")



# end_bool = True
# while(end_bool):
#     print("hello")
#     num_inp = int(input("__"))
#     if(0 == num_inp):
#         end_bool = False
# print("end")



# цикл for работает какое то количество раз
# index - переменная 
# с помощью метода range(x) задаётся количество оборотов цикла
# for index in range(10):
#     print(index)



# for index in range(10):
#     if(index % 2 == 0):
#         print(index)



# for i in range(5,10 + 1):
#     print(i)



# range(x, y, z)
# x - start
# y - stop
# z - step
# for i in range(5, 20, 2):
#     print(i)



# str_1="qwertyuiop[]"
# for index in range(12):
#     print(str_1[index])


# str_1="qwertyuiop[]"
# for index in range(len(str_1)):
#     print(str_1[index])


# с помощью for можно перебирать строку
# str_1="qwertyuiop[]"
# for element_str in str_1:
#     print(element_str)




# str_number = "1234567890"
# str_string = "qwertyuiop"
# if(len(str_number) == len(str_string)):
#     str_number_string = ""
#     for i in range(len(str_number)):
#         str_number_string += str_number[i] + str_string[i]
#     print(str_number_string)



# str_i = ""
# for i in range(10):
#     str_i += str(i)
# print(str_i)


str_x = ""
for y in range(10):
    for x in range(10):
        str_x += str(x) + str(y) + " "
    print(str_x)
    str_x = ""




# дз

# https://metanit.com/python/practice/3.php

# Задание 1. Написать имитацию кассового аппарата для 
# магазина, торгующего новогодними товарами. Кассир 
# должен выбрать товар из списка, ввести его количество, 
# затем выбрать следующий товар. По завершению ввода 
# вывести на экран всю сумму покупки. Предусмотреть 
# наличие скидки. В списке товаров должно быть не меньше 
# 4-х товаров, должна отображаться их цена. Предусмотреть 
# неправильно вводимые данные.
# . Хранение общей выручки магазина;
# . Ограничить количество товара в магазине

# Задание 2. Написать программу-конвертер валют.
# Реализовать общение с пользователем через меню.

# Задание 3. Написать программу, которая проверяет пользователя на знание таблицы умножения. Программа выводит на экран два числа, пользователь должен ввести их 
# произведение. Разработать несколько уровней сложности 
# (отличаются сложностью и количеством вопросов). Вывести пользователю оценку его знаний.

# Задание 4. Вывести на экран ромб из звездочек.
