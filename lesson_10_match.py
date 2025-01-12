
str_num = "5"
# if(str_num == "q"):
#     print("ok q")
# elif(str_num == "w"):
#     print("ok w")
# elif(str_num == "e"):
#     print("ok e")
# elif(str_num == "r"):
#     print("ok r")
# elif(str_num == "t"):
#     print("ok t")



# match делает одну проверку и сразу возвращает нужный case
match(str_num):
    case("q"):
        print("ok q")
    case("w"):
        print("ok w")
    case("e"):
        print("ok e")
    case("r"):
        print("ok r")
    case("t"):
        print("ok t")
    # case _ - действие по умолчанию (можно не писать)
    case _:
        print("default")



# дз
# номер 1
# Составить расписание на неделю. 
# Пользователь вводит порядковый номер дня недели и у него на экране отображается, то,
# что запланировано на этот день.


# номер 2
# сделать программу калькулятор пользователь вводит:
# 1. первое число 
# 2. арифметический оператор
# 3. второе число 