#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class MyList(list):
    """print_sorted:
        prints the list from dir in ascending sorted order
    """

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        my_list = sorted(self)
        print("[", end="")
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]), end="")
            if (not (i == (len(my_list) - 1))):
                print(", ", end="")
        print("]")
