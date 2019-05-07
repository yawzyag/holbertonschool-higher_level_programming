#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        cpy_list = list(my_list)
        if idx >= 0 and idx < len(my_list):
            cpy_list[idx] = element
            return cpy_list
        else:
            return my_list
