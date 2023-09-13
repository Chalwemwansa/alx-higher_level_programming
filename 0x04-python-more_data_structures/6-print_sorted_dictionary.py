#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = list()
    for k, v in a_dictionary.items():
        new_list.append(k)
    new_list = sorted(new_list)
    for i in range(len(new_list)):
        print("{}: {}".format(new_list[i], a_dictionary[new_list[i]]))
