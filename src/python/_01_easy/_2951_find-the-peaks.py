import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Loop. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[int]:
    """Return an array that consists of indices of peaks in the given
    array in any order.

    Examples:
        >>> solution([2, 4, 4])
        []
        >>> solution([1, 4, 3, 8, 5])
        [1, 3]
    """
    res = []
    for i in range(1, len(nums) - 1, 1):
        if nums[i-1] < nums[i] > nums[i+1]:
            res.append(i)
    return res


if __name__ == '__main__':
    doctest.testmod()
