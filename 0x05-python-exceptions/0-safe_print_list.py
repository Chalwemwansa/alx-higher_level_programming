#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            if (i == (x - 1)):
                print()
                return (i + 1)
        except Exception:
            print()
            return (i)
