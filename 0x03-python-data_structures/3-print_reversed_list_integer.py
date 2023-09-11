#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    max = len(my_list)
    for i in range(0, max):
        try:
            print("{0}".format(my_list[i]))
        except er:
            print("{} is an invalid input".format(my_list[i]))
