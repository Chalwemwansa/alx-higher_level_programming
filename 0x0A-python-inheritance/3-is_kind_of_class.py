#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def is_kind_of_class(obj, a_class):
    return (isinstance(obj, a_class))
