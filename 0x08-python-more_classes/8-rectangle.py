#!/usr/bin/python3
""" rectangle

"""


class Rectangle:
    """
    class to create a rectangle object

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Example of docstring on the __init__ method.
        Args:
            width (int): Size of the rectangle obj.
            height (int): size of the rectangle obj.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ print str rectangle """
        listm = []
        if self.__width is 0 or self.__height is 0:
            listm.append("")
        else:
            for i in range(self.__height):
                listm.append("{}".format(self.print_symbol) * self.__width)
                if i < self.__height - 1:
                    listm.append("\n")
        return ("".join(listm))

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        # Rectangle.p_rectangles -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1.area
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
