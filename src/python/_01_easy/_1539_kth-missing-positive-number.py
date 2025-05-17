import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n). Space: O(1)                    !
# ---------------------------------------------------------------------
# Note: For each element num in the array, if it is less than or equal
#       to k, it means we've encountered an actual element of the
#       sequence, so the k-th missing positive integer is pushed further
#       by one. If num is greater than k, we stop because there’s no
#       need to continue iterating once we’ve passed the range where the
#       k-th missing integer could exist.
# ---------------------------------------------------------------------
def solution_one(nums: List[int], k: int) -> int:
    """Given an array nums of positive integers sorted in a strictly
    increasing order, and an integer k. Return the k-th positive integer
    that is missing from this array.

    Examples:
        >>> solution_one([1], 1)
        2
        >>> solution_one([3], 1)
        1
        >>> solution_one([1, 2, 3, 4], 2)
        6
        >>> solution_one([2, 3, 4, 7, 11], 5)
        9
    """
    for n in nums:
        if n <= k:
            k += 1
        else:
            break
    return k


# ---------------------------------------------------------------------
# Approach 2: Binary Search. Time: O(log n). Space: O(1)              !
# ---------------------------------------------------------------------
def solution_two(nums: List[int], k: int) -> int:
    """Given an array nums of positive integers sorted in a strictly
    increasing order, and an integer k. Return the k-th positive integer
    that is missing from this array.

    Examples:
        >>> solution_two([1], 1)
        2
        >>> solution_two([3], 1)
        1
        >>> solution_two([1, 2, 3, 4], 2)
        6
        >>> solution_two([2, 3, 4, 7, 11], 5)
        9
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] - 1 - mid < k:
            i += 1
        else:
            j -= 1
    return i + k


if __name__ == '__main__':
    doctest.testmod()
