#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    new_list = []

    for i in range(0, length):
        new_list += [((my_list[i] % 2) == 0)]
    return (new_list)
