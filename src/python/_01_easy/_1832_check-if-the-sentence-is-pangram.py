import doctest


# ---------------------------------------------------------------------
# Approach 1: Count List I. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> bool:
    """Return True if s is a pangram, or False otherwise.

    Notes:
        A pangram is a sentence where every letter of the English
        alphabet appears at least once.

    Preconditions:
        1 <= len(s) <= 1000
        s consists of lowercase English letters

    Examples:
        >>> solution_one('hello')
        False
        >>> solution_one('leetcode')
        False
        >>> solution_one('thequickbrownfoxjumpsoverthelazydog')
        True
    """
    chars = [0] * 26
    zeros = 26
    for ch in s:
        i = ord(ch) - 97
        if chars[i] == 0:
            zeros -= 1
            chars[i] = 1
    return zeros == 0


# ---------------------------------------------------------------------
# Approach 2: Count List II. Time: O(n)                             ***
# ---------------------------------------------------------------------
def solution_two(s: str) -> bool:
    """Return True if s is a pangram, or False otherwise.

    Notes:
        A pangram is a sentence where every letter of the English
        alphabet appears at least once.

    Preconditions:
        1 <= len(s) <= 1000
        s consists of lowercase English letters

    Examples:
        >>> solution_two('hello')
        False
        >>> solution_two('leetcode')
        False
        >>> solution_two('thequickbrownfoxjumpsoverthelazydog')
        True
    """
    chars = [False] * 26
    for ch in s:
        chars[ord(ch) - 97] = True
    return sum(chars) == 26


if __name__ == '__main__':
    doctest.testmod()
