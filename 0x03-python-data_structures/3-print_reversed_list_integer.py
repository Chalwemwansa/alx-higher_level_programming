#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    max = len(my_list)

    for i in range((max - 1), -1, -1):
        print("{}".format(my_list[i]))
