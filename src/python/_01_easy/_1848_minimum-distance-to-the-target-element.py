import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ^**
# ---------------------------------------------------------------------
def solution_one(nums: List[int], t: int, start: int) -> int:
    """Find an index i such that nums[i] == t and abs(i - start) is
    minimized.  Return abs(i - start).

    Preconditions:
        1 <= len(nums) <= 1000
        1 <= nums[i] <= 10^4
        0 <= start < len(nums)

    Examples:
        >>> solution_one([1], 1, 0)
        0
        >>> solution_one([1, 2, 3, 4, 5], 5, 3)
        1
        >>> solution_one([1, 1, 1, 1, 1, 1], 1, 0)
        0
    """
    i = j = start
    while i < len(nums) or j >= 0:
        if i < len(nums) and nums[i] == t:
            return abs(i - start)
        if j >= 0 and nums[j] == t:
            return abs(j - start)
        i += 1
        j -= 1


# ---------------------------------------------------------------------
# Approach 2: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int], t: int, start: int) -> int:
    """Find an index i such that nums[i] == t and abs(i - start) is
    minimized.  Return abs(i - start).

    Preconditions:
        1 <= len(nums) <= 1000
        1 <= nums[i] <= 10^4
        0 <= start < len(nums)

    Examples:
        >>> solution_two([1], 1, 0)
        0
        >>> solution_two([1, 2, 3, 4, 5], 5, 3)
        1
        >>> solution_two([1, 1, 1, 1, 1, 1], 1, 0)
        0
    """
    res = 10001
    for i in range(len(nums)):
        if nums[i] == t:
            res = min(res, i - start)
    return res


if __name__ == '__main__':
    doctest.testmod()
