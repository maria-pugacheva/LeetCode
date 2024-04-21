import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """In one operation, you can choose an element in nums and increment
    it by 1. Return the minimum number of operations needed to make nums
    strictly increasing.

    Examples:
        >>> solution([7])
        0
        >>> solution([1, 1, 1])
        3
        >>> solution([1, 5, 2, 4, 1])
        14
    """
    res = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            t, nums[i] = nums[i], nums[i-1] + 1
            res += nums[i] - t
    return res


if __name__ == '__main__':
    doctest.testmod()
