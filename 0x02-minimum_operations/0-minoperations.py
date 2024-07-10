#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    A method that calculates the fewest number of operations
    needed to result in exactly n H character in a file.
    Returns an interger. If n is impossible to achive , returns 0
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
