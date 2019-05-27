#!/usr/bin/python3
""" rectangle

"""


class Rectangle:
    """
    class to create a rectangle object

    """
    def __init__(self, width=0, height=0):
        """Example of docstring on the __init__ method.
        Args:
            width (int): Size of the rectangle obj.
            height (int): size of the rectangle obj.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property """
        return self.__width

    @width.setter
    def width(self, value):
        """Height setter.
         Args:
             value (int): Size of the square obj.
         """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ property """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter.
        Args:
             value (int): Size of the square obj.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ perimetro of square """
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__height * 2 + self.__width * 2)
