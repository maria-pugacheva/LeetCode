import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n). Space: O(n)                            !
# ---------------------------------------------------------------------
# We only attempt to build sequences from numbers that are not already
# part of a longer sequence. This is accomplished by first ensuring that
# the number that would immediately precede the current number in a
# sequence is not present, as that number would necessarily be part of a
# longer sequence.
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given an unsorted array of integers nums, return the length of
    the longest consecutive elements sequence.

    Examples:
        >>> solution([])
        0
        >>> solution([1, 2, 0, 1])
        3
        >>> solution([4, 3, 2, 1])
        4
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
            cnt = 1
            while n + 1 in s:
                cnt += 1
                n += 1
            longest = max(longest, cnt)
    return longest


if __name__ == '__main__':
    doctest.testmod()
