import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Convert to String. Time: O(n * log m), m == max(nums) ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Given an array of integers nums, count the number of integers
    that contain an even number of digits.

    Preconditions:
        1 <= len(nums) <= 500
        1 <= nums[i] <= 10^5

    Examples:
        >>> solution_one([333])
        0
        >>> solution_one([12, 345, 2, 6, 7896])
        2
        >>> solution_one([555, 901, 482, 1771])
        1
    """
    cnt = 0
    for x in nums:
        if len(str(x)) % 2 == 0:
            cnt += 1
    return cnt


# ---------------------------------------------------------------------
# Approach 2: Count Digits. Time: O(n * log m), m == max(nums)      ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Given an array of integers nums, count the number of integers
    that contain an even number of digits.

    Preconditions:
        1 <= len(nums) <= 500
        1 <= nums[i] <= 10^5

    Examples:
        >>> solution_two([333])
        0
        >>> solution_two([12, 345, 2, 6, 7896])
        2
        >>> solution_two([555, 901, 482, 1771])
        1
    """
    cnt = 0
    for y in nums:
        cnt_digits = 0
        while y > 0:
            y //= 10
            cnt_digits += 1
        if cnt_digits % 2 == 0:
            cnt += 1
    return cnt


# ---------------------------------------------------------------------
# Approach 3: Constraint Analysis. Time: O(n)                       ^**
# ---------------------------------------------------------------------
def solution_three(nums: List[int]) -> int:
    """Given an array of integers nums, count the number of integers
    that contain an even number of digits.

    Preconditions:
        1 <= len(nums) <= 500
        1 <= nums[i] <= 10^5

    Examples:
        >>> solution_three([333])
        0
        >>> solution_three([12, 345, 2, 6, 7896])
        2
        >>> solution_three([555, 901, 482, 1771])
        1
    """
    cnt = 0
    for n in nums:
        if 9 < n < 100 or 999 < n < 10_000 or n == 100_000:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
