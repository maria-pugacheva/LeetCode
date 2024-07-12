import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Extra Memory. Time: O(n * m). Space: O(n * m)         ***
# ---------------------------------------------------------------------
def solution_one(mat: List[List[int]]) -> List[List[int]]:
    """Given an m x n integer matrix mat, if an element is 0, set its
    entire row and column to 0's. Modify mat in place.

    Examples:
        >>> solution_one([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        >>> solution_one([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        >>> solution_one([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], \
        [13, 14, 15, 0]])
        [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    rows = set()
    cols = set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for l in range(len(mat)):
        for k in range(len(mat[0])):
            if l in rows or k in cols:
                mat[l][k] = 0
    return mat


# ---------------------------------------------------------------------
# Approach 2: No Extra Memory. Time: O(n * m). Space: O(1)          !**
# ---------------------------------------------------------------------
def solution_two(mat: List[List[int]]) -> List[List[int]]:
    """Given an m x n integer matrix mat, if an element is 0, set its
    entire row and column to 0's. Modify mat in place.

    Examples:
        >>> solution_two([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        >>> solution_two([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        >>> solution_two([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], \
        [13, 14, 15, 0]])
        [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    is_col = is_row = False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
                if j == 0:
                    is_col = True
                if i == 0:
                    is_row = True
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
    if is_row:
        for j in range(len(mat[0])):
            mat[0][j] = 0
    if is_col:
        for i in range(len(mat)):
            mat[i][0] = 0
    return mat


if __name__ == '__main__':
    doctest.testmod()
