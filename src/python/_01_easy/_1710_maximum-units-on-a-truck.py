import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution(boxTypes: List[List[int]], truckSize: int) -> int:
    """Given an integer truckSize, which is the maximum number of boxes
    that can be put on a truck, and a 2D array boxTypes, where
    boxTypes[i] = [numberOfBoxes-i, numberOfUnitsPerBox-i], return the
    maximum total number of units that can be put on the truck.

    Examples:
        >>> solution([[1, 3]], 4)
        3
        >>> solution([[1, 3], [2, 2], [3, 1]], 4)
        8
        >>> solution([[5, 10], [2, 5], [4, 7], [3, 9]], 10)
        91
    """
    boxTypes.sort(key=lambda x: x[1])
    cnt = 0
    for i in range(len(boxTypes) - 1, -1, -1):
        cnt += min(boxTypes[i][0], truckSize) * boxTypes[i][1]
        truckSize -= boxTypes[i][0]
        if truckSize <= 0:
            break
    return cnt


if __name__ == '__main__':
    doctest.testmod()
