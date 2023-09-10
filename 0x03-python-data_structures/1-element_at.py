#!/usr/bin/python3
def element_at(my_list, idx):
    max = len(my_list)
    if (idx < 0) or (idx >= max):
        return ("None")
    return (my_list[idx])
