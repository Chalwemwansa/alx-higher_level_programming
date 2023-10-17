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
    obj2 = Rectangle(1, 2)
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
    def test_widthGet(self):
        self.assertEqual(Rect_test.obj2.width, 1)
    def test_heightGet(self):
        self.assertEqual(Rect_test.obj2.height, 2)
    def test_xGet(self):
        self.assertEqual(Rect_test.obj2.x, 0)
    def test_yGet(self):
        self.assertEqual(Rect_test.obj2.y, 0)
    def test_threeargs(self):
        obj1 = Rectangle(5, 5, 6)
        def test_heightGetter(self):
            self.assertEqual(obj1.height, 5)
        def test_xGetter(self):
            self.assertEqual(obj1.x, 6)
    def test_fourargs(self):
        obj1 = Rectangle(5, 5, 6, 10)
        def test_widthGetter(self):
            self.assertEqual(obj1.width, 5)
        def test_yGetter(self):
            self.assertEqual(obj1.y, 10)
    def test_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
    def test_valueEr(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
    def test_area(self):
        self.assertEqual(Rect_test.obj1.area(), 25)

    def test_string(self):
        my_str = str(Rect_test.obj1)
        my_cmp = '[Rectangle] (40) 6/10 - 5/5'
        self.assertEqual(my_str, my_cmp)
    def test_Display(self):
        obj = Rectangle(5, 2)
        my_str = '#####\n#####'
        self.assertEqual(print(my_str), obj.display())

    def test_disply(self):
        obj = Rectangle(5, 2, 1)
        my_str = ' #####\n #####'
        self.assertEqual(print(my_str), obj.display())
