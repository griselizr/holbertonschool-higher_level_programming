#!/usr/bin/python3
"""
Creating a rectangle
"""


class Rectangle:
    """ define rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes the  Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Retrieves width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width value (int): width to setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve size"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height value (int)"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates area given to width and height """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates perimeter given a width and height
        """
        if not self.__width or not self.__height:
            return 0
        return 2 * self.__width + 2 * self.__height
