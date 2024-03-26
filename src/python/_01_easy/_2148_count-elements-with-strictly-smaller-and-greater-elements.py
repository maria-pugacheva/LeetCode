import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Given an integer array nums, return the number of elements that
    have both a strictly smaller and a strictly greater element appear
    in nums.

    Examples:
        >>> solution_one([1, 1, 1, 1])
        0
        >>> solution_one([-3, 3, 3, 90])
        2
        >>> solution_one([11, 7, 2, 15])
        2
    """
    nums.sort()
    cnt = 0
    for i in range(1, len(nums) - 1):
        if nums[i] != nums[0] and nums[i] != nums[-1]:
            cnt += 1
    return cnt


# ---------------------------------------------------------------------
# Approach 2: Three Passes. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given an integer array nums, return the number of elements that
    have both a strictly smaller and a strictly greater element appear
    in nums.

    Examples:
        >>> solution([1, 1, 1, 1])
        0
        >>> solution([-3, 3, 3, 90])
        2
        >>> solution([11, 7, 2, 15])
        2
    """
    mx = max(nums)
    mn = min(nums)
    cnt = 0
    for n in nums:
        if n != mx and n != mn:
            cnt += 1
    return cnt


# ---------------------------------------------------------------------
# Approach 3: One Pass. Time: O(n)                                  ^**
# ---------------------------------------------------------------------
def solution_three(nums: List[int]) -> int:
    """Given an integer array nums, return the number of elements that
    have both a strictly smaller and a strictly greater element appear
    in nums.

    Examples:
        >>> solution_three([1, 1, 1, 1])
        0
        >>> solution_three([-3, 3, 3, 90])
        2
        >>> solution_three([11, 7, 2, 15])
        2
    """
    mx = float('-inf')
    mn = float('inf')
    cnt = [0, 0]
    for n in nums:
        if n > mx:
            mx = n
            cnt[0] = 1
        elif n == mx:
            cnt[0] += 1
        if n < mn:
            mn = n
            cnt[1] = 1
        elif n == mn:
            cnt[1] += 1
    return len(nums) - sum(cnt) if mx != mn else 0


if __name__ == '__main__':
    doctest.testmod()
