import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. T: O(n k log k). S: O(nk)                    ***
# ---------------------------------------------------------------------
# Complexity Analysis: k is the maximum length of a string in words
# ---------------------------------------------------------------------
def solution_one(words: List[str]) -> List[List[str]]:
    """Given an array of strings words, group the anagrams together.

    Preconditions:
        1 <= len(words) <= 10^4
        0 <= len(words[i]) <= 100
        words[i] consists of lowercase English letters

    Examples:
        >>> solution_one(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        >>> solution_one([''])
        [['']]
        >>> solution_one([''])
        [['']]
    """
    groups = {}
    for s in words:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())


# ---------------------------------------------------------------------
# Approach 2: Categorize by Count. T: O(nk). S: O(nk)               ^**
# ---------------------------------------------------------------------
# Complexity Analysis: k is the maximum length of a string in words
# ---------------------------------------------------------------------
def solution_two(words: List[str]) -> List[List[str]]:
    """Given an array of strings words, group the anagrams together.

    Preconditions:
        1 <= len(words) <= 10^4
        0 <= len(words[i]) <= 100
        words[i] consists of lowercase English letters

    Examples:
        >>> solution_two(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        >>> solution_two([''])
        [['']]
        >>> solution_two([''])
        [['']]
    """
    groups = {}
    for s in words:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        key = tuple(cnt)
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())


if __name__ == '__main__':
    doctest.testmod()
