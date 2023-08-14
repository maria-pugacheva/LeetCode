import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution_one(s: str, ch: str) -> str:
    """Reverse the part of s from s[0] to the index of ch (if present).

    Preconditions:
        1 <= len(s) <= 250
        s consists of lowercase English letters
        ch is a lowercase English letter

    Examples:
        >>> solution_one('z', 'z')
        'z'
        >>> solution_one('abcd', 'z')
        'abcd'
        >>> solution_one('abcdefd', 'd')
        'dcbaefd'
    """
    chars = list(s)
    i = j = 0
    while j < len(chars):
        if chars[j] == ch:
            while i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
            return ''.join(chars)
        j += 1
    return s


if __name__ == '__main__':
    doctest.testmod()
