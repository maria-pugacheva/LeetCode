import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> bool:
    """Return True if there exist two sub-arrays of length 2 with equal
    sum, and False otherwise.

    Examples:
        >>> solution([2, 2])
        False
        >>> solution([4, 2, 4])
        True
        >>> solution([1, 2, 3, 4, 5])
        False
        >>> solution([0, 0, 0])
        True
    """
    sums = set()
    for i in range(len(nums) - 1):
        s = nums[i] + nums[i+1]
        if s in sums:
            return True
        sums.add(s)
    return False


if __name__ == '__main__':
    doctest.testmod()
