arr_list = [1,2,4,5 ,7 , 4 ,1]
print(arr_list)


# arr.append(x) - Добавляет элемент x в конец списка
# arr_list.append("str")
# print(arr_list)

# arr_list.append([6,4,0])
# print(arr_list)


# arr.extend(x) - Расширяет список arr, добавляя в конец все элементы списка x
# arr_list.extend([6,4,0])
# print(arr_list)


# arr.index(x, i) - Возвращает положение первого элемента со значением x поиск начинается с индекса i (можно не писать)
# print(arr_list.index(4,3))


# arr.count(x) - Возвращает количество элементов со значением x
# print(arr_list.count(4))


# arr.remove(x) - Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# arr_list.remove(1)
# print(arr_list)


# arr.pop(i) - 	Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# arr_list.pop(5)
# print(arr_list)


# arr.insert(i, x) - Вставляет на i индекс элемент x
# arr_list.insert(5,999)
# print(arr_list)


# arr.sort() - Сортирует список
# arr_list.sort()
# print(arr_list)


# arr.reverse() - Разворачивает список
# arr_list.reverse()
# print(arr_list)


# arr.clear() - Очищает список
# arr_list.clear()
# print(arr_list)


# arr.copy() - Поверхностная копия списка
# arr_2 = arr_list
# arr_copy = arr_list.copy()
# print("arr_2 = " , arr_2)
# arr_list.clear()
# print("arr_list = " , arr_list)
# print("arr_2 = " , arr_2)
# print("arr_copy  = " , arr_copy )



# Исправь ошибку !!!
# index = len(arr_list) - 1
# while (index != 0):
#     print(arr_list[index-2])
#     arr_list.remove(arr_list[index-2])



# dz
# https://metanit.com/python/practice/4.php
# https://pythonist.ru/python-spiski-zadachi-dlya-nachinayushhih/




arr_list = [1,2,4,5 ,7 , 4 ,1]
print(type(5))
# index = len(arr_list) 
# while index != 0:
#     print(arr_list[-1])
#     index -= 1
#     arr_list.pop()