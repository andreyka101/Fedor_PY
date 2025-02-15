
# нужная ссылка
# https://pythonworld.ru/moduli/modul-array-massivy-v-python.html


from array import array

# создаём массив
# array(r , s)
# r - режим массива (размер каждой ячейки в массиве , таблица в ссылке)
# s - список (можно не писать)
# arr = array("b" , [100,2,3])
# arr = array("b")
# print(arr)
# print(arr[0])
# print(type(arr))



# массив с плавающей точкой
arr_2 = array("f" , [100.333,2,3])
# print(arr_2)
# print(arr_2[0])
# print(type(arr_2))



#ANCHOR - у массива есть методы списков:
# arr.append(x)# - добавление элемента в конец массива.
# arr.count(х) - возвращает количество вхождений х в массив.
# arr.index(х) - номер первого вхождения x в массив.
# arr.insert(n, х) - включить новый пункт со значением х в массиве перед номером n. Отрицательные значения рассматриваются относительно конца массива.
# arr.pop(i) - удаляет i-ый элемент из массива и возвращает его. По умолчанию удаляется последний элемент.
# arr.remove(х) - удалить первое вхождение х из массива.
# arr.reverse() - обратный порядок элементов в массиве.




# возвращает режим массива (символ при создании массива)
# print(arr.typecode)



# размер в байтах каждого элемента в массиве
# print(arr.itemsize)



# кортеж (ячейка памяти, длина масива). Полезно для низкоуровневых операций.
# print(arr.buffer_info())



# .tobytes() - преобразовывает к байтам
# arr = array("i" , [1,2])
# print(arr.tobytes())


# frombytes(x) - делает массив из байт
# bytes(b, r) - превращает строку (b) в байты для работы нужно указать кодировку (r)
# arr = array("i")
# arr.frombytes(bytes("\x01\x00\x00\x00\x02\x00\x00\x00" , encoding="utf-8"))
# print(arr)



# .tofile(f) - сохраняет массив в открытый файл (f) , файл сохраняется в байтах
# arr = array("i" , [6,5,3,9])
# with open("i_file.txt" , "bw") as file_open:
#     arr.tofile(file_open)
#     print(arr)



# .fromfile(f , n) - записывает (n) чисел из (f) файла в массив , числа в файле должны быть в байтах
# with open("i_file.txt" , "rb") as file_open:
#     arr = array("i")
#     arr.fromfile(file_open , 2)
#     print(arr)



# .fromlist() - добавление элементов из списка
arr = array("i" , [1,2])
# arr.fromlist([8,5,3])
# print(arr)



# .tolist() - преобразование массива в список
# arr_list = arr.tolist()
# print(arr_list)
# print(arr)



# сортировка пузырьком
# def arr_sort(arr_loc):
#     for i in range(len(arr_loc)):
#         for num_index in range(len(arr_loc) -1):
#             if(arr_loc[num_index] > arr_loc[num_index + 1]):
#                 sive_num = arr_loc[num_index]
#                 arr_loc[num_index] = arr_loc[num_index + 1]
#                 arr_loc[num_index + 1] = sive_num 
#     return arr_loc


# arr = array("i" , [7,3,8,1,8,5,10,5,4])
# print(arr)
# print(arr_sort(arr))



            
                






