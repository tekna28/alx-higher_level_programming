#!/usr/bin/python3
"""Defining a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Documentation for the Square class."""

    def __init__(self, size):
        """Initializes the Square instance with size."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return "[Square] {}/{}".format(self.__size, self.__size)
