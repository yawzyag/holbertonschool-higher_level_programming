#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    elif my_list is not None:
        num = 0
        for i in my_list:
            if i > num:
                num = i
        return num
