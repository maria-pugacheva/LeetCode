import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n^2)                             ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the maximum amount of water a container can store.

    Preconditions:
        n == len(nums)
        2 <= n <= 10^5
        0 <= nums[i] <= 10^4

    Examples:
        >>> solution_one([1, 1])
        1
        >>> solution_one([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
    """
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            res = max(res, min(nums[i], nums[j]) * (j - i))
    return res


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Return the maximum amount of water a container can store.

    Preconditions:
        n == len(nums)
        2 <= n <= 10^5
        0 <= nums[i] <= 10^4

    Examples:
        >>> solution_two([1, 1])
        1
        >>> solution_two([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
    """
    res = 0
    i, j = 0, len(nums) - 1
    while i < j:
        res = max(res, min(nums[i], nums[j]) * (j - i))
        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1
    return res


if __name__ == '__main__':
    doctest.testmod()
