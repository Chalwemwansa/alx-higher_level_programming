#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def read_file(filename=""):
    """function that prints a files content to stdout
    """

    with open(filename, 'r', encoding="utf-8") as fd:
        for i in fd:
            print("{}".format(i), end="")
