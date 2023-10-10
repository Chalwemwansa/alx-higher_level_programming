#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """writes an object to a file
    """

    with open(filename, 'w', encoding="utf-8") as fd:
        dump(my_obj, fd)
