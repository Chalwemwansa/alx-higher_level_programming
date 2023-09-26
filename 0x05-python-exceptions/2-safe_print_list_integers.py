#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0

    if (x == 0):
        return (total)
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            total += 1
            if (i == (x - 1)):
                print()
                return (total)
        except ValueError:
            if (i == (x - 1)):
                print()
                return (total)
            continue
        except TypeError:
            if (i == (x - 1)):
                print()
                return (total)
            continue
