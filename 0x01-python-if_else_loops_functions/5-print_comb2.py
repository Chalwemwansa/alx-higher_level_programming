#!/usr/bin/python3
num = 0
for i in range(0, 100):
    if (not(i == 99) and i < 10):
        print(f"{num}{i}, ", end="")
    elif (not(i == 99)):
        print(f"{i}, ", end="")
    else:
        print(f"{i:.2g}")
