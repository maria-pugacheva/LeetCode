import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterate Matrix. Time: O(m * n)                        ***
# ---------------------------------------------------------------------
def solution(grid: List[List[int]]) -> List[int]:
    """Given a binary matrix grid, find the 0-indexed position of the
    row that contains the maximum count of ones, and the number of ones
    in that row. In case there are multiple rows with the same maximum
    count of ones, the row with the smallest row number should be
    selected. Return an array containing the index of the row, and the
    number of ones in it.

    Examples:
        >>> solution([[0, 1], [1, 0]])
        [0, 1]
        >>> solution([[0, 0, 0], [0, 1, 1]])
        [1, 2]
        >>> solution([[0, 0], [1, 1], [0, 0]])
        [1, 2]
    """
    res = [0, 0]
    for i in range(len(grid)):
        cnt = sum(grid[i])
        if cnt > res[1]:
            res[1] = cnt
            res[0] = i
    return res


if __name__ == '__main__':
    doctest.testmod()
