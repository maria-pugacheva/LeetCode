import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sets. Time: O(n^2)                                    !**
# ---------------------------------------------------------------------
def solution(board: List[List[str]]) -> bool:
    """Determine if a 9 x 9 Sudoku board is valid.

    Examples:
        >>> solution([["5","3",".",".","7",".",".",".","."],\
        ["6",".",".","1","9","5",".",".","."],\
        [".","9","8",".",".",".",".","6","."],\
        ["8",".",".",".","6",".",".",".","3"],\
        ["4",".",".","8",".","3",".",".","1"],\
        ["7",".",".",".","2",".",".",".","6"],\
        [".","6",".",".",".",".","2","8","."],\
        [".",".",".","4","1","9",".",".","5"],\
        [".",".",".",".","8",".",".","7","9"]])
        True
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            x = board[i][j]
            if x.isnumeric():
                if x in rows[i] or x in cols[i] \
                        or x in boxes[(i//3) * 3 + (j//3)]:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                boxes[(i//3) * 3 + (j//3)].add(x)
    return True


if __name__ == '__main__':
    doctest.testmod()
