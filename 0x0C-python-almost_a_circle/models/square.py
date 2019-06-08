#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        super(Square, self.__class__).width.fset(self, value)
        super(Square, self.__class__).height.fset(self, value)
