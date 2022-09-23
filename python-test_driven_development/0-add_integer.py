#!/usr/bin/python3
""" add two integers """


def add_integer(a, b=98):
    """ Define add integer  a + b"""
    if not type(a) is int is not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int is not type(b) is float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
