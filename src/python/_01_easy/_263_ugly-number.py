import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(log n). Space: O(1)                       !
# ---------------------------------------------------------------------
def solution(n: int) -> bool:
    """An ugly number is a positive integer whose prime factors are
    limited to 2, 3, and 5. Given an integer n, return True if n is an
    ugly number.

    Examples:
        >>> solution(0)
        False
        >>> solution(1)
        True
        >>> solution(6)
        True
        >>> solution(11)
        False
        >>> solution(14)
        False
    """
    def keepDividing(a, b) -> int:
        while a % b == 0:
            a //= b
        return a

    if n <= 0:
        return False
    if n <= 6:
        return True
    for num in [2, 3, 5]:
        n = keepDividing(n, num)

    return n == 1


if __name__ == '__main__':
    doctest.testmod()
