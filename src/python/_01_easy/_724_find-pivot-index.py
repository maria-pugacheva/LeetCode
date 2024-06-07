import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Right Sum. Time: O(n)                                 !**
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Calculate the pivot index of nums. The pivot index is the index
    where the sum of all the numbers strictly to the left of the index
    is equal to the sum of all the numbers strictly to the right of the
    index.

    Examples:
        >>> solution([2, 1, -1])
        0
        >>> solution([1, 7, 3, 6, 5, 6])
        3
        >>> solution([1, 2, 3])
        -1
    """
    right = sum(nums)
    left = 0
    for i in range(len(nums)):
        if left == right - left - nums[i]:
            return i
        left += nums[i]
    return -1


if __name__ == '__main__':
    doctest.testmod()
