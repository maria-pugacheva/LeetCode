import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(n log n)                       ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], t: int) -> List[int]:
    """Given a 1-indexed array of integers nums that is already sorted
    in non-decreasing order, find two numbers such that they add up to
    t. Return the indices of the two numbers.

    Examples:
        >>> solution_one([-1, 0], -1)
        [1, 2]
        >>> solution_one([2, 3, 4], 6)
        [1, 3]
        >>> solution_one([2, 7, 11, 15], 9)
        [1, 2]
    """
    for i in range(len(nums)):
        c = t - nums[i]
        left, right = i + 1, len(nums) - 1
        while left <= right:
            ind = (left + right) // 2
            if nums[ind] == c:
                return [i + 1, ind + 1]
            elif nums[ind] < c:
                left += 1
            else:
                right -= 1
    return [-1, -1]


# ---------------------------------------------------------------------
# Approach 2: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int], t: int) -> List[int]:
    """Given a 1-indexed array of integers nums that is already sorted
    in non-decreasing order, find two numbers such that they add up to
    t. Return the indices of the two numbers.

    Examples:
        >>> solution_two([-1, 0], -1)
        [1, 2]
        >>> solution_two([2, 3, 4], 6)
        [1, 3]
        >>> solution_two([2, 7, 11, 15], 9)
        [1, 2]
    """
    i, j = 0, len(nums) - 1
    while i < j:
        val = nums[i] + nums[j]
        if val == t:
            return [i + 1, j + 1]
        elif val < t:
            i += 1
        else:
            j -= 1
    return [-1, -1]


if __name__ == '__main__':
    doctest.testmod()
