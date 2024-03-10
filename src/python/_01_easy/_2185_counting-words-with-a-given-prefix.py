import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n * m)                              ***
# ---------------------------------------------------------------------
def solution(words: List[str], pref: str) -> int:
    """Return the number of strings in words that contain pref as a
    prefix.

    Examples:
        >>> solution(['pay', 'attention', 'practice', 'attend'], 'at')
        2
        >>> solution(['wb', 'tdkecwp', 'jtuqfks', 'w', 'c', 'f'], 'jcsdgs')
        0
    """
    cnt = 0
    for w in words:
        if w[0] != pref[0] or len(pref) > len(w):
            continue
        cnt += 1
        for i in range(len(pref)):
            if w[i] != pref[i]:
                cnt -= 1
                break
    return cnt


if __name__ == '__main__':
    doctest.testmod()
