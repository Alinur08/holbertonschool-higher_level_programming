#!/usr/bin/env python3
def summation_i_squared(n):
    if isinstance(n, int):
        s = 0
        i = 1
        while i <= n:
            s += i**2
            i += 1
        return s
    return None
