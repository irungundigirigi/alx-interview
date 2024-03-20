#!/usr/bin/env python3

"""
Module for calculating the minimum number of operations required to reach a certain number of characters.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    Args:
        n (int): The desired number of characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    min_ops = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            min_ops += divisor
            n //= divisor
        divisor += 1

    return min_ops

