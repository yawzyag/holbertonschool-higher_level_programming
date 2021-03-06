#!/usr/bin/python3
""" testing comments """
from models.base import Base


class Rectangle(Base):
    """ testing comments """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ testing comments """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ testing comments """
        return self.__width * self.__height

    def display(self):
        """ print square """
        if self.__width is 0:
            print("")
        else:
            for i in range(self.__y):
                print("")
            for i in range(self.__height):
                if self.__x:
                    print(" " * self.__x, end="")
                print("#" * self.__width)

    def update(self, *args, **kwargs):
        """ testing comments """
        listm = ["id", "width", "height", "x", "y"]

        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, listm[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ testing comments """
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def to_dictionary(self):
        """ testing comments """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}

    @property
    def width(self):
        """ testing comments """
        return self.__width

    @width.setter
    def width(self, value):
        """ testing comments """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ testing comments """
        return self.__height

    @height.setter
    def height(self, value):
        """ testing comments """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ testing comments """
        return self.__x

    @x.setter
    def x(self, value):
        """ testing comments """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ testing comments """
        return self.__y

    @y.setter
    def y(self, value):
        """ testing comments """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
