#!/usr/bin/python3
num = 0
for i in range(0, 100):
    if (not (i == 99) and i < 10):
        print("{}{}, ".format(num, i), end="")
    elif (not (i == 99)):
        print("{}, ".format(i), end="")
    else:
        print("{}".format(i))
