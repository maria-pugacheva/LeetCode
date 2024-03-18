import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1)                                      ***
# ---------------------------------------------------------------------
def solution(n: int, t: int) -> int:
    """An integer x is called achievable if it can become equal to n
    after increasing or decrease x by 1, and simultaneously increasing
    or decreasing n by 1. Return the maximum possible achievable number.

    Examples:
        >>> solution(4, 1)
        6
        >>> solution(3, 2)
        7
        >>> solution(1, 7)
        15
    """
    return n + (2 * t)


if __name__ == '__main__':
    doctest.testmod()
