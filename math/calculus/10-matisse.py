#!/usr/bin/env python3
"""Module for polynomial derivative calculation"""


def poly_derivative(poly):
    """Calculates sum from i=1 to n of i^2"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = [i * poly[i] for i in range(1, len(poly))]
    if not derivative or all(c == 0 for c in derivative):
        return [0]

    return derivative
