# input() - ввод текста
# str_num = input("введите строку__")
# str_num = int(str_num)
# print(type(str_num))
# print(str_num * 2)
# num_inp = int(input("__"))
# print(num_inp)


print("q\nw\ne\nr\nt")
print('qwe"rt')


# вывод символа из строки
str_var_1 = "qwertyui"
# print(str_var_1[1])
# str_2 = str_var_1 + str_var_1[1] + str_var_1[4]
# print(str_2)
# print(str_var_1 + str_var_1[1] + str_var_1[4])


# len() - возвращает длину строки
# print(len(str_var_1))


# методы строк
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

str_var_1 = "1234ert567890_1234ert567890"
# string.find(s) - Возвращает индекс первого вхождения подстроки s, если подстрока s не найдена возвращает -1 
print(str_var_1.find("ert"), str_var_1.find("ert") + len("ert") - 1)
# string.find(s, x) - Поиск начинается с индекса x, возвращает индекс первого вхождения подстроки s, если подстрока s не найдена возвращает -1 
print(str_var_1.find("ert" ,7))

# string.count(s) - Возвращает количество вхождений подстроки s
print(str_var_1.count("ert"))

str_var_2 = "12345"
# string.isdigit() - Возвращает True, если строка состоит только из цифр, в противном случае False
print(str_var_2.isdigit())
str_var_2 = str_var_2 + "r"
print(str_var_2.isdigit())



# fстроки нужны для простой интеграции переменных внутрь строки
num = 45
# str_var_3 = "qwerty" + str(45)
str_var_3 = f"qweewr{num} gsvcgscgs{77} {True}"
print(str_var_3)



# дз:
# Задание 1. Пользователь вводит год. Необходимо написать программу, которая выведет количество дней в этом 
# году. При написании программы использовать линейный 
# алгоритм (конструкции условного выбора не использовать). Например, пользователь ввел год 2004, программа 
# сообщает, что в этом году 366 дней в следующей форме:
# In 2004 year = 366 days

# Задание 2. Пользователь вводит с клавиатуры денежную 
# сумму в рублях и копейках (рубли и копейки вводятся 
# в разные переменные). Сумма может быть введена как 
# правильно (например 19 руб. 90 коп), так и неправильно 
# (например 22 руб. 978 коп). Написать программу, которая, 
# используя только линейный алгоритм, осуществит корректировку введенной денежной суммы в правильную форму.
# Например, если пользователь ввел 11 руб. 150 коп, 
# программа должна вывести на экран сумму 12 руб. 50 коп

# Задание 3. Написать программу вычисления объема параллелепипеда. Ниже приведен рекомендуемый вид экрана 
# во время выполнения программы.
# Вычисление объема параллелепипеда.
# Введите исходные данные:
# Длина (см) -> 9;
# Ширина (см) -> 7.5;
# Высота (см) -> 5;
# Объем: 337.50 куб. см.

# Задание 4. Зарплата менеджера — 100$ + 5% от продаж. 
# Пользователь вводит с клавиатуры общую сумму сделок менеджера за месяц. 
# Посчитать итоговую зарплату менеджера.

# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_2


year = int(input('Введите год: '))
# days = 365 + (((year % 4 == 0) + (year % 100 != 0) + (year % 400 == 0)) -1 )
# print(f'In {year} year = {days} days')

days = year % 4 
print(days)


