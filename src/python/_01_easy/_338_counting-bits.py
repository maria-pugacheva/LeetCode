import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Odd/Even. Time: O(n)                                    !
# ---------------------------------------------------------------------
def solution(n: int) -> List[int]:
    """Given an integer n, return an array ans of length n + 1 such that
    for each i (0 <= i <= n), ans[i] is the number of 1's in the binary
    representation of i.

    Preconditions:
        0 <= n <= 10^5

    Examples:
        >>> solution(2)
        [0, 1, 1]
        >>> solution(5)
        [0, 1, 1, 2, 1, 2]
    """
    res = [0]
    for i in range(1, n + 1):
        if i % 2 == 0:
            res.append(res[i // 2])
        else:
            res.append(res[i - 1] + 1)
    return res


if __name__ == '__main__':
    doctest.testmod()
