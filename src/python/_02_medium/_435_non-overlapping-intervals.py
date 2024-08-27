import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution(intervals: List[List[int]]) -> int:
    """Given an array of intervals intervals, return the minimum number
    of intervals you need to remove to make the rest of the intervals
    non-overlapping.

    Examples:
        >>> solution([[1, 2], [2, 3]])
        0
        >>> solution([[1, 2], [1, 2], [1, 2]])
        2
        >>> solution([[1, 2], [2, 3], [3, 4], [1, 3]])
        1
        >>> solution([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]])
        2
    """
    intervals.sort(key=lambda x: x[1])

    cnt, i = 0, 0
    for j in range(1, len(intervals)):
        if intervals[j][0] < intervals[i][1]:
            cnt += 1
        else:
            i = j
    return cnt


if __name__ == '__main__':
    doctest.testmod()
