#!/usr/bin/python3
def uniq_add(my_list=[]):
    st = set(my_list)
    num = 0
    for i in st:
        num = num + i
    return num
