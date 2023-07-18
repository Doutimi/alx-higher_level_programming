#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Print each cell in the row, separated by a space
        print(' '.join(['{:d}'.format(cell) for cell in row]))
