import doctest


# ---------------------------------------------------------------------
# Approach 1: String Concatenation. Time: O(n)                      ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Return a string where no three consecutive chars in s are equal.

    Examples:
        >>> solution_one('a')
        'a'
        >>> solution_one('aaab')
        'aab'
        >>> solution_one('aaanaaa')
        'aanaa'
    """
    ans = [s[0]]
    for ch in s:
        if ans[-1] != ch or len(ans) == 1 or ans[-2] != ch:
            ans.append(ch)
    return ''.join(ans)


if __name__ == '__main__':
    doctest.testmod()
