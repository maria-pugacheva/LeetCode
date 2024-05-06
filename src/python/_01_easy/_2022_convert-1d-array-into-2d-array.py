import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Slicing. Time: O(n)                                   ***
# ---------------------------------------------------------------------
def solution(nums: List[int], m: int, n: int) -> List[List[int]]:
    """Create a 2-dimensional (2D) array with  m rows and n columns
    using all the elements from nums.

    Examples:
        >>> solution([1, 2], 1, 1)
        []
        >>> solution([1, 2, 3], 1, 3)
        [[1, 2, 3]]
        >>> solution([1, 2, 3, 4], 2, 2)
        [[1, 2], [3, 4]]
    """
    res = []
    if m * n == len(nums):
        for i in range(0, len(nums), n):
            res.append(nums[i:i+n])
    return res


if __name__ == '__main__':
    doctest.testmod()
