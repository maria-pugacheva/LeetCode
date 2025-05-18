import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n)                           !
# ---------------------------------------------------------------------
def solution(nums: List[int], t: int) -> List[int]:
    """Given an array of integers nums sorted in non-decreasing order,
    find the starting and ending position of a given target value.

    Examples:
        >>> solution([], 0)
        [-1, -1]
        >>> solution([2, 2], 2)
        [0, 1]
        >>> solution([1, 2], 2)
        [1, 1]
        >>> solution([1, 2, 2], 2)
        [1, 2]
        >>> solution([2, 2, 3], 2)
        [0, 1]
        >>> solution([3, 3, 4], 4)
        [2, 2]
        >>> solution([5, 7, 7, 8, 8, 10], 6)
        [-1, -1]
        >>> solution([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
    """
    n = len(nums)

    def findFirstOrLastPosition(isFirst: bool) -> int:
        i, j = 0, n - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == t:
                if isFirst:
                    if m == 0 or nums[m - 1] != t:
                        return m
                    j = m - 1
                else:
                    if m == n - 1 or nums[m + 1] != t:
                        return m
                    i = m + 1
            elif nums[m] < t:
                i = m + 1
            else:
                j = m - 1
        return -1

    first = findFirstOrLastPosition(True)
    if first == -1:
        return [-1, -1]
    last = findFirstOrLastPosition(False)

    return [first, last]


if __name__ == '__main__':
    doctest.testmod()
