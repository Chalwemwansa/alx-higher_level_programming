#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
import unittest
import sys
sys.path.append('..')
from models.rectangle import Rectangle


class Rect_test(unittest.TestCase):
    """tests for the rectangle class
    """

    obj1 = Rectangle(5, 5, 6, 10, 40)
    def test_widthGetter(self):
        self.assertEqual(Rect_test.obj1.width, 5)
    def test_heightGetter(self):
        self.assertEqual(Rect_test.obj1.height, 5)
    def test_xGetter(self):
        self.assertEqual(Rect_test.obj1.x, 6)
    def test_yGetter(self):
        self.assertEqual(Rect_test.obj1.y, 10)
    def test_idGetter(self):
        self.assertEqual(Rect_test.obj1.id, 40)
