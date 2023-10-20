#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
import unittest
import sys
sys.path.append('..')
from models.base import Base


class Base_test(unittest.TestCase):
    """tests for the base class where all other methods are inherited in the 
        other classes that inherit from it
    """

    obj1 = Base()
    obj2 = Base(40)
    def test_id(self):
        self.assertEqual(Base_test.obj1.id, 1)
    def test_id2(self):
        self.assertEqual(Base_test.obj2.id, 40)
    def test_toJasonString(self):
        my_dict = [{'i know': 'cool', 'kayla': 'kay'}, {'school': 'cool', 'chalwe': 'mazasaka'}]
        my_str = Base.to_json_string(my_dict)
        cmp_str = '[{"i know": "cool", "kayla": "kay"}, {"school": "cool", "chalwe": "mazasaka"}]'
        self.assertEqual(my_str, cmp_str)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        my_dict = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(my_dict, [{'id': 89 }])
