#!/usr/bin/env python3
"""Module to perform matrix operations"""

def add_matrices2D(mat1, mat2):
    """Adding arrays"""
    if not all(len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])):
        return None
    mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        mat.append(row)
    return mat
