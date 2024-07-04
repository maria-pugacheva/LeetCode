import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: DP (In-Place). Time: O(n^2)                           ^**
# ---------------------------------------------------------------------
def solution(tr: List[List[int]]) -> int:
    """Given a triangle array, return the minimum path sum from top to
    bottom. For each step, you may move to an adjacent number of the row
    below. More formally, if you are on index i on the current row, you
    may move to either index i or index i + 1 on the next row.

    Examples:
        >>> solution([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
        11
        >>> solution([[-10]])
        -10
        >>> solution([[-1], [2, 3], [1, -1, -3]])
        -1
    """
    for i in range(1, len(tr)):
        for j in range(len(tr[i])):
            if j == 0:
                tr[i][j] += tr[i-1][j]
            elif j == len(tr[i]) - 1:
                tr[i][j] += tr[i-1][j-1]
            else:
                tr[i][j] += min(tr[i-1][j-1], tr[i-1][j])
    return min(tr[-1])


if __name__ == '__main__':
    doctest.testmod()
