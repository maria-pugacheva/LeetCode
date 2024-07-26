import doctest


# ---------------------------------------------------------------------
# Approach 1: Check Length. Time: O(log n)                          !**
# ---------------------------------------------------------------------
def solution(n: int) -> str:
    """Given an integer n, add a dot ('.') as the thousands separator
    and return it as a string.

    Preconditions:
        0 <= n < 2^31

    Examples:
        >>> solution(0)
        '0'
        >>> solution(987)
        '987'
        >>> solution(1238)
        '1.238'
        >>> solution(123456789)
        '123.456.789'
    """
    res = []
    s = str(n)
    for i in range(len(s)):
        if i > 0 and (len(s) - i) % 3 == 0:
            res.append('.')
        res.append(s[i])
    return ''.join(res)


if __name__ == '__main__':
    doctest.testmod()
