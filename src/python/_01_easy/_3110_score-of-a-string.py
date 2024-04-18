import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Return the sum of the absolute difference between the ASCII
    values of adjacent characters in s.

    Examples:
        >>> solution('aa')
        0
        >>> solution('zaz')
        50
        >>> solution('hello')
        13
    """
    res, prev = 0, ord(s[0])
    for i in range(1, len(s)):
        curr = ord(s[i])
        res += abs(prev - curr)
        prev = curr
    return res


if __name__ == '__main__':
    doctest.testmod()
