#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""
from json import load


def load_from_json_file(filename):
    """creates an object from a json file
    """

    with open(filename, 'r', encoding="utf-8") as fd:
        my_obj = load(fd)

    return (my_obj)
