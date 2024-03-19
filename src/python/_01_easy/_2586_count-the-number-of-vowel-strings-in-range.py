import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Counter. Time: O(n)                                   ***
# ---------------------------------------------------------------------
def solution(words: List[str], left: int, right: int) -> int:
    """Return the number of vowel strings words[i] where i belongs to
    the inclusive range [left, right].

    Examples:
        >>> solution(['are', 'amy', 'u'], 0, 2)
        2
        >>> solution(['hey', 'aeo', 'mu', 'ooo', 'artro'], 1, 4)
        3
        >>> solution(['ab'], 0, 0)
        0
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    cnt = 0
    for i in range(left, right + 1, 1):
        if words[i][0] in vowels and words[i][-1] in vowels:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
