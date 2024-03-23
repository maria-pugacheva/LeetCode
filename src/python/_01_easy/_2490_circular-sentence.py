import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(s: str) -> bool:
    """Return.

    Examples:
        >>> solution('leetcode exercises sound delightful')
        True
        >>> solution('eetcode')
        True
        >>> solution('Eetcode')
        False
        >>> solution('Leetcode is cool')
        False
    """
    for i in range(len(s)):
        if s[i] == ' ' and s[i - 1] != s[i + 1]:
            return False
    return s[0] == s[-1]


if __name__ == '__main__':
    doctest.testmod()
