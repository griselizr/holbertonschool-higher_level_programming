#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """ Read the text inside the file and print"""
    
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end='')
