import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting Start and End Times. T: O(n log n). S: O(n)     !
# ---------------------------------------------------------------------
def solution(intervals: List[List[int]]) -> int:
    """Given an array of meeting time intervals intervals where
    intervals[i] = [start-i, end-i], return the minimum number of
    conference rooms required.

    Examples:
        >>> solution([[7, 10], [2, 4]])
        1
        >>> solution([[0, 4], [5, 10], [6, 7]])
        2
        >>> solution([[0, 30], [5, 10], [6, 7]])
        3
        >>> solution([[0, 30], [5, 10], [9, 20]])
        3
        >>> solution([[0, 30], [5, 10], [10, 20]])
        2
        >>> solution([[0, 30], [5, 10], [15, 20]])
        2
        >>> solution([[0, 9], [2, 3], [10, 11], [10, 11], [12, 13]])
        2
    """
    starts = sorted([slot[0] for slot in intervals])
    ends = sorted([slot[1] for slot in intervals])
    usedRooms = 0
    i, j = 0, 0
    while i < len(starts):
        if starts[i] >= ends[j]:
            usedRooms -= 1  # Free up a room as the meeting's just ended
            j += 1
        usedRooms += 1
        i += 1
    return usedRooms


if __name__ == '__main__':
    doctest.testmod()
