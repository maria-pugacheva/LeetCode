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


# ---------------------------------------------------------------------
# Approach 2: Dictionary. Time: O(n). Space: O(n)                   ***
# ---------------------------------------------------------------------
# 1. Create a dictionary to store the elements of the given list and
#    their corresponding indices.
# 2. Iterate through the elements of the list and check if their
#    complements exist in the dictionary.
# 3. Once the complement of a number is found, return their indices.
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
        [0, 1]
        >>> solution_two([3, 2, 4], 6)
        [1, 2]
        >>> solution_two([20, 1, -120, 1, 30, 17], -100)
        [0, 2]
    """
    d = {}
    for i in range(len(nums)):
        n = nums[i]
        c = t - n
        if c in d:
            return [d[c], i]
        d[n] = i


# ---------------------------------------------------------------------
# Approach 3: Sorting + Two Pointers. Time: O(n log n)              ***
# ---------------------------------------------------------------------
def solution_three(nums: List[int], t: int) -> List[int]:
    nums_sorted = sorted(nums)
    i = 0
    j = len(nums_sorted) - 1
    while i < j:
        x = nums_sorted[i]
        y = nums_sorted[j]
        if x + y > t:
            j -= 1
        elif x + y < t:
            i += 1
        else:
            return [nums.index(x), nums.index(y)]


if __name__ == '__main__':
    doctest.testmod()
