import threading
import time


def fun_1():
    print("start fun 1")
    time.sleep(5)
    print("end fun 1")


# fun_1()
# for i in range(10):
#     print(i)





thread_1 = threading.Thread(target=fun_1)
thread_1.start()
for i in range(10):
    print(i)




def fun_2():
    print("eeeee")

thread_2 = threading.Thread(target=fun_2)
thread_2.start()