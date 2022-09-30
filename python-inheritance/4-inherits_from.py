#!/usr/bin/python3
"""Defines an inherited from to a aclass"""


def inherits_from(obj, a_class):
    """
    Verify if an object is an inherited of a class
    obj:the object , a_class (type): the class to pair the obj
    Returns: If obj is an inherited instance of a_class is True,
    Otherwise is False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
