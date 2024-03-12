import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(words: List[str], s: str) -> bool:
    """Return True if s is an acronym of words.

    Examples:
        >>> solution(['alice', 'bob', 'charlie'], 'abc')
        True
        >>> solution(['an', 'apple'], 'a')
        False
        >>> solution(['apple'], 'aa')
        False
    """
    if len(words) != len(s):
        return False
    for i in range(len(words)):
        if words[i][0] != s[i]:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
