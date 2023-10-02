#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def add_integer(a, b=98):
    """function that adds two integers together"""

    if isinstance(a, float) or isinstance(b, float):
        result = int(a) + int(b)
        return (result)
    if (not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return (a + b)
