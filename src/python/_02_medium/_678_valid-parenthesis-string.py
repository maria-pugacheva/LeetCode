import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                                !
# ---------------------------------------------------------------------
def solution(s: str) -> bool:
    """Given a string s containing '(', ')', and '', return True if it
    is valid according to these rules: every '(' must be matched by
    a ')' and every ')' must be preceded by a '('; '*' can be a '('
    or ')', or an empty string.

    Examples:
        >>> solution('(')
        False
        >>> solution('()')
        True
        >>> solution(')*')
        False
        >>> solution('(*)')
        True
        >>> solution('(*))')
        True
    """
    left = right = 0
    n = len(s) - 1
    for i in range(n + 1):
        if s[i] == '(' or s[i] == '*':
            left += 1
        else:
            left -= 1
        if s[n - i] == ')' or s[n - i] == '*':
            right += 1
        else:
            right -= 1
        if left < 0 or right < 0:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
