#!/usr/bin/python3
'''
Write a function def pascal_triangle(n): to return lists of integers 
representing the Pascal's triangle of n:
'''

def pascal_triangle(n):
    '''
    process that writes lists of integers representing
    the Pascal's triangle of an integer.
    '''
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle
