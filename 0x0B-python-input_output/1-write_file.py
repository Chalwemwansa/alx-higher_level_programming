#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def write_file(filename="", text=""):
    """function that writes content to a file
    """

    with open(filename, 'w', encoding="utf-8") as fd:
        num_of_char = fd.write(text)

    return (num_of_char)
