import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(((m log m) * n) + (m * n))           ***
# ---------------------------------------------------------------------
def solution(grid: List[List[int]]) -> int:
    """Given an m x n matrix grid consisting of positive integers,
    perform the following operation until grid becomes empty. Delete the
    element with the greatest value from each row and add the maximum of
    deleted elements to a variable. Return the resulting value.

    Examples:
        >>> solution([[10]])
        10
        >>> solution([[1, 2, 4], [3, 3, 1]])
        8
        >>> solution([[4, 1, 2, 15, 30, 7], [3, 1, 12, 7, 22, 3]])
        60
    """
    res = 0
    for row in grid:
        row.sort()
    for j in range(len(grid[0]) - 1, -1, -1):
        t = 0
        for i in range(len(grid)):
            t = max(t, grid[i][j])
        res += t
    return res


if __name__ == '__main__':
    doctest.testmod()
