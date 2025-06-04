import doctest
from typing import List
import math


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n * m)                           ***
# ---------------------------------------------------------------------
# Complexity Analysis: Let n be the length of the input array piles and
# m be the maximum number of bananas in a single pile from piles.
# ---------------------------------------------------------------------
def solution_one(piles: List[int], h: int) -> int:
    """Return the minimum integer k such that Koko can eat all the
    bananas within h hours.

    Examples:
        >>> solution_one([3, 6, 7, 11], 8)
        4
        >>> solution_one([30, 11, 23, 4, 20], 5)
        30
        >>> solution_one([30, 11, 23, 4, 20], 6)
        23
        >>> solution_one([312884470], 312884469)
        2
    """
    for k in range(1, max(piles) + 1):
        t = 0
        for p in piles:
            t += math.ceil(p / k)
        if t <= h:
            return k


# ---------------------------------------------------------------------
# Approach 2: Binary Search. Time: O(log m * n)                     !**
# ---------------------------------------------------------------------
# Complexity Analysis: Let n be the length of the input array piles and
# m be the maximum number of bananas in a single pile from piles. We're
# doing binary search over a range of possible speeds, from 1 to
# max(piles) (which is m).
# ---------------------------------------------------------------------
def solution_two(piles: List[int], h: int) -> int:
    """Return the minimum integer k such that Koko can eat all the
    bananas within h hours.

    Examples:
        >>> solution_two([3, 6, 7, 11], 8)
        4
        >>> solution_two([30, 11, 23, 4, 20], 5)
        30
        >>> solution_two([30, 11, 23, 4, 20], 6)
        23
        >>> solution_two([312884470], 312884469)
        2
    """
    i, j = 1, max(piles)
    res = j
    while i <= j:
        k = (i + j) // 2
        t = 0
        for p in piles:
            t += math.ceil(p / k)
        if t <= h:
            res = k
            j = k - 1
        else:
            i = k + 1
    return res


if __name__ == '__main__':
    doctest.testmod()
