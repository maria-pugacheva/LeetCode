import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Counter. Time: O(n * k)                               ***
# ---------------------------------------------------------------------
def solution(words: List[str]) -> int:
    """Return True if you can make every string in words equal.

    Notes:
        In one operation, pick two distinct indices i and j, where
        words[i] is a non-empty string, and move any character from
        words[i] to any position in words[j].

    Preconditions:
        1 <= len(words) <= 100
        1 <= len(words[i]) <= 100
        words[i] consists of lowercase English letters

    Examples:
        >>> solution(['b', 'a'])
        False
        >>> solution(['ab', 'a'])
        False
        >>> solution(['abc', 'aabc', 'bc'])
        True
    """
    cnt = [0] * 26

    for word in words:
        for ch in word:
            cnt[ord(ch) - 97] += 1

    n = len(words)
    for x in cnt:
        if x % n != 0:
            return False

    return True


if __name__ == '__main__':
    doctest.testmod()
