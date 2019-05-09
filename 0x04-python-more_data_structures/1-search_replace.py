#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if int == search else int for int in my_list]
    return new_list
