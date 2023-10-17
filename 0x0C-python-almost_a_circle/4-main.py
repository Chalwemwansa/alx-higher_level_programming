#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(4, 6)
    r1.display()
    print("---")
    r1 = Rectangle(2, 2)
    r1.display()
    my_dict = r1.to_dictionary()
    for key, values in my_dict.items():
        print(f"{key} is: {values}")
