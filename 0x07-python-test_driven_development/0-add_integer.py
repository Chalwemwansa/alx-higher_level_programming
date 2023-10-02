#!/usr/bin/python3
"""python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'

    contains the add_integer function

    usage:
    >>>add_integer(5, 5)
    10
"""


def add_integer(a, b=98):
    """python3 -c 'print(__import__("0-add_integer").add_integer)'
        gets two parameters and printd their sum
        if a or b is not an int or a float, a TypeError exception is raised
    """

    if isinstance(a, float) or isinstance(b, float):
        result = int(a) + int(b)
        return (result)
    if (not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return (a + b)
