#!/usr/bin/python3
"""
0-pascal_triangle.py

"""
def pascal_triangle(n):
    """ 
    Implements a pascal triangle of size n
    """
    triangle = []
    for i in range(n):
        t = []
        for j in range(i+1):
            if j == 0 or j == i:
                t.append(1)
            else:
                t.append(triangle[i -1][j -1] + triangle[i - 1][j])
        triangle.append(t)
    return triangle
