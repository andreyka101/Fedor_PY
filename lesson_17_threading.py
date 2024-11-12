import threading
import time


def fun_1():
    print("start fun 1")
    time.sleep(5)
    print("end fun 1")



# пример без потока
# fun_1()
# for i in range(10):
#     print(i)





# пример с потоком
# threading.Thread - создание потока
thread_1 = threading.Thread(target=fun_1)
# .start() - запуск потока 
thread_1.start()
for i in range(10):
    print(i)

#ANCHOR - забыл рассказать
# .join() - строки ниже ждут окончание потока
thread_1.join()
print("hello")



# создание и запуск второго потока
def fun_2():
    print("eeeee")

thread_2 = threading.Thread(target=fun_2)
thread_2.start()





# дз
# номер 1
# создайте много поточную сортировку пузырьком





