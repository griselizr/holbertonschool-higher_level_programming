#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            newstr += idx
    return newstr
