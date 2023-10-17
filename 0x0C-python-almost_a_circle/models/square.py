#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
from models.rectangle import Rectangle
from json import loads


class Square(Rectangle):
    """class that makes a square and inherits from rectangle
    """


    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        my_str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return (my_str)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if not (len(args) == 0):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if not (len(kwargs) == 0):
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        my_str = "{" + '"id": {}, "size": {}, "x": {}, "y": {}\
        '.format(self.id, self.width, self.x, self.y) + "}"
        return (loads(my_str))
