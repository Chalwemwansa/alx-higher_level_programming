#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def print_square(size):
    """function that prints a square of #"""

    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if (isinstance(size, float) and int(size) < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
