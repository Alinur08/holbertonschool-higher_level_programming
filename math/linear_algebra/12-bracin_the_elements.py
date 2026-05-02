#!/usr/bin/env python3
"""Module for element-wise operations using NumPy"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.
    """
    sum_res = mat1 + mat2
    diff_res = mat1 - mat2
    prod_res = mat1 * mat2
    quot_res = mat1 / mat2
    return (sum_res, diff_res, prod_res, quot_res)
