#!/usr/bin/python3
"""
This is a solution to queens puzzle.
"""
import sys


solutions = []
"""A set of method of a queens problem.
"""
n = 0
"""A size of an chessboard.
"""
pos = None
"""A set of index in a chessboard.
"""


def get_input():
    """Fetchs and reviews the program argument.

    Returns:
        int: A size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Sees if the queens is in attacking mode.

    Args:
        pos0 (list or tuple): A first queen's position.
        pos1 (list or tuple): A second queen's position.

    Returns:
        bool: True if queens is in attacking position else False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Sees when group exists in a set of solutions.

    Args:
        group (list of integers): The group of positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        g = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    g += 1
        if g == n:
            return True
    return False


def build_solution(row, group):
    """Creates the solution of queens problem.

    Args:
        row (int): A fresh row in a chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Fetchs a method of a chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
