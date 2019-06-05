#!/usr/bin/python3


from sys import argv


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

listm = []

try:
    my_info = load_from_json_file("add_item.json")
    for i in my_info:
        listm.append(i)
except:
    pass

for i in range(len(argv)):
    if i != 0:
        listm.append(argv[i])

save_to_json_file(listm, "add_item.json")
