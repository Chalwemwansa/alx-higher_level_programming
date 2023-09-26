#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(0, list_length):
        try:
            try:
                result = my_list_1[i] / my_list_2[i]
                new_list.append(result)

            except TypeError:
                new_list.append(0)
                print("wrong type")

            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")

        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            if (not (i == (list_length - 1))):
                continue

    return (new_list)
