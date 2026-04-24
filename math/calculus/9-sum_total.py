#!/usr/bin/python3
def summation_i_squared(n):
    if isinstance(n, int):
        s = 0
        for i in range(1, n+1):
            s += i**2
        return s
    return None
