import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given an integer array nums of size n, return the number with the
    value closest to 0 in nums. If there are multiple answers, return
    the number with the largest value.

    Examples:
        >>> solution([-2, -1, 1])
        1
        >>> solution([-1, 1, 0])
        0
        >>> solution([-4, -2, 1, 4, 8])
        1
    """
    res = float('inf')
    for n in nums:
        if abs(n) < abs(res) or (res < 0 and abs(res) == n):
            res = n
    return res


if __name__ == '__main__':
    doctest.testmod()
