import doctest
from collections import Counter


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
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
# Approach 2: Frequency Counter. Time: O(n). Space: O(1)            ***
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
    cnt = [0] * 26
    for i in range(len(s)):
        cnt[ord(s[i]) - 97] += 1
    for j in range(len(t)):
        cnt[ord(t[j]) - 97] -= 1
        if cnt[ord(t[j]) - 97] < 0:
            return False
    return sum(cnt) == 0


# ---------------------------------------------------------------------
# Approach 3: HashMap. Time: O(n). Space: O(n)                      ***
# ---------------------------------------------------------------------
# Follow up: What if the inputs contain Unicode characters? How would
#            you adapt your solution to such a case?
# ---------------------------------------------------------------------
def solution_three(s: str, t: str) -> bool:
    """Given two strings s and t, return True if t is an anagram of s.

    Examples:
        >>> solution_three('car', 'rac')
        True
        >>> solution_three('car', 'rat')
        False
        >>> solution_three('aaaa', 'aa')
        False
        >>> solution_three('anagram', 'nagaram')
        True
    """
    if len(s) != len(t):
        return False
    cnt = Counter(s)
    for i in range(len(t)):
        cnt[t[i]] = cnt.get(t[i], 0) - 1
        if cnt[t[i]] < 0:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
