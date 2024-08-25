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
           >>> solution_one('aab')
           2
           >>> solution_one('abba')
           2
           >>> solution_one('pwwkew')
           3
           >>> solution_one('bbbbb')
           1
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
# Approach 2: Dictionary. Time: O(n)                                !**
# ---------------------------------------------------------------------
def solution_two(s: str) -> int:
    """Return the length of the longest unique substring in s.

       Preconditions:
           0 <= s.length <= 5 * 10^4
           s consists of English letters, digits, symbols, and spaces

       Examples:
           >>> solution_two('aab')
           2
           >>> solution_two('abba')
           2
           >>> solution_two('pwwkew')
           3
           >>> solution_two('bbbbb')
           1
    """
    longest = i = 0
    d = {}
    for j in range(len(s)):
        if s[j] in d:
            i = max(i, d[s[j]] + 1)
        longest = max(longest, j - i + 1)
        d[s[j]] = j
    return longest


if __name__ == '__main__':
    doctest.testmod()
