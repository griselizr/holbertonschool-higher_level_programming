#!/usr/bin/python3
"""creates an inherited list class MyList."""


class MyList(list):
    """ Defines a class with a subclass list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
