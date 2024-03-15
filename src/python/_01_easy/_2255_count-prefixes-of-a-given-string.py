import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: No Built-ins. Time: O(n * m), where m == len(s)       ***
# ---------------------------------------------------------------------
def solution(words: List[str], s: str) -> int:
    """Return the number of strings in words that are a prefix of s.

    Examples:
        >>> solution(['a', 'a'], 'aa')
        2
        >>> solution(['a', 'b', 'c'], 'abc')
        1
        >>> solution(['a', 'b', 'c', 'ab', 'bc', 'abc'], 'abc')
        3
    """
    cnt = 0
    for w in words:
        if (len(w)) <= len(s):
            flag = True
            for i in range(len(w)):
                if w[i] != s[i]:
                    flag = False
                    break
            if flag:
                cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
