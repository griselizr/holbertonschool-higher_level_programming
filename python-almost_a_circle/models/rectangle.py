#!/usr/bin/python3
"""Creates a class Rectangle"""

from models.base import  Base

class Rectangle(Base):
    """Defines a class rectangle""" 

   
    def __init__(self, width, height, x=0, y=0, id=None): 
        """ initialization of private attributes """
        super().__init__(self, id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """get wight"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """set width"""
        self.___width = width
    
    @property
    def height(self):
        """get height """
        return self.__height
    
    @height.setter
    def height(self, height):
        """set height """
        self.__height = height
    
    @property
    def x(self):
        """get x """
        return self.__x
    
    @x.setter
    def x(self, x):
        """ set x """
        self.__x = x
    
    @property
    def y(self):
        """ get y """
        return self.__y
    
    @y.setter
    def y(self, y):
        """set y"""
        self.__y = y
