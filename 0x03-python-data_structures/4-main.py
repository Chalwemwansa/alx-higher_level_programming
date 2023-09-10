#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

idx = -1
new_element = 10
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

idx = 30
new_element = 90
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

idx = 0
new_element = -9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
