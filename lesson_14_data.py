
# открытие файла
# open_file = open("i_file.txt")
# print(open_file)



# режимы открытия:
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись



# по умолчанию файл открывается в режиме 'r'
# open_file_2 = open("i_file.txt" , "r")
# .read() - получаем текст отрытого файла
# print(open_file_2.read())



# указываем полный путь к файлу
# open_file_3 = open("C:/main_brain/фаилы/delite_i.txt" , "r")
# print(open_file_3.read())



# указываем путь относительно папки проекта 
# папка с файлом внутри проекта
# open_file_4 = open("./pack_file/i_file_2.txt" , "r")
# print(open_file_4.read())

# папка с файлом вне проекта 
# open_file_5 = open("../del_file_global.txt" , "r")
# print(open_file_5.read())



# выходим из двух папок
# open_file_6 = open("../../del_file_global_2.txt" , "r")
# print(open_file_6.read())



# переписываем файл
# open_file_7 = open("i_file.txt" , "w")
# open_file_7.write("123456789")



# пример перезаписи и чтения
# open_file_8 = open("i_file.txt" , "w")
# open_file_8.write("qwertyuio")

# .close() - закрывает файл
# open_file_8.close()

# если не закрыть файл то чтение не сработает
# open_file_9 = open("i_file.txt")
# print(open_file_9.read())



# пример открытия на дозапись
# open_file_9 = open("i_file.txt" , "a")
# open_file_9.write("12555")
# open_file_9.close()




# read_file = open("i_file.txt" , "r").read()
# with - также его можно использовать для чтения файла
# with open("i_file.txt" , "w") as open_file_10:
#     open_file_10.write(read_file+ " = " + read_file)
    
# print(open("i_file.txt" , "r").read())




# read_file_2 = open("i_file.txt" , "r").read()
# read_file_2 = [open("i_file.txt" , "r").read()]
# print(read_file_2)



# метод .readlines() каждую строку txt файла превращает в элемент массива
# он возвращает массив
# read_file_3 = open("i_file.txt" , "r").readlines()
# print(read_file_3)



# .split(s) - разделяет строку по строке s
# read_file_4 = open("i_file.txt" , "r").read()
# read_arr = read_file_4.split("\n")
# print(read_arr)







# дз
# номер 1
# сделать программу , которая принимает текст и сохраняет в файл 


# номер 2
# сделать программу калькулятор с историей программа должна показывать историю


# номер 3
# создайте менеджер пользователей
# . программа должна работать до тех пор пока не не будет введено exit или ex
# . если ввести new - создаётся новый пользователь он должен хранить имя и пароль (если ввести существующие имя то программа просит его изменить)
# . если ввести del - удаляется пользователь его имя и пароль
# все пользователи должны сохраняются на txt файл





