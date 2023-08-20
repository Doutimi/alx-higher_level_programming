#!/usr/bin/python3
"""defines a lookup function"""


def lookup(obj):
    """Returns a list of an object's available attributes."""
    return dir(obj)
