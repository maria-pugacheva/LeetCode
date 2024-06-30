import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Slicing. Time: O(n)                                   ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], k: int) -> List[int]:
    """Given an integer array nums, rotate the array to the right by k
    steps, where k is non-negative..

    Examples:
        >>> solution_one([1, 2], 3)
        [2, 1]
        >>> solution_one([-1, -100, 3, 99], 2)
        [3, 99, -1, -100]
        >>> solution_one([1, 2, 3, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 2, 3, 4]
    """
    n = len(nums)
    if k > n:
        k %= n
    return nums[n - k:] + nums[:n - k]


# ---------------------------------------------------------------------
# Approach 2: Reverse. Time: O(n)                                   ^**
# ---------------------------------------------------------------------
def solution_two(nums: List[int], k: int) -> List[int]:
    """Given an integer array nums, rotate the array to the right by k
    steps, where k is non-negative..

    Examples:
        >>> solution_two([1, 2], 3)
        [2, 1]
        >>> solution_two([-1, -100, 3, 99], 2)
        [3, 99, -1, -100]
        >>> solution_two([1, 2, 3, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 2, 3, 4]
    """
    def reverse(i: int, j: int):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    n = len(nums)
    if k > n:
        k %= n
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums


if __name__ == '__main__':
    doctest.testmod()
