#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def pascal_triangle(n):
    """function that prints a pascals triangle
        based on the value passed as parameter
    """

    if n <= 0:
        return []
    main_list = [[1]]
    for i in range(1, n):
        temp_list = [1]
        for j in range(i - 1):
            temp_list.append(main_list[i - 1][j] + main_list[i - 1][j + 1])
        temp_list.append(1)
        main_list.append(temp_list)
    return (main_list)
