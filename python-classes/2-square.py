#!/usr/bin/python3
""" define square """


class Square:
    """ Defining the square """

    def __init__(self, size=0):
        "" build a square 

        """ private instance size
        size = int

        if size != int 
        TypeError
        if size < 0
        ValueError
        """

        if not instance(size, int):
        raise TypeError("size must be an integer")
        if size < 0:
        raise ValueError("size must be >= 0")
        self.__size = size
