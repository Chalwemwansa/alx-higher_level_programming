#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
try:
    my_square = Rectangle.square("12")
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)
except Exception as e:
    print("[{}] {}".format(e.class.name_, e))

