import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O((n * m) + k)                    ***
# ---------------------------------------------------------------------
def solution(s: str, words: List[str]) -> bool:
    """Given a string s and an array of strings words, determine whether
    s is a prefix string of words.

    Examples:
        >>> solution('ilovetocode', ['i', 'love', 'to' 'code', 'cake'])
        True
        >>> solution('ccccccccc', ['cc', 'ccc'])
        False
        >>> solution('fajsldfsa', ['faj', 's', 'ldfs', 'afdfs', 'f'])
        False
        >>> solution('ilikeleetcode', ['i', 'like', 'leetcodeq'])
        False
    """
    i, k = 0, len(s)
    for w in words:
        if i == k:
            break
        t = i
        for j in range(len(w)):
            if (t < k and w[j] != s[t]) or (t == k and 0 < j < len(w)):
                return False
            t += 1
        i = t
    return i >= k


if __name__ == '__main__':
    doctest.testmod()
