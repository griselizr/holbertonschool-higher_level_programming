#!/usr/bin/python3
""" creates a rectangle"""


class Rectangl:
    """ Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """  initializes the class Rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """print the rectangle with the character #"""
        to_print = ""
        if not self.__height or not self.width:
            return to_print
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    to_print += str(self.print_symbol)
                except Exception:
                    to_print += type(self).print_symbol
            if i is not self.__height - 1:
                to_print += "\n"
        return to_print

    def __repr__(self):
        """ recreate a new instance by using eval()"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Print the message (Bye rectangle...)
            (... being 3 dots not ellipsis)
            when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """ retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width value (int): width to setter
        """
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
        """ set height value (int): height to setter"""
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
