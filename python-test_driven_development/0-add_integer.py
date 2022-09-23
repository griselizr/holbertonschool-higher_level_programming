#!/usr/bin/python3
""" add two integers """


def add_integer(a, b=98):
""" sum of a and b"""    
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is a float:
        a = int(a)
    if type(b) is a float:
        b = int(b)
        return a + b
