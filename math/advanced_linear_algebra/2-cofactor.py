#!/usr/bin/env python3
"""Module for matrix"""


def determinant(matrix):
    """Helper function to calculate the determinant of a square matrix."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(size):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub_matrix)
    return det

def cofactor(matrix):
    """Calculates the cofactor matrix of a square matrix."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if n == 1:
        return [[1]]
    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor_matrix = [
                row[:j] + row[j+1:] 
                for k, row in enumerate(matrix) if k != i
            ]
            minor_val = determinant(minor_matrix)
            cofactor_val = ((-1) ** (i + j)) * minor_val
            cofactor_row.append(cofactor_val)
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix
