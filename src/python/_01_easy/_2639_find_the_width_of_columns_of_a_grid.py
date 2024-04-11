import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterate Matrix                                        ***
# ---------------------------------------------------------------------
def solution(grid: List[List[int]]) -> List[int]:
    """Return an integer array res of size n where res[i] is the width
    of the ith column in grid.

    Examples:
        >>> solution([[1], [22], [333]])
        [3]
        >>> solution([[-15, 1, 3], [15, 7, 12]])
        [3, 1, 2]
        >>> solution([[0, 1, -7], [2, 15, 7], [14, 4, 3]])
        [2, 2, 2]
    """
    res = []
    for i in range(len(grid[0])):
        t = 0
        for j in range(len(grid)):
            t = max(t, len(str(grid[j][i])))
        res.append(t)
    return res


if __name__ == '__main__':
    doctest.testmod()
