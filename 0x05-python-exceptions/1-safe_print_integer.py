#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (1 == 1)
    except Exception:
        return (1 == 2)
