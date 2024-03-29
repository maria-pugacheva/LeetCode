import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1)                                      ***
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Given a positive integer n, return the minimum number of cuts
    needed to divide a circle into n equal slices.

    Examples:
        >>> solution(1)
        0
        >>> solution(3)
        3
        >>> solution(4)
        2
    """
    if n == 1:
        return 0
    return n if n & 1 else n // 2


if __name__ == '__main__':
    doctest.testmod()
