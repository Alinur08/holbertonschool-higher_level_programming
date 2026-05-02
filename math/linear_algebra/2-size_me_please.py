#!/usr/bin/env python3
def matrix_shape(matrix):
    """Return matrix shape"""
    shape = []
    while isinstance(matrix, list) and len(matrix) != 0:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
