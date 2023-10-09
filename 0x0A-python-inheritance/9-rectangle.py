#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__
    """

    def __init__(self, width, height):
        if type(self) is Rectangle:
            super().integer_validator("width", width)
            super().integer_validator("height", height)
        else:
            super().integer_validator("size", width)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        width = self.__width
        height = self.__height
        temp = f"[Rectangle] {width}/{height}"
        return (temp)
