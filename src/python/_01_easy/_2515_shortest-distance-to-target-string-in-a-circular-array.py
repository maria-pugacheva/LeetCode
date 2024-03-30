import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ^**
# ---------------------------------------------------------------------
def solution(words: List[str], target: str, ind: int) -> int:
    """Given a 0-indexed circular string array words, a string target,
    and an integer ind, return the shortest distance needed to reach
    the string target from ind. If the string target does not exist in
    words, return -1.

    Examples:
        >>> solution(['a', 'b', 'c'], 'c', 0)
        1
        >>> solution(['hi', 'a', 'b', 'c', 'hi', 'd'], 'hi', 1)
        1
        >>> solution(['hi', 'a', 'b', 'c', 'd', 'hi', 'e'], 'hi', 3)
        2
        >>> solution(['hi', 'a', 'b', 'c', 'd', 'hi', 'e'], 'hey', 2)
        -1
    """
    res, n = float('inf'), len(words)
    for i in range(n):
        if words[i] == target:
            res = min(res, abs(i - ind), n - abs(i - ind))
    return res if res != float('inf') else -1


if __name__ == '__main__':
    doctest.testmod()
