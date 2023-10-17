#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
from json import loads
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that makes a square and inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the __str__ function that changes the print of the object
        when an object is passed as an argument to the print function in
        python
        """
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
        """the update function in the class that updates the
        previous entries that were present
        """
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
        """the to_dictionary function that
        converts a json string to an actual dictionary in python
        """
        my_str = "{" + '"id": {}, "size": {}, "x": {}, "y": {}\
        '.format(self.id, self.width, self.x, self.y) + "}"
        return (loads(my_str))
