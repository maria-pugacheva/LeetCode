import doctest
from typing import List
import math


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(n log m)                       !**
# ---------------------------------------------------------------------
# Complexity Analysis: Let n be the length of the input array piles and
# m be the maximum number of bananas in a single pile from piles.
# ---------------------------------------------------------------------
def solution(piles: List[int], h: int) -> int:
    """Return the minimum integer k such that Koko can eat all the
    bananas within h hours.

    Examples:
        >>> solution([3, 6, 7, 11], 8)
        4
        >>> solution([30, 11, 23, 4, 20], 5)
        30
        >>> solution([30, 11, 23, 4, 20], 6)
        23
    """
    i, j = 1, max(piles)
    while i < j:
        k = (i + j) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            j = k
        else:
            i = k + 1
    return j


if __name__ == '__main__':
    doctest.testmod()
