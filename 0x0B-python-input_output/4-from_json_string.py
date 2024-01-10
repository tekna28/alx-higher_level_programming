#!/usr/bin/python3
"""Defining from_json_string that returns an object"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON str"""
    return json.loads(my_str)
