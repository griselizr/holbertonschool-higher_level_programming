#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     for rows in range(len(matrix)):
        for columns in range(len(matrix[rows])):
            if columns == len(matrix[rows]) - 1:
                print("{:d}".format[matrix[rows][columns], end="")
            else:
                print("{:d}".format[matrix[rows][columns], "", end="")
        print("")
