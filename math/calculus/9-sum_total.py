#!/usr/bin/env python3
def count_down(n):
    if not isinstance(n, int):
        return
    if n == 0 or n == 1:
        return 1    
    return count_down(n - 1)*n
