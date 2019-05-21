#!/usr/bin/python3
""" This is necesary ? """


class Square:
    """ This is a Square class """

    def __init__(self, size=0, position=(0, 0)):
        """Example of docstring on the __init__ method.
        Args:
            size (int): Size of the square obj.
            position (tuple): tuple of position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ property

        Returns:
            self size
        """
        return self.__size

    @property
    def position(self):
        """ position

        Returns:
            self postion
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) is not 2 or
            type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                if self.__position[0]:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
