import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n)                         !!!
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Find a peak element, an element that is strictly greater than its
    neighbors, and return its index.

    Examples:
        >>> solution_one([3])
        0
        >>> solution_one([1, 3])
        1
        >>> solution_one([3, 1])
        0
        >>> solution_one([1, 3, 2])
        1
        >>> solution_one([1, 2, 0, 5])
        1
        >>> solution_one([1, 2, 3, 1])
        2
    """
    i, j = 0, len(nums) - 1
    while i < j:
        mid = i + (j - i) // 2
        if nums[mid] > nums[mid + 1]:
            j = mid
        else:
            i = mid + 1
    return i


if __name__ == '__main__':
    doctest.testmod()
