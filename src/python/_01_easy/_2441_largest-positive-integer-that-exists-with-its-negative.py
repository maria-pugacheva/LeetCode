import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Given an integer array nums that does not contain any zeros,
    find the largest positive integer k such that -k also exists in the
    array. Return the positive integer k. If there is no such integer,
    return -1.

    Examples:
        >>> solution_one([-1, 2, -3, 3])
        3
        >>> solution_one([-1, 10, 6, 7, -7, 1])
        7
        >>> solution_one([-10, 8, 6, 7, -2, -3])
        -1
    """
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] > 0 or nums[j] < 0:
            break
        elif abs(nums[i]) < nums[j]:
            j -= 1
        elif abs(nums[i]) > nums[j]:
            i += 1
        else:
            return nums[j]
    return -1


# ---------------------------------------------------------------------
# Approach 2: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Given an integer array nums that does not contain any zeros,
    find the largest positive integer k such that -k also exists in the
    array. Return the positive integer k. If there is no such integer,
    return -1.

    Examples:
        >>> solution_two([-1, 2, -3, 3])
        3
        >>> solution_two([-1, 10, 6, 7, -7, 1])
        7
        >>> solution_two([-10, 8, 6, 7, -2, -3])
        -1
    """
    res = -1
    seen = set()
    for n in nums:
        if n in seen:
            res = max(res, abs(n))
        else:
            seen.add(-n)
    return res


if __name__ == '__main__':
    doctest.testmod()
