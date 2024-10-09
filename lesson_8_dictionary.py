obj = {
    "key":50,
    "qwert":"w",
    4:90,
    "5":"0=",
}

print(obj["key"])
print(obj["5"])
print(obj[4])



obj_arr = {
    0:2,
    1:3,
    2:4,
    3:5,
}

print(obj_arr[2])



#NOTE - metods


obj_arr_2 = obj_arr.copy() 


obj_arr.clear()
print(obj_arr)


print(obj.get("5"))

# print(obj["7"])
print(obj.get("7"))

if(obj.get("5") != None):
    print("ok")



print(obj.keys())


print(obj.values())


# num = obj.pop("5")
# print(num)
# print(obj)



# print(obj.popitem())
# print(obj)


# obj.setdefault("7",888)
# print(obj)


obj.setdefault("7",888)
print(obj)


obj.update({"5":555})
print(obj)




str_num = input("__")

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



print(str_num)
if_dist_obj = {
    "q": "ok q",
    "w": "ok w",
    "e": "ok e",
    "r": "ok r",
    "t": "ok t",
}
if(obj.get(str_num) != None):
    print(if_dist_obj[str_num])



