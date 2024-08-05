import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Hash Table. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(n: int, pick: List[List[int]]) -> int:
    """You are given an integer n representing the number of players in
    a game and a 2D array pick where pick[i] = [x-i, y-i] represents
    that the player x-i picked a ball of color y-i. Player i wins the
    game if they pick strictly more than i balls of the same color.
    Return the number of players who win the game.

    Examples:
        >>> solution(2, [[0, 8], [0, 3]])
        1
        >>> solution(5, [[1 ,1], [1, 2], [1, 3], [1, 4]])
        0
        >>> solution(5, [[1, 1], [2, 4], [2, 4], [2, 4]])
        1
        >>> solution(4, [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]])
        2
    """
    cnt = 0
    colors = [{} for _ in range(n)]
    for p, c in pick:
        if colors[p] != -1:
            colors[p][c] = colors[p].get(c, 0) + 1
            if colors[p][c] > p:
                cnt += 1
                colors[p] = -1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
