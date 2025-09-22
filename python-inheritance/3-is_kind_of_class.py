#!/usr/bin/python3
"""Module for is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class"""
    if not isinstance(obj, a_class):
        return False
    else:
        return True
