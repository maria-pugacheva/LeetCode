import doctest
from typing import List
from collections import Counter


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Given an array nums of size n, return the majority element. The
    majority element is the element that appears more than [n//2] times.

    Examples:
        >>> solution_one([3, 2, 3])
        3
        >>> solution_one([2, 2, 1, 1, 1, 2, 2])
        2
        >>> solution_one([2, 2, 1, 1, 1, 2, 2, 1, 1])
        1
    """
    nums.sort()
    return nums[len(nums) // 2]


# ---------------------------------------------------------------------
# Approach 2: Counter. Time: O(n)                                   ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Given an array nums of size n, return the majority element. The
    majority element is the element that appears more than [n//2] times.

    Examples:
        >>> solution_two([3, 2, 3])
        3
        >>> solution_two([2, 2, 1, 1, 1, 2, 2])
        2
        >>> solution_two([2, 2, 1, 1, 1, 2, 2, 1, 1])
        1
    """
    c = Counter(nums)
    length = len(nums)
    for k, v in c.items():
        if v > length // 2:
            return k
    return -1


if __name__ == '__main__':
    doctest.testmod()
