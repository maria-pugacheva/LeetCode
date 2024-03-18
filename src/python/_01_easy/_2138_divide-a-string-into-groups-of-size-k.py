import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Slicing                                               ***
# ---------------------------------------------------------------------
def solution(s: str, k: int, fill: str) -> List[str]:
    """A string s can be partitioned into groups of size k. For the last
    group, if the string does not have k characters remaining, a
    character fill is used to complete the group. Return a string array
    denoting the composition of every group s has been divided into.

    Examples:
        >>> solution('a', 3, 'x')
        ['axx']
        >>> solution('abcdefghi', 3, 'x')
        ['abc', 'def', 'ghi']
        >>> solution('abcdefghij', 3, 'x')
        ['abc', 'def', 'ghi', 'jxx']
    """
    res = []
    for i in range(0, len(s), k):
        res.append(s[i:i+k])
    if len(res[-1]) < k:
        res[-1] = res[-1] + (fill * (k - len(res[-1])))
    return res


if __name__ == '__main__':
    doctest.testmod()
