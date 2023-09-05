#!/usr/bin/python3
num = '0'
for i in range(0, 100):
    if (not (i == 99)):
        print("{:02}, ".format(i), end="")
    else:
        print("{}".format(i))
