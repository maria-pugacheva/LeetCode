import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Scanning I. Time: O(n * m), m == len(shortest)        ***
# ---------------------------------------------------------------------
def solution_one(words: List[str]) -> str:
    """Find the longest common prefix string amongst an array of
    strings words. If there is no common prefix, return an empty string.

    Examples:
        >>> solution_one(['dog', 'racecar', 'car'])
        ''
        >>> solution_one(['a'])
        'a'
        >>> solution_one(['flower', 'flow', 'flight'])
        'fl'
    """
    prefix = []
    shortest = min([len(w) for w in words])
    diff = False
    for i in range(shortest):
        for j in range(len(words)):
            if words[j][i] != words[0][i]:
                diff = True
        if not diff:
            prefix.append(words[0][i])
    return ''.join(prefix)


# ---------------------------------------------------------------------
# Approach 2: Scanning II. Time: O(n * m), m == len(shortest)       ***
# ---------------------------------------------------------------------
def solution_two(words: List[str]) -> str:
    """Find the longest common prefix string amongst an array of
    strings words. If there is no common prefix, return an empty string.

    Examples:
        >>> solution_two(['dog', 'racecar', 'car'])
        ''
        >>> solution_two(['a'])
        'a'
        >>> solution_two(['flower', 'flow', 'flight'])
        'fl'
    """
    for i in range(len(words[0])):
        for j in range(1, len(words)):
            if i == len(words[i]) or words[j][i] != words[0][i]:
                return words[j][:i]
    return '' if not words else words[0]


if __name__ == '__main__':
    doctest.testmod()
