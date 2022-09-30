#!/usr/bin/python3
""" Creates a BaseGeometry."""


class BaseGeometry:
    """ Defines the base geometry."""

    def area(self):
        """ Does not have"""
        raise Exception("area() is not implemented")
