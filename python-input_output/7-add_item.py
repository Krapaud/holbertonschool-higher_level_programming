#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and then save them to
a file"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to save
        filename (str): The name of the file to save to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"

    Args:
        filename (str): The name of the JSON file to load from

    Returns:
        object: The object loaded from the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    my_list = []

arguments = sys.argv[1:]
my_list.extend(arguments)

save_to_json_file(my_list, filename)
