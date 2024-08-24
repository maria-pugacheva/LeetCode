import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sets. Time: O(n^2). Space: O(n^2)                       !
# ---------------------------------------------------------------------
def solution(board: List[List[str]]) -> bool:
    """Determine if a 9 x 9 Sudoku board is valid.

    Examples:
        >>> solution([\
        ['5','3','.','.','7','.','.','.','.'],\
        ['6','.','.','1','9','5','.','.','.'],\
        ['.','9','8','.','.','.','.','6','.'],\
        ['8','.','.','.','6','.','.','.','3'],\
        ['4','.','.','8','.','3','.','.','1'],\
        ['7','.','.','.','2','.','.','.','6'],\
        ['.','6','.','.','.','.','2','8','.'],\
        ['.','.','.','4','1','9','.','.','5'],\
        ['.','.','.','.','8','.','.','7','9']])
        True
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            x = (i // 3) * 3 + (j // 3)
            n = board[i][j]
            if n != '.' and (n in rows[i] or n in cols[i] or
                             n in boxes[(i // 3) * 3 + (j // 3)]):
                return False
            rows[i].add(n)
            cols[j].add(n)
            boxes[(i // 3) * 3 + (j // 3)].add(n)
    return True


if __name__ == '__main__':
    doctest.testmod()
