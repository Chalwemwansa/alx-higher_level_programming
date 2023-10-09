#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def lookup(obj):
    """function returns a list of the available attributes and methods of a class
    """
    return (dir(obj))
