import doctest
from typing import List
from collections import Counter


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> bool:
    """Return True if nums is a good array; otherwise, return False.
    An array is said to be good if it is an array of length n + 1, it
    contains elements from 1 to n - 1 exactly once and has two
    occurrences of n.

    Examples:
        >>> solution_one([1])
        False
        >>> solution_one([1, 1])
        True
        >>> solution_one([2, 1, 3])
        False
        >>> solution_one([1, 3, 3, 2])
        True
        >>> solution_one([3, 4, 4, 1, 2, 1])
        False
    """
    nums.sort()
    n = 1
    for i in range(len(nums) - 2):
        if nums[i] != n:
            return False
        n += 1
    return len(nums) >= 2 and nums[-1] == nums[-2] == n


# ---------------------------------------------------------------------
# Approach 2: Counter. Time: O(n)                                   ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> bool:
    """Return True if nums is a good array; otherwise, return False.
    An array is said to be good if it is an array of length n + 1, it
    contains elements from 1 to n - 1 exactly once and has two
    occurrences of n.

    Examples:
        >>> solution_two([1])
        False
        >>> solution_two([1, 1])
        True
        >>> solution_two([2, 1, 3])
        False
        >>> solution_two([1, 3, 3, 2])
        True
        >>> solution_two([3, 4, 4, 1, 2, 1])
        False
    """
    c = Counter(nums)
    for n in range(1, len(nums) - 1):
        if n not in c:
            return False
    return c[len(nums) - 1] == 2


if __name__ == '__main__':
    doctest.testmod()
