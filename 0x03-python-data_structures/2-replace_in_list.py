#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    max = len(my_list)
    if idx in range(0, max):
        my_list[idx] = element
    return (my_list)
