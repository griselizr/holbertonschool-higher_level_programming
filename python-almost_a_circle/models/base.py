#!/usr/bin/python3
""" Class Base"""

import json


class Base:
    """ Defines a base model"""
    #private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
