#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Class Student that defines a student by:"""

    def __init__(self, first_name, last_name, age):
        """Public instance attributes:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation"""
        return self.__dict__
