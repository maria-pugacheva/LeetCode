import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: DP (In-Place). Time: O(n*m)                           ***
# ---------------------------------------------------------------------
# Note: Can also be solved with extra space if grid can't be modified
# ---------------------------------------------------------------------
def solution(grid: List[List[int]]) -> int:
    """Given a m x n grid filled with non-negative numbers, find a path
    from top left to bottom right, which minimizes the sum of all
    numbers along its path. You can only move either down or right at
    any point in time.

    Examples:
        >>> solution([[2]])
        2
        >>> solution([[1, 2, 3], [4, 5, 6]])
        12
        >>> solution([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        7
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j > 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0 and i > 0:
                grid[i][j] += grid[i-1][j]
            elif i > 0 and j > 0:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


if __name__ == '__main__':
    doctest.testmod()
