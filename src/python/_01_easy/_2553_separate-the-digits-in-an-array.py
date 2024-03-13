import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: String Conversion                                     ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[int]:
    """Given an array of positive integers nums, return an array res
    that consists of the digits of each integer in nums after separating
    them in the same order they appear in nums.

    Examples:
        >>> solution([7, 1, 3, 9])
        [7, 1, 3, 9]
        >>> solution([13, 25, 83, 77])
        [1, 3, 2, 5, 8, 3, 7, 7]
    """
    res = []
    for n in nums:
        s = str(n)
        for d in s:
            res.append(int(d))
    return res


if __name__ == '__main__':
    doctest.testmod()
