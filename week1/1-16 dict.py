empty_dict = {}
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict)  # {'apple': 1, 'banana': 2, 'orange': 3}
my_dict["grape"] = 4
print(my_dict)  # {'apple': 1, 'banana': 2, 'orange': 3, 'grape': 4}

del my_dict["apple"]
print(my_dict)  # {'banana': 2, 'orange': 3, 'grape': 4}

print(my_dict["banana"])  # 2

key_list = list(my_dict.keys())
print(key_list)  # ['banana', 'orange', 'grape']

value_list = list(my_dict.values())
print(value_list)  # [2, 3, 4]
