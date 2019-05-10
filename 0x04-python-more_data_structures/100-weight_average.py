#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and my_list is not None:
        num1 = 0
        num2 = 0
        for tuple_1 in my_list:
            num1 = num1 + (tuple_1[0] * tuple_1[1])
            num2 = num2 + tuple_1[1]
        num1 = num1 / num2
        return num1
    return 0
