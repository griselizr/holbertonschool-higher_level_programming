#!/usr/bin/python3
""" creating an instance of a class or otherwise """


def is_same_class(obj, a_class):
    """ verify if an object is exactly an instance of a given class.
        obj: the object 
        a_class (type): The class to pair with  obj to.
    Returns:
        If obj is exactly an instance of a_class the result is True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
