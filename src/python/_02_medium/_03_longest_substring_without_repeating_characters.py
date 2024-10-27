import doctest


# ---------------------------------------------------------------------
# Approach 1: Brute Force - TLE. Time: O(n^3)                       ^**
# ---------------------------------------------------------------------
# Hint: Find all possible substrings first.
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the length of the longest unique substring in s.

    Preconditions:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols, and spaces

    Examples:
        >>> solution_one('a')
        1
        >>> solution_one('au')
        2
        >>> solution_one('aab')
        2
        >>> solution_one('abba')
        2
        >>> solution_one('bbbbb')
        1
        >>> solution_one('pwwkew')
        3
        >>> solution_one('abcabcbb')
        3
    """
    def is_unique(left: int, right: int) -> bool:
        chars = set()
        for k in range(left, right + 1):
            if s[k] in chars:
                return False
            chars.add(s[k])
        return True

    longest = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if is_unique(i, j):
                longest = max(longest, j - i + 1)
    return longest


# ---------------------------------------------------------------------
# Approach 2: Set. Time: O(n)                                       !**
# ---------------------------------------------------------------------
def solution_two(s: str) -> int:
    """Return the length of the longest unique substring in s.

    Preconditions:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols, and spaces

    Examples:
        >>> solution_two('a')
        1
        >>> solution_two('au')
        2
        >>> solution_two('aab')
        2
        >>> solution_two('abba')
        2
        >>> solution_two('bbbbb')
        1
        >>> solution_two('pwwkew')
        3
        >>> solution_two('abcabcbb')
        3
    """
    res = 0
    i = 0
    charSet = set()
    for j in range(len(s)):
        while s[j] in charSet:
            charSet.remove(s[i])
            i += 1
        res = max(res, j - i + 1)
        charSet.add(s[j])
    return res


if __name__ == '__main__':
    doctest.testmod()
