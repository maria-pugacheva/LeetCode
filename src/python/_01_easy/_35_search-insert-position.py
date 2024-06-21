import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Check All. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], t: int) -> int:
    """Given a sorted array of distinct integers nums and a target
    value t, return the index if the target is found. If not, return
    the index where it would be if it was inserted in order.

    Examples:
        >>> solution_one([1], 2)
        1
        >>> solution_one([1, 3, 5, 6], 5)
        2
        >>> solution_one([1, 3, 5, 6], 2)
        1
        >>> solution_one([1, 3, 5, 6], 7)
        4
    """
    for i in range(len(nums)):
        if nums[i] >= t:
            return i
    return len(nums)


# ---------------------------------------------------------------------
# Approach 2: Binary Search. Time: O(log n)                         ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int], t: int) -> int:
    """Given a sorted array of distinct integers nums and a target
    value t, return the index if the target is found. If not, return
    the index where it would be if it was inserted in order.

    Examples:
        >>> solution_two([1], 2)
        1
        >>> solution_two([1, 3, 5, 6], 5)
        2
        >>> solution_two([1, 3, 5, 6], 2)
        1
        >>> solution_two([1, 3, 5, 6], 7)
        4
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if nums[mid] == t:
            return mid
        elif nums[mid] < t:
            i = mid + 1
        else:
            j = mid - 1
    return i


if __name__ == '__main__':
    doctest.testmod()
