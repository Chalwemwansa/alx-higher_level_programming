#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""
from json import dumps


def to_json_string(my_obj):
    """returns the json string of an object
    """
    my_str = dumps(my_obj)
    return (my_str)
