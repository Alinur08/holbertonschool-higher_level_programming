#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A class that inherits from the built-in list."""

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
