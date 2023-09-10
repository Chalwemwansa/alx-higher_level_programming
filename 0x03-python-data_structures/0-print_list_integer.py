#!/usr/bin/python3
def print_list_integer(my_list=[]):
    max = len(my_list)
    i = 0
    while (1):
        if i >= 0 and i < max:
            print("{0}".format(my_list[i]))
            i += 1
        else:
            break
