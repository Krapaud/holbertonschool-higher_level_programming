#!/usr/bin/python3
"""Module that contains a function to convert class to JSON"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object

    Args:
        obj: An instance of a Class

    Returns:
        dict: Dictionary description of the object
    """
    return obj.__dict__
