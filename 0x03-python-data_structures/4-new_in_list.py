#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    max = len(my_list)

    if idx not in range(0, max):
        return (my_list)

    new_my_list = []

    for i in range(0, max):
        if (i == idx):
            new_my_list.append(element)
        else:
            new_my_list.append(my_list[i])
    return (new_my_list)
