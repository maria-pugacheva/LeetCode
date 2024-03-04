import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(words: List[str]) -> int:
    """Return the maximum number of pairs that can be formed from the
    array words. The string words[i] can be paired with the string
    words[j] if the string words[i] is equal to the reversed string of
    words[j].

    Examples:
        >>> solution(['cd', 'ac', 'dc', 'ca', 'zz'])
        2
        >>> solution(['ab', 'ba', 'cc'])
        1
        >>> solution(['aa', 'ab'])
        0
    """
    s = set()
    cnt = 0
    for w in words:
        if w[1] + w[0] in s:
            cnt += 1
        else:
            s.add(w)
    return cnt


if __name__ == '__main__':
    doctest.testmod()
