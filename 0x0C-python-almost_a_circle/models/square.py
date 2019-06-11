#!/usr/bin/python3
""" testing comments """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ testing comments """

    def __init__(self, size, x=0, y=0, id=None):
        """ testing comments """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ testing comments """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """ testing comments """
        listm = ["id", "size", "x", "y"]

        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, listm[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ testing comments """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.height}

    @property
    def size(self):
        """ testing comments """
        return super().width

    @size.setter
    def size(self, value):
        """ testing comments """
        super(Square, self.__class__).width.fset(self, value)
        super(Square, self.__class__).height.fset(self, value)
