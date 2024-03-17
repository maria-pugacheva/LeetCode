import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sort. Time: O(n log n)                                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], n: int) -> int:
    """If n is found in nums, multiply it by two. Repeat this step until
    the new number is not in nums. Return the final value of n.

    Examples:
        >>> solution_one([2, 7, 9], 4)
        4
        >>> solution_one([5, 3, 6, 1, 12], 3)
        24
        >>> solution_one([1, 4, 2, 5], 1)
        8
    """
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == n:
            n *= 2
        else:
            continue
    return n


# ---------------------------------------------------------------------
# Approach 2: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int], n: int) -> int:
    """If n is found in nums, multiply it by two. Repeat this step until
    the new number is not in nums. Return the final value of n.

    Examples:
        >>> solution_two([2, 7, 9], 4)
        4
        >>> solution_two([5, 3, 6, 1, 12], 3)
        24
        >>> solution_two([1, 4, 2, 5], 1)
        8
    """
    seen = set(nums)
    while n in seen:
        n *= 2
    return n


if __name__ == '__main__':
    doctest.testmod()
