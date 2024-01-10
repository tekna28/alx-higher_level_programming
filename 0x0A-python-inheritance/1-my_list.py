#!/usr/bin/python3
""" Defining a class MyList that inherits from list. """


class MyList(list):
    """ Implements sorted printing for the built-in class list. """

    def print_sorted(self):
        """ Prints the list, but sorted (ascending sort). """
        print(sorted(self))
