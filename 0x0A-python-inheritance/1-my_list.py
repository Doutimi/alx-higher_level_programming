#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """Initializes the class with the superclass's constructor"""
        super().__init__()

    def print_sorted(self):
        """ Method to print the sorted list"""
        print(sorted(self))
