import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Count Even Numbers. Time: O(n)                        ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> bool:
    """Given an array of positive integers nums, check if it is possible
    to select two or more elements in the array such that the bitwise OR
    of the selected elements has at least one trailing zero in its
    binary representation.

    Examples:
        >>> solution([1, 2, 3, 4, 5])
        True
        >>> solution([2, 4, 6, 8, 16])
        True
        >>> solution([1, 3, 5, 7, 9])
        False
    """
    cnt = 0
    for n in nums:
        if not n & 1:
            cnt += 1
        if cnt >= 2:
            return True
    return False


if __name__ == '__main__':
    doctest.testmod()
