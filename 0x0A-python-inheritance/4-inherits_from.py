#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def inherits_from(obj, a_class):
    flag = issubclass(type(obj), a_class) and not (type(obj) is a_class)
    return (flag)
