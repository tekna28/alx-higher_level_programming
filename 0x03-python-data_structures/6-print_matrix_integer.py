#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ for i in matrix: """
    for i in range(len(matrix)):
        """ for j in i: """
        for j in range(len(matrix[i])):
            """ print("{:d}".format(j), end=" " if j != i[-1] else "") """
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")

        print("")
