#!/usr/bin/env python3
def summation_i_squared(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    # Add n squared to the sum of the previous squares
    return summation_i_squared(n - 1) + (n ** 2)
