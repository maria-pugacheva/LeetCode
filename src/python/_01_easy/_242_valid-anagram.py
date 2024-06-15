import doctest
from collections import Counter


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n). Space: O(n)                ^**
# ---------------------------------------------------------------------
def solution_one(s: str, t: str) -> bool:
    """Given two strings s and t, return True if t is an anagram of s.

    Examples:
        >>> solution_one('car', 'rac')
        True
        >>> solution_one('car', 'rat')
        False
        >>> solution_one('aaaa', 'aa')
        False
        >>> solution_one('anagram', 'nagaram')
        True
    """
    return sorted(s) == sorted(t)


# ---------------------------------------------------------------------
# Approach 2: HashMap. Time: O(n). Space: O(1)                      ***
# ---------------------------------------------------------------------
def solution_two(s: str, t: str) -> bool:
    """Given two strings s and t, return True if t is an anagram of s.

    Examples:
        >>> solution_two('car', 'rac')
        True
        >>> solution_two('car', 'rat')
        False
        >>> solution_two('aaaa', 'aa')
        False
        >>> solution_two('anagram', 'nagaram')
        True
    """
    if len(s) != len(t):
        return False
    c = Counter(s)
    for i in range(len(t)):
        if t[i] not in c or c[t[i]] - 1 < 0:
            return False
        c[t[i]] -= 1
    return True


if __name__ == '__main__':
    doctest.testmod()
