import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution(slots: List[List[int]]) -> bool:
    """Given an array of meeting time slots where slots[i] =
    [start-i, end-i], determine if a person could attend all meetings.

    Examples:
        >>> solution([[7, 10], [2, 4]])
        True
        >>> solution([[4, 10], [2, 4]])
        True
        >>> solution([[0, 30], [5, 10], [15, 20]])
        False
    """
    slots.sort()
    for i in range(len(slots) - 1):
        if slots[i][1] > slots[i + 1][0]:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
