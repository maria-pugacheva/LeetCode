import doctest


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                !**
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
    longest = start = 0
    d = {}
    for i in range(len(s)):
        ch = s[i]
        if ch in d:
            start = max(start, d[ch] + 1)
        longest = max(longest, i - start + 1)
        d[ch] = i
    return longest


if __name__ == '__main__':
    doctest.testmod()
