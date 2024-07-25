import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Scan. Time: O(n), n is a number of rows or cols       ***
# ---------------------------------------------------------------------
def solution(mat: List[List[int]]) -> int:
    """Given a square matrix, return the sum of the matrix diagonals.

    Examples:
        >>> solution([[5]])
        5
        >>> solution([[1,2,3],\
                      [4,5,6],\
                      [7,8,9]])
        25
        >>> solution([[1,1,1,1],\
                      [1,1,1,1],\
                      [1,1,1,1],\
                      [1,1,1,1]])
        8
    """
    res, n = 0, len(mat)
    for i in range(n):
        res += mat[i][i] + mat[i][n - 1 - i]
    return res if not n & 1 else res - mat[n // 2][n // 2]


if __name__ == '__main__':
    doctest.testmod()
