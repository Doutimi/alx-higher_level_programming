#!/usr/bin/python3
"""Checks instance of an object"""


def is_same_class(obj, a_class):
    """checks if obj is exactly an instance of the specified class
    Args:
        obj: Object to be checked
        a_class: the class to compare
    Returns:
        bool: True for isinstance of obj or False if not
    """
    return type(obj) is a_class
