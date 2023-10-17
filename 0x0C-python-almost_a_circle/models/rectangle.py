#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
from json import loads
from models.base import Base


class Rectangle(Base):
    """class that makes a rectagle and inherits from base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """the area function that computes the area of the
        insatnce or object and returns its area
        """
        return (self.height * self.width)

    def display(self):
        """the display function that prints the area using the symbol #
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """the __str__ method that changes what is printed when an object is
        passed as parameter to the print function in python
        """
        my_str = f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return ("[Rectangle] " + my_str)

    def update(self, *args, **kwargs):
        """updates the members of the object to the values that the user
        wants to set them to
        """
        if not (len(kwargs) == 0):
            for key, value in kwargs.items():
                setattr(self, key, value)
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            elif i == 4:
                self.y = args[i]

    def to_dictionary(self):
        """converts a json string of the dictionary format into
        an actual dictioanry obj
        """
        my_str = "{" + '"id": {}, "width": {}, "height": {}, "x": {}, "y": {}\
            '.format(self.id, self.width, self.height, self.x, self.y) + "}"
        return (loads(my_str))
