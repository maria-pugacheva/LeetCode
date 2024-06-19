import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log(n))                            ***
# ---------------------------------------------------------------------
def solution_one(points: List[List[int]]) -> int:
    """Given the array points, return the minimum number of arrows that
    must be shot to burst all balloons.

    Examples:
        >>> solution_one([[1,2],[2,3], [3,4], [4,5]])
        2
        >>> solution_one([[1,2], [3,4], [5,6], [7,8]])
        4
        >>> solution_one([[10,16],[2,8],[1,6],[7,12]])
        2
        >>> solution_one([[9,12], [1,10], [4,11], [3,9], [6,9], [6,7]])
        2
    """
    cnt, start = 1, 0
    points.sort(key=lambda x: x[1])
    for i in range(1, len(points)):
        if points[i][0] > points[start][1]:
            cnt += 1
            start = i
    return cnt


if __name__ == '__main__':
    doctest.testmod()
