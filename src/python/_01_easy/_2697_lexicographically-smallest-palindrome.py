import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Make s a palindrome with the minimum number of operations
    possible. If there are multiple palindromes that can be made using
    the minimum number of operations, make the lexicographically
    smallest one.

    Examples:
        >>> solution('abcd')
        'abba'
        >>> solution('egcfe')
        'efcfe'
        >>> solution('seven')
        'neven'
    """
    s = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            s[i] = s[j] = min(s[i], s[j])
        i += 1
        j -= 1
    return ''.join(s)


if __name__ == '__main__':
    doctest.testmod()
