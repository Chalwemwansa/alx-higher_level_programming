#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""
from json import loads


def from_json_string(my_str):
    """converts a json string to an object
    """

    my_obj = loads(my_str)
    return (my_obj)
