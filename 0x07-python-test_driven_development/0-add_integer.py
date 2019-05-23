#!/usr/bin/python3
""" This is necesary ?
    i
    dont
    know
"""


def add_integer(a, b=98):
    """function to add two numbers.
       i dont know
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int) and not isinstance(a, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
