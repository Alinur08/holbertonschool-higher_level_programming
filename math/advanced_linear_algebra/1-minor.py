#!/usr/bin/env python3
"""Module for matrix"""


def determinant(matrix):
    """Helper function to calculate the determinant of a square matrix."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    det = 0
    for j in range(n):
        minor_sub = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor_sub)
    return det

def minor(matrix):
    """Helper function to calculate the minor of a square matrix."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")
    if n == 1:
        return [[1]]
    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            sub_matrix = [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]
            minor_row.append(determinant(sub_matrix))
        minor_matrix.append(minor_row)
    return minor_matrix
