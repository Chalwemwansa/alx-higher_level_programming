#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)
    r2 = Rectangle(2, 10)
    print(r2.id)
    r3 = Rectangle(10, 2, 16, 9, 12)
    print(r3.id)
    print(f"width before is: {r3.width}")
    r3.width=15
    print(f"width after is: {r3.width}")
    print("{}".format(r3.y))
    print("old x was: {}".format(r3.x))
    r3.x = 20
    print("new x is: {}".format(r3.x))
