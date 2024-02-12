import doctest


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the longest palindromic substring in s.

    Examples:
        >>> solution_one('AaaAa')
        0
        >>> solution_one('aaB')
        1
        >>> solution_one('aaBbC')
        2
        >>> solution_one('aaBbCb')
        3
    """
    cnt = 0
    curr = s[0].lower()
    for i in range(1, len(s)):
        ch = s[i].lower()
        if ch != curr:
            cnt += 1
            curr = ch
    return cnt


if __name__ == '__main__':
    doctest.testmod()
