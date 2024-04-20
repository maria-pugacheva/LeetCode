import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Four Pointers. Time: O(n)                             ***
# ---------------------------------------------------------------------
def solution(word1: List[str], word2: List[str]) -> bool:
    """Return True if word1 and word2 represent the same string, and
    False otherwise.

    Examples:
        >>> solution(['ab', 'c'], ['a', 'bc'])
        True
        >>> solution(['a', 'cb'], ['ab', 'c'])
        False
        >>> solution(['a', 'bc'], ['ab', 'cd'])
        False
        >>> solution(['abc', 'd', 'defg'], ['abcddefg'])
        True
    """
    w1 = w2 = i = j = 0
    while w1 < len(word1) and w2 < len(word2):
        if word1[w1][i] != word2[w2][j]:
            return False
        i += 1
        j += 1
        if i == len(word1[w1]):
            w1 += 1
            i = 0
        if j == len(word2[w2]):
            w2 += 1
            j = 0
    return w1 == len(word1) and w2 == len(word2)


if __name__ == '__main__':
    doctest.testmod()
