#!/usr/bin/env python3
"""
Pickle serialization module for custom Python objects
"""
import pickle


class CustomObject:
    """
    Custom class for demonstrating pickle serialization
    """

    def __init__(self, name=None, age=None, is_student=None):
        """
        Initialize CustomObject

        Args:
            name (str): Name of the person
            age (int): Age of the person
            is_student (bool): Student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display object's attributes in the specified format
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle

        Args:
            filename (str): File to save the serialized object
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle

        Args:
            filename (str): File to load the serialized object from

        Returns:
            CustomObject instance or None if error
        """
        with open(filename, 'rb') as f:
            obj = pickle.load(f)
        return obj
