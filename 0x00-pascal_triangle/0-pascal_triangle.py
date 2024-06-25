#!/usr/bin/python3
"""Create a function that return lists of integers"""


def pascal_triangle(n):
    """
    a function that returns a list
    of integers representing the
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    pascal_tri = []

    if n <= 0:
        return []

    for k in range(n):
        if (k == 0):
            pascal_tri.append([1])
        else:
            cur_row = []
            for m in range(k + 1):
                if (m == 0 or m == k):
                    cur_row.append(1)
                else:
                    cur_row.append(pascal_tri[k - 1][m - 1] +
                                   pascal_tri[k - 1][m])

            pascal_tri.append(cur_row)

    return (pascal_tri)
