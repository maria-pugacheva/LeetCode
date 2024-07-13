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
    res = [1 for _ in range(n)]
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    right = 1
    for j in range(n - 1, -1, -1):
        res[j] = res[j] * right
        right *= nums[j]
    return res


if __name__ == '__main__':
    doctest.testmod()
