import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sum                                                   ***
# ---------------------------------------------------------------------
def solution(teams: List[List[int]]) -> int:
    """Return the team that will be the champion of the tournament.

    Examples:
        >>> solution([[0, 1], [0, 0]])
        0
        >>> solution([[0, 0, 1], [1, 0, 1], [0, 0, 0]])
        1
    """
    for i in range(len(teams)):
        if sum(teams[i]) == len(teams) - 1:
            return i
    return -1


if __name__ == '__main__':
    doctest.testmod()
