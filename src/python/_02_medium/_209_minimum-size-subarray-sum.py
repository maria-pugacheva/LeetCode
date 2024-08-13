import doctest
from bisect import bisect_left
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sliding Window. Time: O(n)                            ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], t: int) -> int:
    """Given an array of positive integers nums and a positive integer
    t, return the minimal length of a sub-array whose sum is greater
    than or equal to t. If there is no such sub-array, return 0 instead.

    Examples:
        >>> solution_one([1, 1, 1, 1, 1, 1, 1, 1], 11)
        0
        >>> solution_one([1, 4, 4], 4)
        1
        >>> solution_one([2, 3, 1, 2, 4, 3], 7)
        2
    """
    length = len(nums)
    res, curr, i = length + 1, 0, 0
    for j in range(length):
        curr += nums[j]
        while curr >= t:
            res = min(res, j - i + 1)
            curr -= nums[i]
            i += 1
    return res if res != length + 1 else 0


# ---------------------------------------------------------------------
# Approach 2: Binary Search. Time: O(n log n)                         !
# ---------------------------------------------------------------------
def solution_two(nums: List[int], t: int) -> int:
    """Given an array of positive integers nums and a positive integer
    t, return the minimal length of a sub-array whose sum is greater
    than or equal to t. If there is no such sub-array, return 0 instead.

    Examples:
        >>> solution_two([1, 1, 1, 1, 1, 1, 1, 1], 11)
        0
        >>> solution_two([1, 4, 4], 4)
        1
        >>> solution_two([2, 3, 1, 2, 4, 3], 7)
        2
    """
    length = len(nums)
    res = length + 1
    arr = [0]
    for n in nums:
        arr.append(arr[-1] + n)
    for i in range(1, length + 1):
        x = t + arr[i - 1]
        bound = bisect_left(arr, x)

        if bound != length:
            res = min(res, bound - (i - 1))

    return res if res != length + 1 else 0


if __name__ == '__main__':
    doctest.testmod()
