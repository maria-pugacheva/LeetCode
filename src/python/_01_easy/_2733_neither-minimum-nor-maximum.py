import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Given an integer array nums containing distinct positive
    integers, find and return any number from the array that is neither
    the minimum nor the maximum value in the array, or -1 if there is
    no such number.

    Examples:
        >>> solution_one([1])
        -1
        >>> solution_one([1, 2])
        -1
        >>> solution_one([3, 30, 24])
        24
        >>> solution_one([3, 2, 1, 4])
        3
        >>> solution_one([2, 1, 3])
        2
    """
    if len(nums) <= 2:
        return -1
    max_v, min_v, n = nums[0], nums[0], -1
    for i in range(1, len(nums)):
        if nums[i] > max_v:
            max_v, n = nums[i], max_v
        elif nums[i] < min_v:
            min_v, n = nums[i], min_v
        else:
            n = nums[i]
    return n


# ---------------------------------------------------------------------
# Approach 2: Only First Three. Time: O(1)                          ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Given an integer array nums containing distinct positive
    integers, find and return any number from the array that is neither
    the minimum nor the maximum value in the array, or -1 if there is
    no such number.

    Examples:
        >>> solution_two([1])
        -1
        >>> solution_two([1, 2])
        -1
        >>> solution_two([3, 30, 24])
        24
        >>> solution_two([3, 2, 1, 4])
        2
        >>> solution_two([2, 1, 3])
        2
    """
    if len(nums) <= 2:
        return -1
    min_v, max_v = min(nums[0], nums[1]), max(nums[0], nums[1])
    if nums[2] < min_v:
        return min_v
    elif nums[2] > max_v:
        return max_v
    return nums[2]


if __name__ == '__main__':
    doctest.testmod()
