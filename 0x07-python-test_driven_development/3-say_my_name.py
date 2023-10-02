#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
    the say_my_name function says the full name of a person
    usage is:
    >>>say_my_name(first_name, last_name)
    output
"""


def say_my_name(first_name, last_name=""):
    """function that says a name
        the first name should be a string
        the last name should be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
