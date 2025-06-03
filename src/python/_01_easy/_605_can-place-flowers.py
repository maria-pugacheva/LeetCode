import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n)                                      !
# ---------------------------------------------------------------------
def solution(fBed: List[int], n: int) -> bool:
    """Given an integer array fBed containing 0's and 1's, where 0
    means empty and 1 means not empty, and an integer n, return True if
    n new flowers can be planted in the flowerbed without violating the
    no-adjacent-flowers rule and False otherwise.

    Examples:
        >>> solution([1, 0, 0, 0, 1], 1)
        True
        >>> solution([1, 0, 0, 0, 1], 2)
        False
        >>> solution([1, 0, 1, 0, 1, 0, 1], 0)
        True
        >>> solution([0, 0, 0, 0, 0, 1, 0, 0], 0)
        True
    """
    cnt, length = 0, len(fBed)
    for i in range(length):
        if fBed[i] == 0:
            if (i == 0 or fBed[i - 1] == 0) and \
                    i == length - 1 or fBed[i + 1] == 0:
                fBed[i] = 1
                cnt += 1
        if cnt >= n:
            return True
    return False


if __name__ == '__main__':
    doctest.testmod()
