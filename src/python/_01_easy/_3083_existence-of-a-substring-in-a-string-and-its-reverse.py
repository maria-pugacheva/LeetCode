import doctest


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(s: str) -> bool:
    """Given a string s, find any substring of length 2 which is also
    present in the reverse of s. Return True if such a substring exists,
    and False otherwise.

    Examples:
        >>> solution('abcd')
        False
        >>> solution('abcba')
        True
        >>> solution('leetcode')
        True
    """
    seen = set()
    for i in range(len(s) - 1):
        if s[i] == s[i+1] or ''.join([s[i+1], s[i]]) in seen:
            return True
        seen.add(''.join([s[i], s[i+1]]))
    return False


if __name__ == '__main__':
    doctest.testmod()
