#!/usr/bin/env python3
"""Module for matrix"""


def determinant(matrix):
    """Function that calculate matrix"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]] or len(matrix) == 0:
        return 1
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a square matrix")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][2])
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        sign = (-1) ** j
        det += sign * matrix[0][j] * determinant(minor)
    return det
