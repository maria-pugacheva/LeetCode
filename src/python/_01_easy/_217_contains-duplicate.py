import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n). Space: O(n).               ***
# ---------------------------------------------------------------------
# 1. Modify the original list by sorting it (if it's allowed).
# 2. Iterate over the sorted list to check if there are any two
#    consecutive duplicate elements.  If so, return True.
# 3. Return False at the end.
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
# Approach 2: Set. Time: O(n). Space: O(n).                         ***
# ---------------------------------------------------------------------
# 1. Create an empty set to store the elements of the input list.
# 2. Iterate through the elements of the list and check if an element
#    exists in the set.  If so, return True; otherwise, add the element
#    to the set.
# 3. Return False at the end.
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
