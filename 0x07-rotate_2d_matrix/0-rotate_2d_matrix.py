#!/usr/bin/python3
"""
A process of rotation method.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the 2d matrix in place
    Args:
        matrix (list): 2d square matrix
    Return:
        None
    """
    n = len(matrix)
    for p in range(n):
        for v in range(i):
            temp = matrix[p][v]
            matrix[p][v] = matrix[v][p]
            matrix[v][p] = temp

    for p in range(n):
        for v in range(int(n / 2)):
            temp = matrix[p][v]
            matrix[p][v] = matrix[p][n-1-v]
            matrix[p][n-1-v] = temp
