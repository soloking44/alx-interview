#!/usr/bin/python3
"""This represnts UTF-8 encoding.
"""


def validUTF8(data):
    """It verifies that array of integers is correct unicode values.
    See if it returns true if data is valid else return false
    """
    skip = 0
    n = len(data)
    for k in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[k]) != int or data[k] < 0 or data[k] > 0x10ffff:
            return False
        elif data[k] <= 0x7f:
            skip = 0
        elif data[k] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if n - k >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[k + 1: k + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[k] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if n - k >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[k + 1: k + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[k] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if n - k >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[k + 1: k + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
