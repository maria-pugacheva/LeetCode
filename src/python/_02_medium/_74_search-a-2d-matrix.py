import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n * m)                     !!!
# ---------------------------------------------------------------------
def solution(mat: List[List[int]], t: int) -> bool:
    """Return True if t is in matrix mat.

    Examples:
        >>> solution([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 3)
        True
        >>> solution([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 13)
        False
    """
    cols = len(mat[0])
    i, j = 0, len(mat) * cols - 1
    while i <= j:
        m = (i + j) // 2
        n = mat[m // cols][m % cols]
        if n == t:
            return True
        elif n < t:
            i = m + 1
        else:
            j = m - 1
    return False


if __name__ == '__main__':
    doctest.testmod()
