#!/usr/bin/python3
"""
Includes a method to compute the minimum number of operations required to produce exactly n H characters in the file.
"""


def minOperations(n):
    if n == 1:
        return 0

    operations = 0
    h = 1
    while h < n:
        if n % h == 0:
            h_copy = h
            ops += 1
        h += h_copy
        operations += 1

    if h == n:
        return operations
    else:
        return 0
