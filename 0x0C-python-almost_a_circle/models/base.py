#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
from json import dumps, loads


class Base:
    """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return ("[]")
        return (dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        from models.rectangle import Rectangle
        from models.square import Square
        filename = "Rectangle.json"
        if cls is Square:
            filename = "Square.json"
        if list_objs is None or len(list_objs) == 0:
            with open(filename, 'w', encoding="utf-8") as fd:
                fd.write("[]")
        else:
            with open(filename, 'w', encoding="utf-8") as fd:
                my_list = []
                for i in list_objs:
                    my_list.append(i.to_dictionary())
                my_str = Base.to_json_string(my_list)
                fd.write(my_str)

    @staticmethod
    def from_json_string(json_string):
        if (json_string is None) or (len(json_string) == 0):
            return ([])
        return (loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        from models.square import Square
        from models.rectangle import Rectangle
        if cls is Square:
            new_instance = cls(1)
        else:
            new_instance = cls(1, 1)

        new_instance.update(**dictionary)
        return (new_instance)

    @classmethod
    def load_from_file(cls):
        from models.rectangle import Rectangle
        from models.square import Square
        from os.path import exists
        new_list = list()
        my_list_dicts = []
        if cls is Rectangle:
            filename = "Rectangle.json"

        else:
            filename = "Square.json"
        if not exists(filename):
            return ([])
        with open(filename, 'r', encoding="utf-8") as fd:
            my_list_dicts = Base.from_json_string(fd.read())
        for i in my_list_dicts:
            new_list.append(cls.create(**i))
        return (new_list)
