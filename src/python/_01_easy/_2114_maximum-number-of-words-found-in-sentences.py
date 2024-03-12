import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Count Spaces. Time: O(n * m)                          ***
# ---------------------------------------------------------------------
def solution(sentences: List[str]) -> int:
    """Return the maximum number of words that appear in a single
    sentence.

    Examples:
        >>> solution(['please wait', 'continue to win', 'hi'])
        3
        >>> solution(['i like apples', 'this is great thanks'])
        4
    """
    cnt = 0
    for s in sentences:
        c = 1
        for ch in s:
            if ch == ' ':
                c += 1
        cnt = max(cnt, c)
    return cnt


if __name__ == '__main__':
    doctest.testmod()
