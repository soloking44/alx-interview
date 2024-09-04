#!/usr/bin/python3
"""
This is prime game
"""


def isWinner(x, nums):
    """Checks for a winner of prime game `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # creates primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for z, is_prime in enumerate(primes, 1):
        if z == 1 or not is_prime:
            continue
        for p in range(z + z, n + 1, z):
            primes[p - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
