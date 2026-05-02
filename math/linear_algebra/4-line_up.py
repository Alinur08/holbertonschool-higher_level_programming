#!/usr/bin/env python3
"""Module to perform matrix operations"""


def add_arrays(arr1, arr2):
    """Adding arrays"""
    if len(arr1) != len(arr2):
        return None
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    return arr
