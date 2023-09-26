"""
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
class Square:
    def __init__(self, size=0):
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
