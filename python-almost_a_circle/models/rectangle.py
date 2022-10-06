#!/usr/bin/python3
"""Creates a class Rectangle"""

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
    def width(self, width):
        """set width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width  must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """get height """
        return self.__height

    @height.setter
    def height(self, height):
        """set height """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(height) < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """get x """
        return self.__x

    @x.setter
    def x(self, x):
        """ set x """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
