#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    numerator = 0
    denominator = 0
    for i in range(len(my_list)):
        value1 = int(my_list[i][0])
        value2 = int(my_list[i][1])
        numerator += value1 * value2
        denominator += value2
    if denominator == 0:
        return (0)
    result = numerator / denominator
    return (result)
