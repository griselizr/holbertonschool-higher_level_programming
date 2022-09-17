#!/usr/bin/python3
def safe_print_division(a, b):
    total = 0.0
    try:
        result = a / b
    except ZeroDivisionError:
        total = None
    finally:
        print("Inside result: {}".format(total))
    return total
