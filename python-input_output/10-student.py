#!/usr/bin/python3
"""Module that defines a Student class with filter"""


class Student:
    """
    A class that defines a student
    
    Attributes:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student
    """
    
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        
        Args:
            attrs (list): List of strings, only attribute names contained in this list must be retrieved
            
        Returns:
            dict: Dictionary representation of the Student instance
        """
        dict_json_attributes = {}
        
        if attrs is None:
            for attribute, value in self.__dict__.items():
                if type(value) in [list, dict, str, int, bool, float, type(None)]:
                    dict_json_attributes[attribute] = value
            return dict_json_attributes
        
        elif isinstance(attrs, list):
            for attribute in attrs:
                if hasattr(self, attribute):
                    value = getattr(self, attribute)
                    if type(value) in [list, dict, str, int, bool, float, type(None)]:
                        dict_json_attributes[attribute] = value
            return dict_json_attributes
        else:
            return {}
