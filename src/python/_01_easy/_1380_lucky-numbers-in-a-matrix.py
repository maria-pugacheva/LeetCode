import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(m * n)                                   ***
# ---------------------------------------------------------------------
def solution(mat: List[List[int]]) -> List[int]:
    """Given an m x n matrix of distinct numbers, return all lucky
    numbers in mat. A lucky number is an element of the matrix such that
    it is the minimum element in its row and the maximum element in its
    column.

    Examples:
        >>> solution([[7,8], [1,2]])
        [7]
        >>> solution([[3,7,8], [9,11,13], [15,16,17]])
        [15]
        >>> solution([[1,10,4,2], [9,3,8,7], [15,16,17,12]])
        [12]
    """
    mn, mx = set(), set()
    for row in mat:
        mn.add(min(row))
    for i in range(len(mat[0])):
        t = 0
        for j in range(len(mat)):
            t = max(t, mat[j][i])
        mx.add(t)
    return list(mn & mx)


if __name__ == '__main__':
    doctest.testmod()
