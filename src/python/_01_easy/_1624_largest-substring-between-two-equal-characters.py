import doctest


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the length of the longest substring btw. 2 equal chars in s.

    Preconditions:
    1 <= len(s) <= 300
    s contains only lowercase English letters

    Examples:
        >>> solution_one('aa')
        0
        >>> solution_one('abbaca')
        4
        >>> solution_one('cbzxyrtm')
        -1
    """
    res = -1
    seen = {}
    for i in range(len(s)):
        ch = s[i]
        if ch in seen:
            res = max(res, abs(seen[ch] - i) - 1)
        else:
            seen[ch] = i
    return res


if __name__ == '__main__':
    doctest.testmod()
