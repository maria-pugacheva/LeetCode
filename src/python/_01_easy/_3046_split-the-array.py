import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> bool:
    """Given an integer list nums of even length, return True if it is
    possible to split nums into two lists such that:
        - len(nums1) == len(nums2) == len(nums) / 2;
        - nums1 should contain distinct elements;
        - nums2 should also contain distinct elements.
    Return False otherwise.

    Examples:
        >>> solution_one([1, 1, 1, 1])
        False
        >>> solution_one([1, 1, 1, 2])
        False
        >>> solution_one([1, 2, 1, 3, 2, 4])
        True
    """
    nums.sort()
    for i in range(1, len(nums) - 1):
        if nums[i - 1] == nums[i + 1]:
            return False
    return True


# ---------------------------------------------------------------------
# Approach 2: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> bool:
    """Given an integer list nums of even length, return True if it is
    possible to split nums into two lists such that:
        - len(nums1) == len(nums2) == len(nums) / 2;
        - nums1 should contain distinct elements;
        - nums2 should also contain distinct elements.
    Return False otherwise.

    Examples:
        >>> solution_two([1, 1, 1, 1])
        False
        >>> solution_two([1, 1, 1, 2])
        False
        >>> solution_two([1, 2, 1, 3, 2, 4])
        True
    """
    seen = {}
    for n in nums:
        seen[n] = seen.get(n, 0) + 1
        if seen[n] > 2:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
