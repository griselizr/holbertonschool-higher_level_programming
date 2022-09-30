#!/usr/bin/python3

def inherits_from(obj, a_class):
    ""Defines an inherited from to a class"""


def inherits_from(obj, a_class):
    """ Verify  if an object is an inherited instance of a class.
    Arguments:
        obj : the object 
        a_class (type): The class to pait the obj
    Returns:
        If obj is an inherited instance of a_class  is True.
        Otherwise is False.
    """


    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
