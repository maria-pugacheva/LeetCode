import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Return the absolute difference between the element sum and digit
    sum of nums.

    Examples:
        >>> solution([1, 15, 6, 3])
        9
        >>> solution([1, 2, 3, 4])
        0
        >>> solution([7, 3, 11])
        9
    """
    esum = dsum = 0
    for n in nums:
        esum += n
        while n:
            dsum += n % 10
            n = n // 10
    return abs(esum - dsum)


if __name__ == '__main__':
    doctest.testmod()
