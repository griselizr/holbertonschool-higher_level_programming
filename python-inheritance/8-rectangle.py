#!/usr/bin/python3
"""Creates a class Rectangle that inherits from BaseGeometry"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Defines a rectangle class"""

    def __init__(self, width, height):
        """initialize rectangle
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
