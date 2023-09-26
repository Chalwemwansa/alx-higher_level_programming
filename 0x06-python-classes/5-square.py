#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    """Square class
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if (self.size == 0):
            print()
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#", end="")
                print()
