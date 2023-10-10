#!/usr/bin/python3
import json
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def to_json_string(my_obj):
    """returns the json string of an object
    """
    my_str = json.dumps(my_obj)
    return (my_str)
