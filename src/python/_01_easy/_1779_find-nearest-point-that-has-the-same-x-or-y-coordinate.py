import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n)                                    ***
# ---------------------------------------------------------------------
def solution(x: int, y: int, points: List[List[int]]) -> int:
    """Return the index of the valid point with the smallest Manhattan
    distance from your current location

    Preconditions:
        1 <= len(points) <= 10^4
        len(points[i]) == 2
        1 <= x, y, points[i][0], points[i][1] <= 10^4

    Examples:
        >>> solution(3, 4, [[3, 4]])
        0
        >>> solution(3, 4, [[2, 3]])
        -1
        >>> solution(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]])
        2
    """
    ind = -1
    dist = 100_000_000_000
    for i in range(len(points)):
        if points[i][0] == x or points[i][1] == y:
            t = abs(x - points[i][0]) + abs(y - points[i][1])
            if t < dist:
                dist = t
                ind = i
    return ind


if __name__ == '__main__':
    doctest.testmod()
