import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n). Space: O(1)                   !
# ---------------------------------------------------------------------
def solution_one(nums: List[int], val: int) -> int:
    """Remove all instances of val and return the new length of nums.

    Modify the input list in-place with O(1) extra memory.  The order
    of the elements in the list can be changed.  It doesn't matter what
    will be left beyond the new length.

    Preconditions:
        0 <= len(nums) <= 100
        0 <= nums[i] <= 50
        0 <= val <= 100

    Examples:
        >>> solution_one([2], 3)
        1
        >>> solution_one([1, 7], 2)
        2
        >>> solution_one([3, 2, 2, 3], 3)
        2
        >>> solution_one([0, 1, 2, 2, 3, 0, 4, 2], 2)
        5
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


# ---------------------------------------------------------------------
# Approach 2: Two Pointers II. Time: O(n). Space: O(1)              ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int], val: int) -> int:
    """Remove all instances of val and return the new length of nums.

    Modify the input list in-place with O(1) extra memory.  The order
    of the elements in the list can be changed.  It doesn't matter what
    will be left beyond the new length.

    Preconditions:
        0 <= len(nums) <= 100
        0 <= nums[i] <= 50
        0 <= val <= 100

    Examples:
        >>> solution_two([2], 3)
        1
        >>> solution_two([1, 7], 2)
        2
        >>> solution_two([3, 2, 2, 3], 3)
        2
        >>> solution_two([0, 1, 2, 2, 3, 0, 4, 2], 2)
        5
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        if nums[i] == val and nums[j] != val:
            nums[i] = nums[j]
            i += 1
            j -= 1
        elif nums[i] != val:
            i += 1
        else:
            j -= 1
    return i


if __name__ == '__main__':
    doctest.testmod()
