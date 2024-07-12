import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sliding Window. Time: O(n)                            ***
# ---------------------------------------------------------------------
def solution(nums: List[int], t: int) -> int:
    """Given an array of positive integers nums and a positive integer
    t, return the minimal length of a sub-array whose sum is greater
    than or equal to t. If there is no such sub-array, return 0 instead.

    Examples:
        >>> solution([1, 1, 1, 1, 1, 1, 1, 1], 11)
        0
        >>> solution([1, 4, 4], 4)
        1
        >>> solution([2, 3, 1, 2, 4, 3], 7)
        2
    """
    length = len(nums)
    res, curr, i = length + 1, 0, 0
    for j in range(length):
        curr += nums[j]
        while curr >= t:
            res = min(res, j - i + 1)
            curr -= nums[i]
            i += 1
    return res if res != length + 1 else 0


if __name__ == '__main__':
    doctest.testmod()
