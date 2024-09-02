import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                         !
# ---------------------------------------------------------------------
def solution(triplets: List[List[int]], t: List[int]) -> bool:
    """You can obtain the target triplet t from the given array triplets
    by repeatedly updating any triplet to the maximum values of two
    different triplets. Return True if the target can be obtained;
    otherwise, return False.

    Examples:
        >>> solution([[3, 4, 5], [4, 5, 6]], [3, 2, 5])
        False
        >>> solution([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5])
        True
        >>> solution([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], \
        [5, 5, 5])
        True
    """
    good = set()
    for item in triplets:
        if item[0] > t[0] or item[1] > t[1] or item[2] > t[2]:
            continue
        for i, v in enumerate(item):
            if v == t[i]:
                good.add(i)
    return len(good) == 3


if __name__ == '__main__':
    doctest.testmod()
