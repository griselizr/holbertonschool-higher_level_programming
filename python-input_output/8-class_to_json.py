#!/usr/bin/python3
"""
Creates JSON serialization of
an object to return 
a dictionary with list, dictionary, string, 
integer and boolean
"""


def class_to_json(obj):
    """Return the dictionary represntation of a 
    simple data structure.
    """
    return obj.__dict__
