from lesson_12_class import Dogs

# класс родитель
class Animals():
    def __init__(self , name = "w"):
        self.num = 2
        # пишем в начале __ для создания приватной переменной или метода
        self.__num_priv = 3
        self.name = name
        print("start Animals")
    def print_did(self):
        print(self.did)
        self.__priv_metod()

    def get_num_priv(self):
        return self.__num_priv
    
    def __priv_metod(self):
        print("hello priv_metod")
    
    def i_metod(self):
        print("i_")

    # def __del__(self):
    #     print("I deleted")
    #     del self.__num_priv
    

            
dog = Animals("all")


# print(dog.num)
# dog.num = 7
# print(dog.num)



# print(dog.__num_priv)

# dog.did = 4
# print(dog.did)
# dog.print_did()

# dog.__num_priv = 1
# print(dog.__num_priv)
# print(dog.get_num_priv())


# dog.__priv_metod()



# num_1 = 4
# del num_1
# print(num_1)


# del dog

# print(dog.num)




# наследуем класс Animals
# в наследуемом классе можно создавать свои переменные и методы
class Cats(Animals):
    def __init__(self, name_cat):
        # вызываем метод
        super().__init__(name_cat)
        self.name = name_cat + "oooooo"
        print("ooooopop")

    def sleep(self):
        print(self.name, "sleep")
    
    def i_metod(self):
        print("metod")
        # super().i_metod()



cat = Cats("sipu")
cat.sleep()
print(cat.num)

cat.i_metod()





# дз
# задание 1
# создайте родительский класс , описывающий транспорт
# (модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации о транспорте.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# наследуйте класс автомобили в котором есть ещё одна переменная количество мест

# наследуйте класс вертолеты с дополнительным методом взлет 





class All_class():
    def __init__(self , text_all):
        self.animals = Animals(text_all)
        self.dogs = Dogs(text_all)



print('All_class("jon")')
num_all = All_class("jon")

num_all.animals.i_metod()
print(num_all.dogs.num)
