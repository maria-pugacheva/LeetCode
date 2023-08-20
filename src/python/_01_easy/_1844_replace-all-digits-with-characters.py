import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Return s after replacing all digits.

    Preconditions:
        1 <= len(s) <= 100
        s consists only of lowercase English letters and digits
        shift(s[i-1], s[i]) <= 'z' for all odd indices i

    Examples:
        >>> solution_one('a1c1e1')
        'abcdef'
        >>> solution_one('a1b2c3d4e')
        'abbdcfdhe'
        >>> solution_one('b4n5h3d1a1')
        'bfnshkdeab'
    """
    chars = list(s)
    for i in range(1, len(s), 2):
        chars[i] = chr(ord(chars[i - 1]) + int(chars[i]))
    return ''.join(chars)


if __name__ == '__main__':
    doctest.testmod()
