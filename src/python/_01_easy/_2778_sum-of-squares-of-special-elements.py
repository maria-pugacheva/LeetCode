import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given a 1-indexed integer array nums of length n, return the sum
    of the squares of all special elements of nums. An element nums[i]
    is called special if n % i == 0.

    Examples:
        >>> solution([1, 2, 3, 4])
        21
        >>> solution([2, 7, 1, 19, 18, 3])
        63
    """
    res = 0
    for i in range(len(nums)):
        if len(nums) % (i + 1) == 0:
            res += (nums[i] * nums[i])
    return res


if __name__ == '__main__':
    doctest.testmod()
