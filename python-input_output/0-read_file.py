#!/usr/bin/python3
"""Module that contains a function to read a file"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): The name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
