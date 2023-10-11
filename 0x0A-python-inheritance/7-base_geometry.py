#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class BaseGeometry:
    """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__
    >>> obj = BaseGeometry()

    >>> obj.area()
    Traceback (most recent call last):
    Exception: area() is not implemented

    >>> obj.integer_validator("age", None)
    Traceback (most recent call last):
    TypeError: age must be an integer

    >>> obj.integer_validator("age", 89)
    obj.integer_validator()
    Traceback (most recent call last):
    TypeError: BaseGeometry.integer_validator() missing 2 required positional arguments: 'name' and 'value'
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not (type(value) is int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
