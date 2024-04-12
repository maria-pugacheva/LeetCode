import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Counter                                               ***
# ---------------------------------------------------------------------
def solution(words: List[str]) -> List[str]:
    """Given a string array words, return an array of all characters
    that show up in all strings within the words (including duplicates).

    Examples:
        >>> solution(['bella', 'label', 'roller'])
        ['e', 'l', 'l']
        >>> solution(['cool', 'lock', 'cook'])
        ['c', 'o']
    """
    c, res = [100] * 26, []
    for w in words:
        t = [0] * 26
        for ch in w:
            t[ord(ch) - 97] += 1
        for i in range(26):
            c[i] = min(c[i], t[i])
    for j in range(26):
        if c[j] > 0:
            res.extend([chr(j + 97)] * c[j])
    return res


if __name__ == '__main__':
    doctest.testmod()
