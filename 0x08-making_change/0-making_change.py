#!/usr/bin/python3
"""
The methode of making change
"""


def makeChange(coins, total):
    """
    Output a minimum number of coins to meet up a given amount
    Args:
        coins (list of ints): a list of coins in different values
        total (int): total amount to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for v in coins:
        if total % v == 0:
            coin_count += int(total / v)
            return coin_count
        if total - v >= 0:
            if int(total / v) > 1:
                coin_count += int(total / v)
                total = total % v
            else:
                coin_count += 1
                total -= v
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
