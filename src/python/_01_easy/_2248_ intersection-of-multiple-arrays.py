import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Counter                                               ***
# ---------------------------------------------------------------------
def solution(nums: List[List[int]]) -> List[int]:
    """Given a 2D integer array nums where nums[i] is a non-empty array
    of distinct positive integers, find all integers that are present
    in each array of nums sorted in ascending order.

    Examples:
        >>> solution([[1, 2, 3], [4, 5, 6]])
        []
        >>> solution([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]])
        [3, 4]
    """
    cnt = [0] * 1001
    for arr in nums:
        for n in arr:
            cnt[n] += 1
    res = []
    for i in range(1001):
        if cnt[i] == len(nums):
            res.append(i)
    return res


if __name__ == '__main__':
    doctest.testmod()
