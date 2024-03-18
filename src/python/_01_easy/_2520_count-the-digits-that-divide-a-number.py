import doctest


# ---------------------------------------------------------------------
# Approach 1: Modulo.                                               ***
# ---------------------------------------------------------------------
def solution(num: int) -> int:
    """Return the number of digits in num that divide num without
    leaving any remainder.

    Note: Could also convert num to string.

    Examples:
        >>> solution(7)
        1
        >>> solution(54)
        0
        >>> solution(121)
        2
        >>> solution(1248)
        4
    """
    cnt, n = 0, num
    while n:
        cnt += num % (n % 10) == 0
        n //= 10
    return cnt


if __name__ == '__main__':
    doctest.testmod()
