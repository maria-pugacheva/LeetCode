import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given an integer array nums, return the most frequent even
    element. If there is a tie, return the smallest one. If there is no
    such element, return -1.

    Examples:
        >>> solution([0, 1, 4, 4, 2, 1, 2])
        2
        >>> solution([4, 4, 4, 9, 2, 4])
        4
        >>> solution([5, 7, 11])
        -1
        >>> solution([0])
        0
    """
    cnt = {}
    freq, v = 0, -1
    for n in nums:
        if n % 2 == 0:
            cnt[n] = cnt.get(n, 0) + 1
            if cnt[n] > freq or (cnt[n] == freq and n < v):
                freq = cnt[n]
                v = n
    return v


if __name__ == '__main__':
    doctest.testmod()
