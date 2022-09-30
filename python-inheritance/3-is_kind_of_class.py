#!/usr/bin/python3
""" Creates a kind of class and inherited class """


def is_kind_of_class(obj, a_class):
    """ Verify if an object is an instance or inherited instance of a class.
    Args:
        obj: the object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class is True.
        Otherwise is False.
    """
    if isinstance(obj, a_class):
        return True
    return False
