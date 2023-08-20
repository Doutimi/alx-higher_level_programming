#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        t_next = triangle[-1]
        tmp = [1]
        for i in range(len(t_next) - 1):
            tmp.append(t_next[i] + t_next[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
