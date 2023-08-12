import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution_one(s: List[str], t: List[str]) -> int:
    """Return the number of strings that appear once in both s and t.

    Preconditions:
        1 <= len(s), len(t) <= 1000
        1 <= len(s[i]), len(t[j]) <= 30
        s[i] and t[j] consists only of lowercase English letters

    Examples:
        >>> solution_one(['b', 'bb', 'bbb'], ['a', 'aa', 'aaa'])
        0
        >>> solution_one(['a', 'ab'], ['a', 'a', 'a', 'ab'])
        1
        >>> solution_one(['am', 'i', 'is'], ['am', 'is'])
        2
    """
    cnt = 0
    d = {}
    for w in s:
        d[w] = d.get(w, 0) + 1
    for w in t:
        if w in d:
            if d[w] == 1:
                cnt += 1
                d[w] = -1
            elif d[w] == -1:
                cnt -= 1
                d[w] = 0
    return cnt


if __name__ == '__main__':
    doctest.testmod()
