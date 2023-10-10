#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def class_to_json(obj):
    """returns the dictionary representation of the object
    """

    dictio = obj.__dict__
    return (dictio)
