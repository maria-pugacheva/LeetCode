import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(T)                              ***
# ---------------------------------------------------------------------
def solution(s: str, t: str) -> bool:
    """Return True if s is a subsequence of t; otherwise, return False.

    Examples:
        >>> solution('abc', 'ahbgdc')
        True
        >>> solution('axc', 'ahbgdc')
        False
    """
    i = 0
    for j in range(len(t)):
        if t[j] == s[i]:
            i += 1
    return i == len(s)


if __name__ == '__main__':
    doctest.testmod()
