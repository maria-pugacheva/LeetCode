import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sort. Time: O(n log n)                                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> bool:
    """Given an integer array nums consisting of 2 * n integers, return
    True if nums can be divided into n pairs where each element belongs
    to exactly one pair and the elements present in a pair are equal.
    Otherwise, return False.

    Note: Could also use XOR after sorting (won't work w/o sorting).
          Consider this example: 20^17^6^12^11^4 = 0

    Examples:
        >>> solution_one([3, 2, 3, 2, 2, 2])
        True
        >>> solution_one([1, 2, 3, 4])
        False
        >>> solution_one([3, 3, 3, 5])
        False
    """
    nums.sort()
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return False
    return True


# ---------------------------------------------------------------------
# Approach 2: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> bool:
    """Given an integer array nums consisting of 2 * n integers, return
    True if nums can be divided into n pairs where each element belongs
    to exactly one pair and the elements present in a pair are equal.
    Otherwise, return False.

    Examples:
        >>> solution_two([3, 2, 3, 2, 2, 2])
        True
        >>> solution_two([1, 2, 3, 4])
        False
        >>> solution_two([3, 3, 3, 5])
        False
    """
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    for v in d.values():
        if v & 1:
            return False
    return True


# ---------------------------------------------------------------------
# Approach 3: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution_three(nums: List[int]) -> bool:
    """Given an integer array nums consisting of 2 * n integers, return
    True if nums can be divided into n pairs where each element belongs
    to exactly one pair and the elements present in a pair are equal.
    Otherwise, return False.

    Examples:
        >>> solution_three([3, 2, 3, 2, 2, 2])
        True
        >>> solution_three([1, 2, 3, 4])
        False
        >>> solution_three([3, 3, 3, 5])
        False
    """
    seen = set()
    for n in nums:
        if n in seen:
            seen.remove(n)
        else:
            seen.add(n)
    return len(seen) == 0


if __name__ == '__main__':
    doctest.testmod()

