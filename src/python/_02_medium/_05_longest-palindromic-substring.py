import doctest


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n^3)                             ***
# ---------------------------------------------------------------------
# Hint: Allocate all possible substrings first.
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Return the longest palindromic substring in s.

       Examples:
           >>> solution_one('babad')
           'bab'
           >>> solution_one('abba')
           'abba'
       """
    def is_palindrome(l, r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    longest = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(i, j) and len(longest) < j - i + 1:
                longest = s[i:j + 1]
    return longest


# ---------------------------------------------------------------------
# Approach 2: Expand From Centers. Time: O(n^2)                       !
# ---------------------------------------------------------------------
def solution_two(s: str) -> str:
    """Return the longest palindromic substring in s.

       Examples:
           >>> solution_two('babad')
           'bab'
           >>> solution_two('abba')
           'abba'
       """
    def expand(l, r) -> int:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    start = end = length = 0
    for i in range(len(s)):
        curr_max_len = max(expand(i, i), expand(i, i+1))
        if curr_max_len > length:
            start = i - ((curr_max_len - 1) // 2)
            end = i + curr_max_len // 2
            length = curr_max_len

    return s[start:end+1]


if __name__ == '__main__':
    doctest.testmod()
