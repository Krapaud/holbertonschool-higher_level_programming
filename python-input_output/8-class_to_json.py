#!/usr/bin/python3
"""Module that contains a function to convert class to JSON"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure 
    (list, dictionary, string, integer and boolean) for JSON serialization of an object
    
    Args:
        obj: An instance of a Class
        
    Returns:
        dict: Dictionary description of the object
    """
    dict_json_attributes = {}
    for attribute, value in obj.__dict__.items():
        if type(value) in [list, dict, str, int, bool, float, type(None)]:
            dict_json_attributes[attribute] = value
    return dict_json_attributes