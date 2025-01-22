import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Scanning. Time: O(n * m), m == len(shortest)          ***
# ---------------------------------------------------------------------
def solution(words: List[str]) -> str:
    """Find the longest common prefix string amongst an array of
    strings words. If there is no common prefix, return an empty string.

    Examples:
        >>> solution(['dog', 'racecar', 'car'])
        ''
        >>> solution(['a'])
        'a'
        >>> solution(['flower', 'flow', 'flight'])
        'fl'
    """
    for i in range(len(words[0])):
        for j in range(1, len(words)):
            if i == len(words[j]) or words[j][i] != words[0][i]:
                return words[j][:i]
    return words[0]


if __name__ == '__main__':
    doctest.testmod()
