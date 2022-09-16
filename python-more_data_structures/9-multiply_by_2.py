#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nova = a_dictionary.copy()
    for todo in nova:    
        nova[todo] *= 2
    return nova
