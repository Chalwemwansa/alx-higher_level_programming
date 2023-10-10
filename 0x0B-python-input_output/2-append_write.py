#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as fd:
        num_char = fd.write(text)

    return (num_char)
