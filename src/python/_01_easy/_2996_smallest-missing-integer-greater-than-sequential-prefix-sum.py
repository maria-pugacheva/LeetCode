import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       !**
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Return the smallest integer x missing from nums such that x is
    greater than or equal to the sum of the longest sequential prefix.

    Examples:
        >>> solution([38])
        39
        >>> solution([38, 1])
        39
        >>> solution([9, 8, 7, 4, 9, 1, 5])
        10
        >>> solution([1, 2, 3, 2, 5])
        6
        >>> solution([3, 4, 5, 1, 12, 14, 13])
        15
    """
    res, i = nums[0], 1
    while i < len(nums) and nums[i] == nums[i - 1] + 1:
        res += nums[i]
        i += 1
    seen = set(nums)
    while res in seen:
        res += 1
    return res


if __name__ == '__main__':
    doctest.testmod()
