import doctest


# ---------------------------------------------------------------------
# Approach 1: Counter. Time: O(m)                                   ***
# ---------------------------------------------------------------------
def solution(note: str, magazine: str) -> bool:
    """Return True if note can be constructed by using the letters from
    magazine and False otherwise.

    Examples:
        >>> solution('a', 'b')
        False
        >>> solution('aa', 'ab')
        False
        >>> solution('aa', 'aba')
        True
    """
    magazine_chars = [0] * 26
    for ch in magazine:
        magazine_chars[ord(ch) - 97] += 1
    for ch in note:
        magazine_chars[ord(ch) - 97] -= 1
        if magazine_chars[ord(ch) - 97] < 0:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
