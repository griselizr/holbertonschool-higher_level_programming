#!/usr/bin/python3
def add_integer(a, b=98):
        """ sum of a and B"""

        
    if type(a) is not int or float:
            raise TypeError("a must be an integer")
    if type(b) is not int or float:
            raise TypeError("b must be an integer")
    if type(a) is a float:
            a = int(a)
    if type(b) is a float:
            b = int(b)
            return a + b
