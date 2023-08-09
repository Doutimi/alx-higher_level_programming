#!/usr/bin/python3
class LockedClass:
    '''This class prevents the user from dynamically creating new instance attributes

    Atrributes:
        none
    '''
    __slots__ = ["first_name"]
