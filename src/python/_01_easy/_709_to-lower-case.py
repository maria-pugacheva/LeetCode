import doctest


# ---------------------------------------------------------------------
# Approach 1: ASCII. Time: O(n). Space: O(n)                        ***
# ---------------------------------------------------------------------
# Hint: Think about the different capital letters and their ASCII codes.
#       How does that relate to their lowercase counterparts?
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Convert s to lowercase.

    Examples:
        >>> solution_one('here')
        'here'
        >>> solution_one('Hello')
        'hello'
        >>> solution_one('LOVELY')
        'lovely'
        >>> solution_one('Hello@[]')
        'hello@[]'
    """
    lower = list(s)
    for i in range(len(lower)):
        code = ord(lower[i])
        if 64 < code < 91:
            lower[i] = chr(code + 32)
    return ''.join(lower)


if __name__ == '__main__':
    doctest.testmod()
