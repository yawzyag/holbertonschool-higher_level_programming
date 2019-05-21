#!/usr/bin/python3
""" This is necesary ? """


class Square:
    """ This is a Square class """

    def __init__(self, size=0):
        """Example of docstring on the __init__ method.
         Args:
             size (int): Size of the square obj.
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
