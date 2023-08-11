import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Modulo. Time: O(n)                                    ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the smallest index i of nums such that i % 10 == nums[i].

    Preconditions:
        1 <= len(nums) <= 100
        0 <= nums[i] <= 9

    Examples:
        >>> solution_one([0, 1, 2])
        0
        >>> solution_one([4, 3, 2, 1])
        2
        >>> solution_one([1, 2, 3, 4, 5, 6, 7])
        -1
        >>> solution_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11])
        10
    """
    for i in range(len(nums)):
        if nums[i] == i % 10:
            return i
    return -1


if __name__ == '__main__':
    doctest.testmod()
