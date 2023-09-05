#!/usr/bin/python3
zer = 0
for i in range(0, 100):
    first = i // 10
    if (i >= 0):
        second = i % 10
    elif (i < 0):
        second = (i * -1) % 10
        second = second * -1
    num = (second * 10) + first
    if (not(num <= i)):
        if (i < 10 and not(i == 89)):
            print(f"{zer}{i}, ", end="")
        elif (i >= 10 and not(i == 89)):
            print(f"{i}, ", end="")
        else:
            print(f"{i}")
