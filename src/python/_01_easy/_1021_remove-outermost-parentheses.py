import doctest


# ---------------------------------------------------------------------
# Approach 1: Counters. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Return s after removing the outermost parentheses of every
    primitive decomposition of s.

    Examples:
        >>> solution('()()')
        ''
        >>> solution('(()())(())')
        '()()()'
        >>> solution('(()())(())(()(()))')
        '()()()()(())'
    """
    res = []
    i = j = 0
    for ch in s:
        if ch == '(':
            i += 1
        else:
            j += 1
        if i == j:
            i = j = 0
        elif i != 1:
            res.append(ch)
    return ''.join(res)


if __name__ == '__main__':
    doctest.testmod()
