#!/usr/bin/python3
"""
Module for converting CSV files to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format.
    
    This function reads data from a CSV file and converts it to JSON format,
    saving the result to 'data.json'. Each row in the CSV becomes a dictionary
    in the JSON array, with CSV headers as keys.
    
    Args:
        csv_filename (str): The name of the CSV file to convert
        
    Returns:
        bool: True if conversion is successful, False otherwise
    """
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
            
        return True
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
