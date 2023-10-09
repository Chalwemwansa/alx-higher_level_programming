#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class BaseGeometry:
    """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__
    """

    def area(self):
        raise Exception("area() is not implemented")
