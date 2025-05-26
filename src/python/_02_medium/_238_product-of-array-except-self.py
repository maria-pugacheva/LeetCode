import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: No Extra Space. Time: O(n)                             !!
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[int]:
    """Given an integer array nums, return an array answer such that
    answer[i] is equal to the product of all the elements of nums except
    nums[i].

    Examples:
        >>> solution([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> solution([-1, 1, 0, -3, 3])
        [0, 0, 9, 0, 0]
    """
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for j in range(n - 1, -1, -1):
        res[j] *= suffix
        suffix *= nums[j]
    return res


if __name__ == '__main__':
    doctest.testmod()
