import doctest


# ---------------------------------------------------------------------
# Approach 1: Frequency Count. Time: O(n)                           ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> bool:
    """Return true if all the characters in s have the same frequency.

    Preconditions:
        1 <= len(s) <= 1000
        s consists of lowercase English letters

    Examples:
        >>> solution_one('a')
        True
        >>> solution_one('abacbc')
        True
        >>> solution_one('aaabb')
        False
    """
    chars = [0] * 26
    for ch in s:
        chars[ord(ch) - 97] += 1
    for n in chars:
        if n != 0 and n != chars[ord(s[0]) - 97]:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
