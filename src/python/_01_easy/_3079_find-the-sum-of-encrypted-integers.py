import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Math.                                                 !**
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given an integer array nums containing positive integers, we
    define a function encrypt such that encrypt(x) replaces every digit
    in x with the largest digit in x (e.g, encrypt(573) = 777). Return
    the sum of encrypted elements in nums.

    Examples:
        >>> solution([1, 2, 3])
        6
        >>> solution([10, 21, 31])
        66
        >>> solution([12, 12, 85, 1000, 597])
        2242
    """
    res = 0
    for n in nums:
        x = m = 0
        while n:
            x = max(x, n % 10)
            n //= 10
            m = (m * 10) + 1
        res += x * m
    return res


if __name__ == '__main__':
    doctest.testmod()
