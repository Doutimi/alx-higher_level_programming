#!/usr/bin/python3
"""Defines a class that inverts the != and == operators"""


class MyInt(int):
    """Defines a class MyInt inherited from int"""

    def __eq__(self, other):
        """Switches the == operator to !="""
        return self.real != other

    def __ne__(self, other):
        """switches the != operator to =="""
        return self.real == other
