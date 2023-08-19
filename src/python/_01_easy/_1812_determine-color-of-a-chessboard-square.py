import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1)                                      ***
# ---------------------------------------------------------------------
def solution_one(c: str) -> bool:
    """Return True if c represents a white chessboard square.

    Examples:
        >>> solution_one('a1')
        False
        >>> solution_one('h3')
        True
        >>> solution_one('c7')
        False
    """
    return True if (ord(c[0]) + int(c[1])) & 1 else False


if __name__ == '__main__':
    doctest.testmod()
