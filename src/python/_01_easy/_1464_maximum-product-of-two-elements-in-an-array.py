import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n). Space: O(n).               ***
# ---------------------------------------------------------------------
# 1. Modify the original list by sorting it (if it's allowed).
# 2. Retrieve the last two integers of the sorted list, decrement their
#    values by 1, calculate their product, and return it.
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the maximum value of (nums[i]-1) * (nums[j]-1).

    Preconditions:
        2 <= len(nums) <= 500
        1 <= nums[i] <= 10^3

    Examples:
        >>> solution_one([3, 7])
        12
        >>> solution_one([3, 4, 5, 2])
        12
        >>> solution_one([1, 5, 4, 5])
        16
    """
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1)


# ---------------------------------------------------------------------
# Approach 2: Two Largest Values. Time: O(n). Space: O(1)           ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Return the maximum value of (nums[i]-1) * (nums[j]-1).

    Preconditions:
        2 <= len(nums) <= 500
        1 <= nums[i] <= 10^3

    Examples:
        >>> solution_two([3, 7])
        12
        >>> solution_two([3, 4, 5, 2])
        12
        >>> solution_two([1, 5, 4, 5])
        16
    """
    mx_one = mx_two = -1
    for n in nums:
        if n > mx_one:
            mx_one, mx_two = n, mx_one
        elif n > mx_two:
            mx_two = n
    return (mx_one - 1) * (mx_two - 1)


if __name__ == '__main__':
    doctest.testmod()
