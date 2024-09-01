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
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] *= postfix
        postfix *= nums[j]
    return res


if __name__ == '__main__':
    doctest.testmod()
