import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n). Space: O(n)                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> bool:
    """Return True if nums contains any duplicates.

    Examples:
        >>> solution_one([1])
        False
        >>> solution_one([1, 2, 3, 1])
        True
        >>> solution_one([1, 2, 3, 4, 5, 6])
        False
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# ---------------------------------------------------------------------
# Approach 2: Set. Time: O(n). Space: O(n)                          ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> bool:
    """Return True if nums contains any duplicates.

    Examples:
        >>> solution_two([1])
        False
        >>> solution_two([1, 2, 3, 1])
        True
        >>> solution_two([1, 2, 3, 4, 5, 6])
        False
    """
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == '__main__':
    doctest.testmod()
