import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Boundaries. Time: O(n * m)                              !
# ---------------------------------------------------------------------
def solution(mat: List[List[int]]) -> List[int]:
    """Given an m x n matrix, return all elements of the matrix in
    spiral order.

    Examples:
        >>> solution([[1]])
        [1]
        >>> solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """
    res = []
    rows, cols = len(mat), len(mat[0])
    left = up = 0
    right = cols - 1
    down = rows - 1
    while len(res) < rows * cols:
        for i in range(left, right + 1):
            res.append(mat[up][i])
        for j in range(up + 1, down + 1):
            res.append(mat[j][right])
        if up != down:
            for k in range(right - 1, left - 1, -1):
                res.append(mat[down][k])
        if left != right:
            for l in range(down - 1, up, -1):
                res.append(mat[l][left])
        left += 1
        right -= 1
        up += 1
        down -= 1
    return res


if __name__ == '__main__':
    doctest.testmod()
