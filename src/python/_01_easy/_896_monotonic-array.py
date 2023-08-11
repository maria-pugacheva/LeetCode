import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                   !
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> bool:
    """Return True if the given list is monotonic, or False otherwise.

    Notes:
        A list is monotonic if it is either monotone increasing or
        monotone decreasing.

    Preconditions:
        1 <= len(nums) <= 10^5
        -10^5 <= nums[i] <= 10^5

    Examples:
        >>> solution_one([1, 1, 1])
        True
        >>> solution_one([6, 5, 4, 4])
        True
        >>> solution_one([1, 3, 4, 5, 2])
        False
    """
    inc = dec = True
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            dec = False
        elif nums[i] > nums[i + 1]:
            inc = False
    return inc or dec


# ---------------------------------------------------------------------
# Approach 2: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> bool:
    """Return True if the given list is monotonic, or False otherwise.

    Notes:
        A list is monotonic if it is either monotone increasing or
        monotone decreasing.

    Preconditions:
        1 <= len(nums) <= 10^5
        -10^5 <= nums[i] <= 10^5

    Examples:
        >>> solution_two([1])
        True
        >>> solution_two([6, 5, 4, 4])
        True
        >>> solution_two([1, 3, 4, 5, 2])
        False
    """
    length = len(nums)
    if nums[0] <= nums[length - 1]:
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                return False
    else:
        for i in range(length - 1):
            if nums[i] < nums[i + 1]:
                return False
    return True


if __name__ == '__main__':
    doctest.testmod()
