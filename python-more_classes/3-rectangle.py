#!/usr/bin/python3
""" creating a rectangle """


class Rectangl:
    """ Define a rectangle"""
    def __init__(self, width=0, height=0):
        """ nitializes the class Rectangle"""
        self.height = height
        self.width = width

    def __str__(self):
        to_print = ""
        if not self.__height or not self.width:
            return to_print
        for i in range(self.__height):
            to_print += ("#" * self.__width)
            if i is not self.__height - 1:
                to_print += "\n"
        return to_print

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width value (int)"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve size"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set height value (int)"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates area given a width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """ calculates perimeter given a width and height"""
        if not self.__width or not self.__height:
            return 0
        return 2 * self.__width + 2 * self.__height
