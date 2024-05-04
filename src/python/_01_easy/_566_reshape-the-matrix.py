import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(m * n)                              ***
# ---------------------------------------------------------------------
def solution(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    """You are given an m x n matrix mat and two integers r and c
    representing the number of rows and the number of columns of the new
    reshaped matrix. If the reshape operation with given parameters is
    possible, output the new reshaped matrix; otherwise, output the
    original matrix.

    Examples:
        >>> solution([[1]], 1, 1)
        [[1]]
        >>> solution([[1, 2], [3, 4]], 2, 4)
        [[1, 2], [3, 4]]
        >>> solution([[1, 2], [3, 4]], 1, 4)
        [[1, 2, 3, 4]]
    """
    if r * c != len(mat) * len(mat[0]):
        return mat
    res, t = [], []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            t.append(mat[i][j])
            if len(t) == c:
                res.append(t)
                t = []
    return res


if __name__ == '__main__':
    doctest.testmod()
