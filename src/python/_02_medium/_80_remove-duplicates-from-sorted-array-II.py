import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Delete. Time: O(n^2)                                  ^**
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Given an integer array nums sorted in non-decreasing order,
    remove some duplicates in-place such that each unique element
    appears at most twice.

    Examples:
        >>> solution_one([1, 1, 1, 2, 2, 3])
        5
        >>> solution_one([0, 0, 1, 1, 1, 1, 2, 3, 3])
        7
    """
    i = 1
    cnt = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            cnt += 1
            if cnt > 2:
                nums.pop(i)
                i -= 1
        else:
            cnt = 1
        i += 1
    return i


# ---------------------------------------------------------------------
# Approach 2: Overwrite. Time: O(n)                                   !
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Given an integer array nums sorted in non-decreasing order,
    remove some duplicates in-place such that each unique element
    appears at most twice.

    Examples:
        >>> solution_two([1, 1, 1, 2, 2, 3])
        5
        >>> solution_two([0, 0, 1, 1, 1, 1, 2, 3, 3])
        7
    """
    i = 1
    cnt = 1
    for j in range(1, len(nums)):
        if nums[j] == nums[j - 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt <= 2:
            nums[i] = nums[j]
            i += 1
    return i


if __name__ == '__main__':
    doctest.testmod()
