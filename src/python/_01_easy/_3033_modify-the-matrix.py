import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: O(1) Memory. Time: O(m * 2n)                          ^**
# ---------------------------------------------------------------------
def solution(matrix: List[List[int]]) -> List[List[int]]:
    """Given a 0-indexed m x n integer matrix matrix, replace each
    element with the value -1 with the maximum element in its respective
    column.

    Examples:
        >>> solution([[3, -1], [5, 2]])
        [[3, 2], [5, 2]]
        >>> solution([[1, 2, -1], [4, -1, 6], [7, 8, 9]])
        [[1, 2, 9], [4, 8, 6], [7, 8, 9]]
    """
    m, n = len(matrix), len(matrix[0])
    for r in range(n):
        mx = -1
        for c in range(m):
            mx = max(mx, matrix[c][r])
        for j in range(m):
            if matrix[j][r] == -1:
                matrix[j][r] = mx
    return matrix


if __name__ == '__main__':
    doctest.testmod()
