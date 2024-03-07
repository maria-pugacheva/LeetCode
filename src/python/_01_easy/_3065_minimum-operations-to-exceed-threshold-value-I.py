import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution(nums: List[int], k:int) -> int:
    """Return the minimum number of operations needed so that all
    elements of the array are greater than or equal to k.

    Examples:
        >>> solution([2, 11, 10, 1, 3], 10)
        3
        >>> solution([1, 1, 2, 4, 9], 1)
        0
        >>> solution([1, 1, 2, 4, 9], 9)
        4
    """
    cnt = 0
    for n in nums:
        if n < k:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
