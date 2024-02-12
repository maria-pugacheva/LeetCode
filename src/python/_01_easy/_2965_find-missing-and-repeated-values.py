import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution_one(grid: List[List[int]]) -> List[int]:
    """Return a 0-indexed integer array arr of size 2 where arr[0]
    equals to an integer that appears twice in grid, and arr[1] equals
    to an integer that is missing in grid.

    Examples:
        >>> solution_one([[1, 3], [2, 2]])
        [2, 4]
        >>> solution_one([[9, 1, 7], [8, 9, 2], [3, 4, 6]])
        [9, 5]
    """
    arr = [0, 0]
    s = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            n = grid[i][j]
            if n in s:
                arr[0] = n
            else:
                s.add(n)
    for k in range(1, len(grid)**2 + 1):
        if k not in s:
            arr[1] = k
    return arr


if __name__ == '__main__':
    doctest.testmod()
