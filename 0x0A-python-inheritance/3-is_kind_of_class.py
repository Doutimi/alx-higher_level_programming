#!/usr/bin/python3
"""Checks instance of an object"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of the specified class
    Args:
        obj: Object to be checked
        a_class: the class to compare
    Returns:
        bool: True for isinstance of obj or False if not
    """
    return isinstance(obj, a_class)
