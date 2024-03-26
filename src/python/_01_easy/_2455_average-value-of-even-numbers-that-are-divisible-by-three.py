import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Modulo. Time: O(n)                                    ^**
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given an integer array nums of positive integers, return the
    average value of all even integers that are divisible by 3.

    Examples:
        >>> solution([1, 2, 4, 7, 10])
        0
        >>> solution([1, 3, 6, 10, 12, 15])
        9
        >>> solution([9, 3, 8, 4, 2, 5, 3, 8, 6, 1])
        6
    """
    res = cnt = 0
    for n in nums:
        if n % 6 == 0:
            res += n
            cnt += 1
    return res if cnt == 0 else res // cnt


if __name__ == '__main__':
    doctest.testmod()
