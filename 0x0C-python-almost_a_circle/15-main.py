#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    r1 = Square(10, 7, 2, 8)
    r2 = Square(2, 4)
    Square.save_to_file([r1, r2])
    with open("Square.json", "r") as file:
        print(file.read())
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([])
    with open("Rectangle.json", 'r', encoding="utf-8") as fd:
        print(fd.read())

