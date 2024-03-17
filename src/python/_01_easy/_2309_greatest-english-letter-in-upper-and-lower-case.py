import doctest


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Return the greatest English letter which occurs as both a
    lowercase and uppercase letter in s. The returned letter should be
    in uppercase. If no such letter exists, return an empty string.

    Examples:
        >>> solution('lEeTcOdE')
        'E'
        >>> solution('arRAzFif')
        'R'
        >>> solution('AbCdEfGhIjK')
        ''
    """
    res = ''
    seen = set()
    for ch in s:
        a = ord(ch)
        if a - 32 in seen or a + 32 in seen:
            res = max(res, ch.upper())
        else:
            seen.add(a)
    return res


if __name__ == '__main__':
    doctest.testmod()
