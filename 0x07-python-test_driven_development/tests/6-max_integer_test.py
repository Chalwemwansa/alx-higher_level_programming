#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class for testing code"""

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_list(self):
        self.assertEqual(max_integer([3, 5, 6, 2, 6, 46, 78, -2, -4, -5]), 78)

    def test_one(self):
        self.assertEqual(max_integer([0]), 0)

    def test_two(self):
        self.assertEqual(max_integer([1, 0]), 1)
