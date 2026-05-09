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
    # 1. Validation: Check if it's a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # 2. Validation: Check if it is empty or non-square
    n = len(matrix)
    if n == 0 or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    # Special case: 1x1 matrix minor is typically defined as 1 
    if n == 1:
        return [[1]]

    # 3. Calculate the Matrix of Minors
    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            # Create sub-matrix by removing row i and column j
            sub_matrix = [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]
            
            # The minor is the determinant of this sub-matrix
            minor_row.append(determinant(sub_matrix))
        minor_matrix.append(minor_row)
        
    return minor_matrix