import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ^**
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given an unsorted array of integers nums, return the length of
    the longest consecutive elements sequence.

    Examples:
        >>> solution([])
        0
        >>> solution([1, 2, 0, 1])
        3
        >>> solution([0])
        1
        >>> solution([0, 0])
        1
        >>> solution([100, 4, 200, 1, 3, 2])
        4
        >>> solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        9
    """
    longest = 0
    s = set(nums)
    for n in nums:
        if n - 1 not in s:
            cnt = 0
            while n in s:
                cnt += 1
                n += 1
            longest = max(longest, cnt)
    return longest


if __name__ == '__main__':
    doctest.testmod()
