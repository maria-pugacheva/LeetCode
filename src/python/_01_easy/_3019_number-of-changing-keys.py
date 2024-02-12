import doctest


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the number of times the user had to change the key
    to type string s.

    Preconditions:
        Modifiers like Shift or Caps Lock won't be counted
        1 <= len(s) <= 100

    Examples:
        >>> solution_one('AaaAa')
        0
        >>> solution_one('aaB')
        1
        >>> solution_one('aaBbC')
        2
        >>> solution_one('aaBbCb')
        3
    """
    cnt = 0
    curr = s[0].lower()
    for i in range(1, len(s)):
        ch = s[i].lower()
        if ch != curr:
            cnt += 1
            curr = ch
    return cnt


if __name__ == '__main__':
    doctest.testmod()
