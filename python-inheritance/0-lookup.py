#!/usr/bin/python3
"""Module for object attribute lookup."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing attributes and methods.
    """
    return dir(obj)
