#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        lista = []
        for i in my_list:
                lista.append(i % 2 == 0)
        return lista
