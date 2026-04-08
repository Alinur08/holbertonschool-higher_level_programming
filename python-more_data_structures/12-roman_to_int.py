#!/usr/bin/python3
from functools import reduce
def roman_to_int(roman_string):
    roman_integers=roman_string.split()
    alp={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500}
    r = reduce(lambda a,b: alp[a]+alp[b] if alp[a]>=alp[b] else alp[a]-alp[b],roman_integers)
    return r
