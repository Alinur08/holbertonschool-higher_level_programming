#!/usr/bin/python3
def roman_to_int(roman_string):
    alp={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500}
    r=0
    for i in range(len(roman_string)-1):
        a=roman_string[i]
        b=roman_string[i+1]
        r+=alp[a] if alp[a]>=alp[b] else -alp[a]
    r+=alp[roman_string[-1]]
    return r
