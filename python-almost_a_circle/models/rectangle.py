#!/usr/bin/python3
"""Creates a class Rectangle"""


class Rectangle(Base):
"""Defines a class rectangle""" 

   
    def __init__(self, width, height, x=0, y=0, id=None): 
        """ initialization of private attributes """
          super(Base, id, self).__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """get wight"""
        return self.__width
    
    @width.setter
    def width(self, ___width = width):
        """set width"""
        return self.___width = width
    
    @property
    def height(self):
        """get height """
        return self.__height
    
    @height.setter
    def height(self, __height = height):
        """set height """
        return self.__height = height
    
    @property
    def x(self):
        """get x """
        return self.__x
    
    @x.setter
    def x(self, __x = x):
        """ set x """
        return self.__x = x
    
    @property
    def y(self):
        """ get y """
        return self.__y
    
    @y.setter
    def y(self,__y = y):
        """set y"""
        return self.__y = y
    