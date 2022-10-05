#!/usr/bin/python3
"""creates a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)
