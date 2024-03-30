import doctest


# ---------------------------------------------------------------------
# Approach 1: Longest Common Prefix                                 ***
# ---------------------------------------------------------------------
def solution(s1: str, s2: str, s3: str) -> int:
    """Given three strings: s1, s2, and s3, in one operation choose one
    of these strings and delete its rightmost character. Note that you
    are not allowed to make a string completely empty. Return the
    minimum number of operations required to make the strings equal.
    If it is impossible to make them equal, return -1.

    Examples:
        >>> solution('abc', 'abb', 'ab')
        2
        >>> solution('dac', 'bac', 'cac')
        -1
        >>> solution('a', 'a', 'a')
        0
    """
    sz1, sz2, sz3, i = len(s1), len(s2), len(s3), 0
    while i < sz1 and i < sz2 and i < sz3 and s1[i] == s2[i] == s3[i]:
        i += 1
    return -1 if i == 0 else sz1 + sz2 + sz3 - (i * 3)


if __name__ == '__main__':
    doctest.testmod()
