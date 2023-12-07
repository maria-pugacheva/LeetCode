import doctest


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n^3)                             ***
# ---------------------------------------------------------------------
# Hint: Allocate all possible substrings first.
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
    def is_unique(start, end) -> bool:
        seen = set()
        for k in range(start, end + 1):
            ch = s[k]
            if ch in seen:
                return False
            seen.add(ch)
        return True

    longest = 0
    for i in range(len(s)):
        for j in range(len(s)):
            length = j - i + 1
            if is_unique(i, j) and longest < length:
                longest = length
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
