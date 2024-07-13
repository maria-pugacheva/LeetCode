import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: In-Place. Time: O(n * n)                              ***
# ---------------------------------------------------------------------
def solution_one(mat: List[List[int]]) -> List[List[int]]:
    """Given an n x n 2D matrix representing an image, rotate the image
    by 90 degrees (CLOCKWISE).

    Examples:
        >>> solution_one([[1, 2], [3, 4]])
        [[3, 1], [4, 2]]
        >>> solution_one([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        >>> solution_one([[5, 1, 9, 11], [2, 4, 8, 10],\
        [13, 3, 6, 7], [15, 14, 12, 16]])
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    """
    length = len(mat)
    for r in range(length):
        for c in range(r, length):
            mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
    for row in range(length):
        i, j = 0, length - 1
        while i < j:
            mat[row][i], mat[row][j] = mat[row][j], mat[row][i]
            i += 1
            j -= 1
    return mat


# ---------------------------------------------------------------------
# Approach 2: In-Place. Time: O(n * n)                              ***
# ---------------------------------------------------------------------
def solution_two(mat: List[List[int]]) -> List[List[int]]:
    """Given an n x n 2D matrix representing an image, rotate the image
    by 90 degrees (COUNTERCLOCKWISE).

    Examples:
        >>> solution_two([[1, 2], [3, 4]])
        [[2, 4], [1, 3]]
        >>> solution_two([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        >>> solution_two([[5, 1, 9, 11], [2, 4, 8, 10],\
        [13, 3, 6, 7], [15, 14, 12, 16]])
        [[11, 10, 7, 16], [9, 8, 6, 12], [1, 4, 3, 14], [5, 2, 13, 15]]
    """
    length = len(mat)
    for r in range(length):
        for c in range(r, length):
            mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
    for col in range(length):
        i, j = 0, length - 1
        while i < j:
            mat[i][col], mat[j][col] = mat[j][col], mat[i][col]
            i += 1
            j -= 1
    return mat


if __name__ == '__main__':
    doctest.testmod()
