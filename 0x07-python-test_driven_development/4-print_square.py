#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
    there is the print_square
    usage:
    >>> print_square(size)
    output
"""


def print_square(size):
    """function that prints a square of #
        size must be either an integer
        or size must be a float
        size must not be less than 0
    """

    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
