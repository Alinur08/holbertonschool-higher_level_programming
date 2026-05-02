#!/usr/bin/env python3
"""Return matrix shape"""
def matrix_shape(matrix):
    shape = []
    while isinstance(matrix, list) and len(matrix) != 0:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
