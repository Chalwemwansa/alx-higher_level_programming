#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Student:
    """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__
    """

    def __init__(self, first_name, last_name, age):
        if not (isinstance(first_name, str)):
            raise TypeError("first_name should be string")
        if not (isinstance(last_name, str)):
            raise TypeError("last_name should be string")
        if not (isinstance(age, int)):
            raise TypeError("Age must be an int")
        if age < 0:
            raise ValueError("age must be greater than or equal to 0")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            my_list = []
            for i, v in self.__dict__.items():
                if i in attrs:
                    my_list.append((i, v))
            return (dict(my_list))
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        first_name = json.get('first_name')
        last_name = json.get('last_name')
        age = json.get('age')
        if not (isinstance(first_name, str)):
            raise TypeError("first_name should be string")
        if not (isinstance(last_name, str)):
            raise TypeError("last_name should be string")
        if not (isinstance(age, int)):
            raise TypeError("Age must be an int")
        if age < 0:
            raise ValueError("age must be greater than or equal to 0")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
