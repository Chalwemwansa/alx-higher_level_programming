#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        flag = 0
    except Exception:
        flag = 1
    finally:
        if (not (flag == 0)):
            result = None
        print("Inside result: {}".format(result))
        return (result)
