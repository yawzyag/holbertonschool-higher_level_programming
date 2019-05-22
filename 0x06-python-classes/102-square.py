#!/usr/bin/python3
""" This is necesary ? """


class Square:
    """ This is a Square class """

    def __init__(self, size=0):
        """Example of docstring on the __init__ method.
        Args:
            size (int): Size of the square obj.
        """
        self.size = size

    def area(self):
        """ area of square """
        return self.__size * self.__size

    @property
    def size(self):
        """ property """
        return self.__size

    @size.setter
    def size(self, value):
        """Example of docstring on the __init__ method.
         Args:
             size (int): Size of the square obj.
         """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, value):
        return self.size == value.size

    def __ne__(self, value):
        return self.size != value.size

    def __lt__(self, value):
        return self.size < value.size

    def __gt__(self, value):
        return self.size > value.size

    def __ge__(self, value):
        return self.size >= value.size

    def __le__(self, value):
        return self.size <= value.size
