#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    Rectangle class contained in the file
"""


class Rectangle:
    """clas that creates a rectangle object"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        perim = 0
        if not (self.width == 0) and not (self.height == 0):
            perim = (self.height * 2) + (self.width * 2)
        return (perim)

    def __str__(self):
        temp = ""
        if (self.width == 0) or (self.height == 0):
            return (temp)
        for height in range(self.height):
            temp += '#' * self.width
            if not (height == (self.height - 1)):
                temp += '\n'
        return (temp)

    def __repr__(self):
        temp = "Rectangle(" + f"{self.width}" + ", " + f"{self.height}" + ")"
        return (temp)
