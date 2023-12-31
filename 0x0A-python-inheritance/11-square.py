#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        self._size = size
        super().integer_validator(self._size, self._size)

    def __str__(self):
        """Returns str() representation of a Square."""
        return "[Square] {:d}/{:d}".format(self._size, self._size)

    def area(self):
        """Returns the area of the square."""
        return (self._size * self._size)
