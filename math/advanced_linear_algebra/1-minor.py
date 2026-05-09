#!/usr/bin/env python3
import numpy as np
"""Module for matrix"""


def minor(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or (n == 1 and len(matrix[0]) == 0):
        raise ValueError("matrix must be a non-empty square matrix")

    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1.0]]

    n = matrix.shape[0]
    minors = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            sub = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            minors[i, j] = np.linalg.det(sub)

    return minor.tolist()
