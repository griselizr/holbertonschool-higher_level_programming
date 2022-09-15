#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) >= 2:
        new = (tuple_b[0], tuple_b[1])
    if len(tuple_b) == 1:
        new= (tuple_b[0], 0)
    if len(tuple_b) == 0:
        new = (0, 0)
    if len(tuple_a) >= 2:
        new_a = (tuple_a[0], tuple_a[1])
    if len(tuple_a) == 1:
        new_a = (tuple_a[0], 0)
    if len(tuple_a) == 0:
        new_a = (0, 0)
    tuple_c = ((new_a[0] + new[0]), (new_a[1] + new[1]))
    return tuple_c
