#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)

    if idx not in range(0, length):
        return (my_list)
    my_list.remove(my_list[idx])
    return (my_list)
