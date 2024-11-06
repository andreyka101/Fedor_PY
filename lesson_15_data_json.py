import json

arr = [1,2,3,4]
obj = {
    "s":1,
    "d":2,
    "f":3,
    6:"rggg",
}

# str_json = json.dumps(arr)
# print(str_json)
# print(str_json[0])
# print(type(str_json))



# data_open = open("i_j_file.json", "w")
# data_open.write(str_json)
# data_open.close()



# data_open_2 = open("i_j_file.json")
# arr_file = json.load(data_open_2)
# print(arr_file)
# print(arr_file[0])
# print(type(arr_file))



# arr_json_local = json.loads(str_json)
# print("==============")
# print(arr_json_local)
# print(arr_json_local[0])
# print(type(arr_json_local))



data_open_3 = open("i_j_file.json", "w")
data_open_3.write(json.dumps(obj))
data_open_3.close()



data_open_3 = open("i_j_file.json")
arr_file_2 = dict(json.load(data_open_3))
with open("i_j_file.json", "w") as data_open_4:
    arr_file_2.update({
        "rr":13
    })
    data_open_4.write(json.dumps(arr_file_2))




