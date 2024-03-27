import doctest
from collections import Counter


# ---------------------------------------------------------------------
# Approach 1: Two Counters. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution(string: str, target: str) -> int:
    """Return the maximum number of copies of target that can be formed
    by taking letters from string and rearranging them.

    Examples:
        >>> solution('abcba', 'abc')
        1
        >>> solution('abbaccaddaeea', 'aaaaa')
        1
        >>> solution('abc', 'abcd')
        0
        >>> solution('ilovecodingonleetcode', 'code')
        2
    """
    s = Counter(string)
    t = Counter(target)
    res = float('inf')
    for k, v in t.items():
        if k in s:
            res = min(res, s[k] // v)
        else:
            return 0
    return res


if __name__ == '__main__':
    doctest.testmod()
