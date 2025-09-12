#!/usr/bin/python3
"""Module that prints a text with 2 new lines after certain characters.

This module contains a function that formats text with indentation.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The text to format (string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        char = text[i]
        if char in ['.', '?', ':']:
            print(char, end="\n\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            i -= 1
        else:
            print(char, end="")
        i += 1
    return
