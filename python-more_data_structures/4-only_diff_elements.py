#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    r1 = set(filter(lambda x: False if x in set_2 else True, set_1))
    r2 = set(filter(lambda x: False if x in set_1 else True, set_2))
    return r1.union(r2)
