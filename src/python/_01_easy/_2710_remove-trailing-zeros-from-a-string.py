import doctest


# ---------------------------------------------------------------------
# Approach 1: While Loop. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(num: str) -> str:
    """Given a positive integer num represented as a string, return the
    integer num without trailing zeros as a string.

    Examples:
        >>> solution('51230100')
        '512301'
        >>> solution('123')
        '123'
        >>> solution('123077000000800000')
        '1230770000008'
    """
    i = len(num) - 1
    while num[i] == '0':
        i -= 1
    return num[:i+1]


if __name__ == '__main__':
    doctest.testmod()
