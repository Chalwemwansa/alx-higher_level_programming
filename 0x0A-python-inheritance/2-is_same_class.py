#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def is_same_class(obj, a_class):
    """checks if object is an instance of a given a_class
    """

    return (type(obj) is a_class)
