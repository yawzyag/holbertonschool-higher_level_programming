#!/usr/bin/python3
""" This is necesary ?
    I
    dont
    know
"""


def say_my_name(first_name, last_name=""):
    """function to add two numbers.
       I dont know
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
