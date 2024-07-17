#!/usr/bin/python3
"""
A code for parsing logs.
"""


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for keys, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(keys, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for keys, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(keys, value))
