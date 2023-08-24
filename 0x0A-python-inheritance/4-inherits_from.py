#!/usr/bin/python3

"""
This function checks if the object is an instance of a class
or a subclass of the specified class.
"""


def inherits_from(obj, a_class):

    """ Checks if an object is an instance of a class inherited
    from the specified class.

    Args:
    obj (object): The object to be checked.
    a_class (class): The class to be checked against.

    Returns:
    bool: True if the object is an instance of a class or a subclass
    of the specified class, otherwise False."""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
