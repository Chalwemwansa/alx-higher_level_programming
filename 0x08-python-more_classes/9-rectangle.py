#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    Rectangle class contained in the file
"""


class Rectangle:
    """class that creates a rectangle object"""
    number_of_instances = 0
    print_symbol = None

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if Rectangle.print_symbol is None:
            Rectangle.print_symbol = '#'
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
            temp += f'{self.print_symbol}' * self.width
            if not (height == (self.height - 1)):
                temp += '\n'
        return (temp)

    def __repr__(self):
        temp = "Rectangle(" + f"{self.width}" + ", " + f"{self.height}" + ")"
        return (temp)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        elif rect_1.area() < rect_2.area():
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")
        cl = cls(size, size)
        return (cl)
