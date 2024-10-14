
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




match (str_num):
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
    case _:
        print("default")