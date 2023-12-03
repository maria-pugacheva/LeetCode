import doctest
from collections import defaultdict
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting + Dictionary                                  ***
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
    groups = defaultdict(list)
    for s in strs:
        a = ''.join(sorted(s))
        groups[a].append(s)
    return list(groups.values())


if __name__ == '__main__':
    doctest.testmod()
