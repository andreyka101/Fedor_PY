
# классы везде
num = [1,2,4]
print(type(num))


class Dogs():
    '''это сообщение'''
    # init - вызывается при создании класса
    # self - это хранилище переменных и методов
    def __init__(self , name_loc):
          print("start class Dogs")
        #   создание переменной
          self.num = 7
        #   использование переменной
          print(self.num)
          print(name_loc)
          self.name = name_loc
          self.eat_num = 0
    # создание метода
    def run(self):
         print("run run run")
        #  self.eat_fun()
    # метод изменяет переменную
    def eat_fun(self , number = 2):
        '''это сообщение для метода'''
        self.eat_num += number
          


# создание объекта (вызов класса)
dog_sharik = Dogs("sharik")

# print(type(dog_sharik))

# получаем переменную класса
# print(dog_sharik.num)
# print(dog_sharik.name)



# вызываем метод
# dog_sharik.run()
# print(dog_sharik.run)


# print(dog_sharik.eat_num)
# метод меняет переменную eat_num
# dog_sharik.eat_fun(9)
# print(dog_sharik.eat_num)






# дз

# номер 1
# создайте класс с тремя переменными 
# у класса есть метод который возвращает все переменные в списке

# номер 2
# Создать класс, описывающий автомобиль (производитель, 
# модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации об автомобиле.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# номер 3
# создать класс колькулятор 
# в конструкторе нужно в писать 2 числа
# создать 4 метода: умножение , деление , сумма , вычитание
# создать метод для добавления числа (его можно вызвать много раз и подучить много чисел)





# class Auto():
#     def __init__(self , brand):
#         self.brand = brand
#         self.model = 'm5'
#         self.year = '2020'
#         self.speed = '150 km/h'
#     def info(self):
#         print(f'Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nSpeed: {self.speed}')
#     def calc(self):
#         self.speed = 150
#         distance = int(input('Введите расстояние: '))
#         total = distance/self.speed
#         print(f'Время для преодоления расстояния равно: {round(total,1)} часов')

# s = Auto()