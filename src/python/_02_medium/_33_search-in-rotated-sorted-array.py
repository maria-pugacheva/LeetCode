import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n)                         ***
# ---------------------------------------------------------------------
def solution(nums: List[int], t: int) -> int:
    """Given an array nums sorted in ascending order (with distinct
    values) and possibly rotated, and an integer t, return the index of
    t if it is in nums; otherwise, return -1 if it is not in nums.

    Examples:
        >>> solution([1], 0)
        -1
        >>> solution([1, 2], 1)
        0
        >>> solution([2, 1], 1)
        1
        >>> solution([3, 5, 1], 3)
        0
        >>> solution([5, 1, 3], 3)
        2
        >>> solution([4, 5, 6, 7, 0, 1, 2], 1)
        5
        >>> solution([4, 5, 6, 7, 0, 1, 2], 3)
        -1
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] == t:
            return m
        elif nums[0] <= nums[m]:
            if nums[0] <= t < nums[m]:
                j = m - 1
            else:
                i = m + 1
        else:
            if nums[m] < t <= nums[-1]:
                i = m + 1
            else:
                j = m - 1
    return -1


if __name__ == '__main__':
    doctest.testmod()
