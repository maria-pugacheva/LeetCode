import doctest


# ---------------------------------------------------------------------
# Approach 1: Look for 'ba'. Time: O(n)                             ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> bool:
    """Given a string s consisting of only the characters 'a' and 'b',
    return True if every 'a' appears before every 'b' in the string.
    Otherwise, return false.

    Examples:
        >>> solution_one('bbb')
        True
        >>> solution_one('abab')
        False
        >>> solution_one('aaabbb')
        True
    """
    for i in range(len(s) - 1):
        if s[i] == 'b' and s[i + 1] == 'a':
            return False
    return True


# ---------------------------------------------------------------------
# Approach 2: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution_two(s: str) -> bool:
    """Given a string s consisting of only the characters 'a' and 'b',
    return True if every 'a' appears before every 'b' in the string.
    Otherwise, return false.

    Examples:
        >>> solution_two('bbb')
        True
        >>> solution_two('abab')
        False
        >>> solution_two('aaabbb')
        True
    """
    b = False
    for ch in s:
        if ch == 'a':
            if b:
                return False
        else:
            b = True
    return True


if __name__ == '__main__':
    doctest.testmod()
