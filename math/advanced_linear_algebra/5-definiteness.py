#!/usr/bin/env python3
"""Module for matrix"""


import numpy as np

def definiteness(matrix):
    """Determines the definiteness of a square matrix based on its eigenvalues."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1] or matrix.size == 0:
        return None
    if not np.allclose(matrix, matrix.T):
        return None
    try:
        eigenvalues = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        return None
    pos = np.all(eigenvalues > 1e-10)
    pos_semi = np.all(eigenvalues >= -1e-10)
    neg = np.all(eigenvalues < -1e-10)
    neg_semi = np.all(eigenvalues <= 1e-10)
    if pos:
        return "Positive definite"
    elif neg:
        return "Negative definite"
    elif pos_semi:
        return "Positive semi-definite"
    elif neg_semi:
        return "Negative semi-definite"
    any_pos = np.any(eigenvalues > 1e-10)
    any_neg = np.any(eigenvalues < -1e-10)
    if any_pos and any_neg:
        return "Indefinite"
    return None
