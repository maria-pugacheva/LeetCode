import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(m * n * (m + n))                 ***
# ---------------------------------------------------------------------
def solution_one(mat: List[List[int]]) -> int:
    """Given an m x n binary matrix mat, return the number of special
    positions in mat. A position (i, j) is called special if
    mat[i][j] == 1 and all other elements in row i and column j are 0.

    Examples:
        >>> solution_one([[1,0,0], [0,0,1], [1,0,0]])
        1
        >>> solution_one([[1,0,0], [0,1,0], [0,0,1]])
        3
    """
    cnt, m, n = 0, len(mat), len(mat[0])

    def is_special(r: int, k: int) -> bool:
        for a in range(r+1, m):
            if mat[a][k] != 0:
                return False
        for b in range(r-1, -1, -1):
            if mat[b][k] != 0:
                return False
        for c in range(k+1, n):
            if mat[r][c] != 0:
                return False
        for d in range(k-1, -1, -1):
            if mat[r][d] != 0:
                return False
        return True

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and is_special(i, j):
                cnt += 1
    return cnt


# ---------------------------------------------------------------------
# Approach 2: Pre-computation. Time: O(m * n)                       !**
# ---------------------------------------------------------------------
def solution_two(mat: List[List[int]]) -> int:
    """Given an m x n binary matrix mat, return the number of special
    positions in mat. A position (i, j) is called special if
    mat[i][j] == 1 and all other elements in row i and column j are 0.

    Examples:
        >>> solution_two([[1,0,0], [0,0,1], [1,0,0]])
        1
        >>> solution_two([[1,0,0], [0,1,0], [0,0,1]])
        3
    """
    cnt, m, n = 0, len(mat), len(mat[0])
    rows, cols = [0] * m, [0] * n
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                rows[i] += 1
                cols[j] += 1
    for k in range(m):
        for l in range(n):
            if mat[k][l] == rows[k] == cols[l] == 1:
                cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
