import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n). Space: O(1)              !
# ---------------------------------------------------------------------
# Note:
# ---------------------------------------------------------------------
def solution(nums: List[int], k: int) -> int:
    """Given an array nums of positive integers sorted in a strictly
    increasing order, and an integer k. Return the k-th positive integer
    that is missing from this array.

    Examples:
        >>> solution([1, 2, 3, 4], 2)
        6
        >>> solution([2, 3, 4, 7, 11], 5)
        9
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] - 1 - mid < k:
            i += 1
        else:
            j -= 1
    return i + k


if __name__ == '__main__':
    doctest.testmod()
