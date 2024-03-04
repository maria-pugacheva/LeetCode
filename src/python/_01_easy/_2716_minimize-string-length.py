import doctest


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Return the number of unique characters in s.

    Examples:
        >>> solution('a')
        1
        >>> solution('aaabc')
        3
        >>> solution('cbbd')
        3
    """
    return len(set(s))


if __name__ == '__main__':
    doctest.testmod()
