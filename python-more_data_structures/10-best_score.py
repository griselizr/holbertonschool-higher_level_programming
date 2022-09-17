#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    score = max(a_dictionary.values(), default=None)
    for keys, val in a_dictionary.items():
        if val == score:
            return keys
