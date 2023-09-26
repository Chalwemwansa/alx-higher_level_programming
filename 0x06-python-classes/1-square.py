#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    def __init__(self, size):
        self.__size = size
