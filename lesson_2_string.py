# str_num = input("введите строку__")
# str_num = int(str_num)
# print(type(str_num))
# print(str_num * 2)
# num_inp = int(input("__"))
# print(num_inp)


# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
print("q\nw\ne\nr\nt")
print('qwe"rt')

str_var_1 = "qwertyui"
# print(str_var_1[1])
# str_2 = str_var_1 + str_var_1[1] + str_var_1[4]
# print(str_2)
# print(str_var_1 + str_var_1[1] + str_var_1[4])


# print(len(str_var_1))


str_var_1 = "1234ert567890_1234ert567890"
print(str_var_1.find("ert"), str_var_1.find("ert") + len("ert") - 1)
print(str_var_1.find("ert" ,7))

str_var_2 = "12345"
print(str_var_2.isdigit())
str_var_2 = str_var_2 + "r"
print(str_var_2.isdigit())

print(str_var_1.count("ert"))



num = 45
# str_var_3 = "qwerty" + str(45)
str_var_3 = f"qweewr{num} gsvcgscgs{77} {True}"
print(str_var_3)




# .split