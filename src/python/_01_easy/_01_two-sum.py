import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n^2). Space: O(1)                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], t: int) -> List[int]:
    """Return the indices of the two numbers in nums that sum up to t.

    Notes:
        Each input would have exactly one solution.
        The same element can't be used twice.
        The answer can be returned in any order.

    Preconditions:
        2 <= len(nums) <= 10^5
        -10^9 <= nums[i] <= 10^9
        -10^9 <= t <= 10^9

    Examples:
        >>> solution_one([3, 2], 5)
        [0, 1]
        >>> solution_one([3, 3], 6)
        [0, 1]
        >>> solution_one([3, 2, 4], 6)
        [1, 2]
        >>> solution_one([20, 1, -120, 1, 30, 17], -100)
        [0, 2]
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == t:
                return [i, j]
    return [-1, -1]


# ---------------------------------------------------------------------
# Approach 2: Sorting + Two Pointers. Time: O(n log n)              ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int], t: int) -> List[int]:
    """Return the indices of the two numbers in nums that sum up to t.

    Notes:
        Each input would have exactly one solution.
        The same element can't be used twice.
        The answer can be returned in any order.

    Preconditions:
        2 <= len(nums) <= 10^5
        -10^9 <= nums[i] <= 10^9
        -10^9 <= t <= 10^9

    Examples:
        >>> solution_two([3, 2], 5)
        [1, 0]
        >>> solution_two([3, 3], 6)
        [0, 1]
        >>> solution_two([3, 2, 4], 6)
        [1, 2]
        >>> solution_two([20, 1, -120, 1, 30, 17], -100)
        [2, 0]
    """
    nums_sorted = sorted(nums)
    i, j = 0, len(nums_sorted) - 1
    while i < j:
        x, y = nums_sorted[i], nums_sorted[j]
        if x + y > t:
            j -= 1
        elif x + y < t:
            i += 1
        else:
            if x == y:
                return [nums.index(x), nums.index(y, nums.index(x) + 1)]
            return [nums.index(x), nums.index(y)]
    return [-1, -1]


# ---------------------------------------------------------------------
# Approach 3: Hash Table. Time: O(n). Space: O(n)                   ***
# ---------------------------------------------------------------------
def solution_three(nums: List[int], t: int) -> List[int]:
    """Return the indices of the two numbers in nums that sum up to t.

    Notes:
        Each input would have exactly one solution.
        The same element can't be used twice.
        The answer can be returned in any order.

    Preconditions:
        2 <= len(nums) <= 10^5
        -10^9 <= nums[i] <= 10^9
        -10^9 <= t <= 10^9

    Examples:
        >>> solution_three([3, 2], 5)
        [0, 1]
        >>> solution_three([3, 3], 6)
        [0, 1]
        >>> solution_three([3, 2, 4], 6)
        [1, 2]
        >>> solution_three([20, 1, -120, 1, 30, 17], -100)
        [0, 2]
    """
    d = {}
    for i in range(len(nums)):
        n = nums[i]
        c = t - n
        if c in d:
            return [d[c], i]
        d[n] = i
    return [-1, -1]


if __name__ == '__main__':
    doctest.testmod()
