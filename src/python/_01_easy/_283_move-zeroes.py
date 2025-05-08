import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n). Space: O(1)                   !
# ---------------------------------------------------------------------
# Note: Better when there are many zeros. Avoids swaps, which are more
#       expensive than assignment.
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> List[int]:
    """Given an integer array nums, move all 0's to the end of it while
    maintaining the relative order of the non-zero elements. Modify the
    input list in-place with O(1) extra memory.

    Examples:
        >>> solution_one([0])
        [0]
        >>> solution_one([1])
        [1]
        >>> solution_one([1, 0])
        [1, 0]
        >>> solution_one([0, 1, 1, 1, 1])
        [1, 1, 1, 1, 0]
        >>> solution_one([0, 1, 0, 3, 12])
        [1, 3, 12, 0, 0]
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    for k in range(i, len(nums)):
        nums[k] = 0
    return nums


# ---------------------------------------------------------------------
# Approach 2: Two Pointers. Time: O(n). Space: O(1)                   !
# ---------------------------------------------------------------------
# Note: Better when the list has few or no zeros
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> List[int]:
    """Given an integer array nums, move all 0's to the end of it while
    maintaining the relative order of the non-zero elements. Modify the
    input list in-place with O(1) extra memory.

    Examples:
        >>> solution_two([0])
        [0]
        >>> solution_two([1])
        [1]
        >>> solution_two([1, 0])
        [1, 0]
        >>> solution_two([0, 1, 1, 1, 1])
        [1, 1, 1, 1, 0]
        >>> solution_two([0, 1, 0, 3, 12])
        [1, 3, 12, 0, 0]
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


if __name__ == '__main__':
    doctest.testmod()
