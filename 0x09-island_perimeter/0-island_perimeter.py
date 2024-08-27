#!/usr/bin/python3
"""A method of island perimeter computing.
"""


def island_perimeter(grid):
    """Computes perimeter of the island without lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for k, row in enumerate(grid):
        m = len(row)
        for p, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                k == 0 or (len(grid[k - 1]) > p and grid[k - 1][p] == 0),
                p == m - 1 or (m > p + 1 and row[p + 1] == 0),
                k == n - 1 or (len(grid[k + 1]) > p and grid[k + 1][p] == 0),
                p == 0 or row[p - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
