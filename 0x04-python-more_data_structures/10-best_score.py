#!/usr/bin/python3

def best_score(a_dictionary):
    key = None
    best = -1
    if (a_dictionary is None):
        return key
    for i, j in a_dictionary.items():
        if j > best:
            best = j
            key = i
    return (key)
