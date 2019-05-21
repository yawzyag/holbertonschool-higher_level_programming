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

    @property
    def size(self):
        """ property

        Returns:
            self size
        """
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

    def area(self):
        """ area of square

        Returns:
            area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """ print square """
        if self.__size is 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
