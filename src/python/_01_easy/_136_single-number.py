import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Bit Manipulation. Time: O(n). Space: O(1)             ***
# ---------------------------------------------------------------------
# Concept: Use the XOR bitwise operator (0 ^ n = n; n ^ n = 0).
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the only integer in nums that doesn't occur twice.

    Preconditions:
        nums is a non-empty list of integers

    Examples:
        >>> solution_one([2, 2, 1])
        1
        >>> solution_one([4, 1, 2, 1, 2])
        4
    """
    a = 0
    for n in nums:
        a ^= n
    return a


# ---------------------------------------------------------------------
# Approach 2: Mathematical. Time: O(n). Space: O(n)                 ***
# ---------------------------------------------------------------------
# Concept: 2 ∗ (a + b + c) − (a + a + b + b + c) = c
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Return the only integer in nums that doesn't occur twice.

    Preconditions:
        nums is a non-empty list of integers

    Examples:
        >>> solution_two([2, 2, 1])
        1
        >>> solution_two([4, 1, 2, 1, 2])
        4
    """
    return 2 * sum(set(nums)) - sum(nums)


# ---------------------------------------------------------------------
# Approach 1: Frequency Counter. Time: O(n). Space: O(n)            ***
# ---------------------------------------------------------------------
# 1. Use a dictionary to store the frequency of each element present in
#    the given list.
# 2. Iterate through the items of the dictionary and return the element
#    that appeared only once.
# ---------------------------------------------------------------------
def solution_three(nums: List[int]) -> int:
    """Return the only integer in nums that doesn't occur twice.

    Preconditions:
        nums is a non-empty list of integers

    Examples:
        >>> solution_three([2, 2, 1])
        1
        >>> solution_three([4, 1, 2, 1, 2])
        4
    """
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    for k, v in d.items():
        if v == 1:
            return k
    return -1


if __name__ == '__main__':
    doctest.testmod()
