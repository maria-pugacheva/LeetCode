import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1)                                      ***
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Given a positive integer n, return the smallest positive integer
    that is a multiple of both 2 and n.

    Examples:
        >>> solution(5)
        10
        >>> solution(6)
        6
    """
    if n % 2 == 0:
        return n
    return n * 2


if __name__ == '__main__':
    doctest.testmod()
