#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    first = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list), end="")
            first += 1
        except (ValueError, TypeError):
            continue
    print()
    return (first)
