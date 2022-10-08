#!/usr/bin/python3
"""Creates a class Rectangle"""

from tkinter import Y
from turtle import width
from models.base import Base


class Rectangle(Base):
    """Defines a class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization of private attributes """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get wight"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height """
        return self.__height

    @height.setter
    def height(self, value):
        """set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance """
        return self.width * self.height

    def display(self):
        """ prints stdout character #"""
        for row in range(self.y):
            print("")

        """ prints height and width starting from 0"""
        for i in range(0, self.height):
            for side in range(self.x):
                print(" ", end="")
            for other in range(0, self.width):
                print("#", end="")
                """ prints newline"""
            print()

    def update(self, *args, **kwargs):
        """Updates rectangle values
        """

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def __str__(self):
        """ overwrite str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
