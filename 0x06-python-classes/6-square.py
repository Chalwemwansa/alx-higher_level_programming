#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    """Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(position, tuple) or not (len(position) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0 or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
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
                if self.__position[1] >= 0:
                    for j in range(0, self.__position[0]):
                        print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple)) or not (len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0 or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
