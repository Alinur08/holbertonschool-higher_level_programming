#!/usr/bin/python3
def common_elements(set_1, set_2):
    return set(filter(lambda x: True if x in set_2 else False, set_1))
