#!/usr/bin/env python3
"""Module to determine the shape of a numpy array"""


def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray.
    
    Args:
        matrix (numpy.ndarray): The array to check.
        
    Returns:
        tuple: The dimensions of the matrix.
    """
    return matrix.shape