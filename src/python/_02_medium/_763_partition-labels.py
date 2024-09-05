import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n). Space: O(1)                         !
# ---------------------------------------------------------------------
def solution(s: str) -> List[int]:
    """Return a list of integers representing the sizes of the maximum
    number of partitions of string s, where each letter appears in at
    most one part and the concatenation of all parts reconstructs the
    original string.

    Examples:
        >>> solution('eccbbbbdec')
        [10]
        >>> solution('ababcbacadefegdehijhklij')
        [9, 7, 8]
    """
    lastIndex = {}
    for i in range(len(s)):
        lastIndex[s[i]] = i
    res = []
    size, end = 0, 0
    for j in range(len(s)):
        size += 1
        end = max(end, lastIndex[s[j]])
        if end == j:
            res.append(size)
            size = 0
    return res


if __name__ == '__main__':
    doctest.testmod()
