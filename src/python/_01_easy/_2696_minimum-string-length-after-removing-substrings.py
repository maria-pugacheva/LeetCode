import doctest


# ---------------------------------------------------------------------
# Approach 1: Stack. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Remove any occurrence of one of the substrings "AB" or "CD" from
    s and return the minimum possible length of the resulting string
    that you can obtain.

    Examples:
        >>> solution('B')
        1
        >>> solution('AB')
        0
        >>> solution('ACBBD')
        5
        >>> solution('ABFCACDB')
        2
    """
    substrings = {'AB', 'CD'}
    stack = []
    for ch in s:
        if len(stack) > 0 and stack[-1] + ch in substrings:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)


if __name__ == '__main__':
    doctest.testmod()
