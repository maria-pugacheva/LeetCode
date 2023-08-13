import doctest


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n)                                    ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the minimum N of moves to convert all chars in s to 'O'.

    Notes:
        A move is defined as selecting three consecutive characters of s
        and converting them to 'O'.  If a move is applied to the
        character 'O', it will stay the same.

    Preconditions:
        3 <= len(s) <= 1000
        s[i] is either 'X' or 'O'

    Examples:
        >>> solution_one('XXX')
        1
        >>> solution_one('OOO')
        0
        >>> solution_one('XXOX')
        2
    """
    cnt = 0
    i = 0
    while i < len(s):
        if s[i] == 'X':
            cnt += 1
            i += 2
        i += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
