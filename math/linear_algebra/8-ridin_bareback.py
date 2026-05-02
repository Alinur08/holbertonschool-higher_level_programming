#!/usr/bin/env python3
"""Module to perform matrix operations"""


def mat_mul(mat1, mat2):
    """Multi Mat"""
    if len(mat1[0]) != len(mat2):
        return None
    mat = []
    for i in range(len(mat1)):
        row = []
        for k in range(len(mat2[0])):
            s = 0
            for j in range(len(mat1[0])):
                s += mat1[i][j] * mat2[j][k]
            row.append(s)
            
        mat.append(row)
    return mat
