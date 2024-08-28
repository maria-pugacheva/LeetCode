import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n)                         ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Given a sorted rotated array nums of unique elements, return the
    minimum element of this array.

    Examples:
        >>> solution_one([1, 2])
        1
        >>> solution_one([2, 1])
        1
        >>> solution_one([3, 4, 5, 1, 2])
        1
        >>> solution_one([11, 13, 15, 17])
        11
        >>> solution_one([4, 5, 6, 7, 0, 1, 2])
        0
    """
    i, j = 0, len(nums) - 1
    while i < j:
        mid = (i + j) // 2
        if mid < len(nums) - 1 and nums[mid] > nums[-1]:
            i = mid + 1
        else:
            j = mid
    return nums[j]


if __name__ == '__main__':
    doctest.testmod()
