#!/usr/bin/env python3
"""Module to perform matrix operations"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Adding matrices"""
    mat = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        mat = mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        mat = [mat1[i] + mat2[i] for i in range(len(mat1))] 
    else:
        return None
    return mat
