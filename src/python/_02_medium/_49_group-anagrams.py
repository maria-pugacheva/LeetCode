import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. T: O(n k log k). S: O(nk)                    ***
# ---------------------------------------------------------------------
# Complexity Analysis: k is the maximum length of a string in strs
# ---------------------------------------------------------------------
def solution_one(strs: List[str]) -> List[List[str]]:
    """Given an array of strings strs, group the anagrams together.

    Preconditions:
        1 <= len(strs) <= 10^4
        0 <= len(strs[i]) <= 100
        strs[i] consists of lowercase English letters

    Examples:
        >>> solution_one(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        >>> solution_one([''])
        [['']]
        >>> solution_one([''])
        [['']]
    """
    groups = {}
    for s in strs:
        t = ''.join(sorted(s))
        if t not in groups:
            groups[t] = []
        groups[t].append(s)
    return list(groups.values())


# ---------------------------------------------------------------------
# Approach 2: Categorize by Count. T: O(nk). S: O(nk)               ^**
# ---------------------------------------------------------------------
# Complexity Analysis: k is the maximum length of a string in strs
# ---------------------------------------------------------------------
def solution_two(strs: List[str]) -> List[List[str]]:
    """Given an array of strings strs, group the anagrams together.

    Preconditions:
        1 <= len(strs) <= 10^4
        0 <= len(strs[i]) <= 100
        strs[i] consists of lowercase English letters

    Examples:
        >>> solution_two(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        >>> solution_two([''])
        [['']]
        >>> solution_two([''])
        [['']]
    """
    groups = {}
    for s in strs:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        t = tuple(cnt)
        if t not in groups:
            groups[t] = []
        groups[t].append(s)
    return list(groups.values())


if __name__ == '__main__':
    doctest.testmod()
