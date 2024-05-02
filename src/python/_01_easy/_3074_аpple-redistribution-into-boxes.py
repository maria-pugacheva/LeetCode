import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(m log m)                             ***
# ---------------------------------------------------------------------
def solution(apples: List[int], boxes: List[int]) -> int:
    """Given an array apples of size n and an array boxes of size m,
    return the minimum number of boxes needed to redistribute n packs
    of apples into boxes.

    Examples:
        >>> solution([1], [2])
        1
        >>> solution([5, 5, 5], [2, 4, 2, 7])
        4
        >>> solution([1, 3, 2], [4, 3, 1, 5, 2])
        2
    """
    total, cnt, i = sum(apples), 0, len(boxes) - 1
    boxes.sort()
    while total > 0 and i >= 0:
        total -= boxes[i]
        i -= 1
        cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
