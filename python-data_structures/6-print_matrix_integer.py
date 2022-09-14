#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for columns in range(0, len(rows)):
            print("{:d}".format(rows[columns]), end="")
            if columns != len(rows) - 1:
                print(" ", end="")
        print("")
