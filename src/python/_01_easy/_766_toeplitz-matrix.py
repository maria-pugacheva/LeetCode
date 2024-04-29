import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(m * n)                              ***
# ---------------------------------------------------------------------
def solution(matrix: List[List[int]]) -> bool:
    """Given an m x n matrix, return True if the matrix is Toeplitz;
    otherwise, return False. A matrix is Toeplitz if every diagonal from
    top-left to bottom-right has the same elements.

    Examples:
        >>> solution([[1, 2], [2, 2]])
        False
        >>> solution([[1, 2], [3, 1]])
        True
        >>> solution([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
        True
    """
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


if __name__ == '__main__':
    doctest.testmod()
