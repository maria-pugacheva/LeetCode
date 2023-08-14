import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterate Backwards. Time: O(n)                         ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Return the largest-valued odd non-empty substring of s.

    Preconditions:
        1 <= len(s) <= 10^5
        s only consists of digits and does not contain any leading zeros

    Examples:
        >>> solution_one('24')
        ''
        >>> solution_one('155')
        '155'
        >>> solution_one('14278')
        '1427'
    """
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) & 1:
            return s[:i+1]
    return ''


# ---------------------------------------------------------------------
# Approach 2: String to Integer Conversion. Time: O(n)              ***
# ---------------------------------------------------------------------
def solution_two(s: str) -> str:
    """Return the largest-valued odd non-empty substring of s.

    Preconditions:
        1 <= len(s) <= 10^5
        s only consists of digits and does not contain any leading zeros

    Examples:
        >>> solution_two('24')
        ''
        >>> solution_two('155')
        '155'
        >>> solution_two('14278')
        '1427'
    """
    n = int(s)
    if n & 1:
        return s
    while n:
        n //= 10
        if n & 1:
            return str(n)
    return ''


if __name__ == '__main__':
    doctest.testmod()
