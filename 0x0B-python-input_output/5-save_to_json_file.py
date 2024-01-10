#!/usr/bin/python3
"""Defines save_to_json_file that creates an Object from a "JSON file" """
import json


def save_to_json_file(my_obj, filename):
    """Saves to json file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
