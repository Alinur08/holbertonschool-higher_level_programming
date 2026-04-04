#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print(f"{chr(ord(c)-32) if 'a' <= c <= 'z' else c}", end="")
    print()
