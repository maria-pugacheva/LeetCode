import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n^2)                                ***
# ---------------------------------------------------------------------
def solution(grid: List[List[int]]) -> bool:
    """A square matrix is said to be an X-Matrix if all the elements in
    the diagonals of the matrix are non-zero and all other elements are
    0. Given a 2D integer array grid of size n x n representing a square
    matrix, return True if grid is an X-Matrix. Otherwise, return False.

    Examples:
        >>> solution([[5,7,0], [0,3,1], [0,5,0]])
        False
        >>> solution([[2,0,0,1], [0,3,1,0], [0,5,2,0], [4,0,0,2]])
        True
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == j or len(grid[0]) - 1 - i == j:
                if grid[i][j] == 0:
                    return False
            elif grid[i][j] != 0:
                return False
    return True


if __name__ == '__main__':
    doctest.testmod()
