#!/usr/bin/python3
def print_list_integer(my_list=[]):
    max = len(my_list)

    for i in range(0, max):
        p = my_list[i]
        print("{}".format(p))
