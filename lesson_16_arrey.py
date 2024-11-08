# https://pythonworld.ru/moduli/modul-array-massivy-v-python.html


from array import array

arr = array("b" , [100,2,3])
# print(arr)
# print(arr[0])
# print(type(arr))



# arr_2 = array("f" , [100.333,2,3])
# print(arr_2)
# print(arr_2[0])
# print(type(arr_2))





# print(arr.typecode)



# print(arr.itemsize)



# arr.append(5)# - добавление элемента в конец массива.
# print(arr)



# print(arr.buffer_info() )



# array.count(х) - возвращает количество вхождений х в массив.
# array.extend(iter) - добавление элементов из объекта в массив.
# array.index(х) - номер первого вхождения x в массив.
# array.insert(n, х) - включить новый пункт со значением х в массиве перед номером n. Отрицательные значения рассматриваются относительно конца массива.
# array.pop(i) - удаляет i-ый элемент из массива и возвращает его. По умолчанию удаляется последний элемент.
# array.remove(х) - удалить первое вхождение х из массива.
# array.reverse() - обратный порядок элементов в массиве.



file_open = open("i_file.txt")
arr.fromfile(file_open , 1)
print(arr)










#FIXME - array.byteswap()
# array.frombytes(b) - делает массив array из массива байт. Количество байт должно быть кратно размеру одного элемента в массиве.