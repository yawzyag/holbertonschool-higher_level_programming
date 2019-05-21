#!/usr/bin/python3
class Square:
    """ This is a Square class

    Attributes:
        __size (int): Size of the square.

    """
    __size = 0

    def __init__(self, __size=0):
        """Example of docstring on the __init__ method.
         Args:
             __size (int): Size of the square obj.
         """
        try:
            if __size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = __size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise
