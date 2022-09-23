#!/usr/bin/python3
"""creating class Square"""
class Square:
    """define the Square"""



    def __init__(self, size=0):
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size**2
