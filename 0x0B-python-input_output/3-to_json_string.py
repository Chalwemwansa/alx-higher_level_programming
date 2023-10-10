#!/usr/bin/python3
from json import dumps
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def to_json_string(my_obj):
    return (dumps(my_obj))
