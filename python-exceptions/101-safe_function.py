#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        total = fct(*args)
        return(total)
    except Exception as mistake:
        print("Exception: {}".format(mistake), file=sys.stderr)
