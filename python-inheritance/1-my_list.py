#!/usr/bin/python3
"""Module for object attribute lookup."""


class MyList(list):
    """
        Mylist class
    """
    
    def print_sorted(self):
        self.sort()
        print(self)
