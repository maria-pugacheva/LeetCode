import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Check Second Position. Time: O(n)                     ***
# ---------------------------------------------------------------------
def solution(s: str, d: List[int]) -> bool:
    """Given a string s consisting of only lowercase English letters,
    where each letter in s appears exactly twice, and a 0-indexed
    integer array d of length 26. In a well-spaced string, the number
    of letters between the two occurrences of the i-th letter is d[i].
    If the i-th letter does not appear in s, then d[i] can be ignored.
    Return True if s is a well-spaced string; otherwise, return False.

    Examples:
        >>> solution('abaccb', [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        True
        >>> solution('aa', [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        False
    """
    for i in range(len(s)):
        ind = ord(s[i]) - 97
        if d[ind] != -1:
            j = i + 1 + d[ind]
            if j >= len(s) or s[i] != s[j]:
                return False
            else:
                d[ind] = -1
    return True


if __name__ == '__main__':
    doctest.testmod()
