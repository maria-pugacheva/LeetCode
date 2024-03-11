import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(n)                                      ***
# ---------------------------------------------------------------------
def solution(s: str, letter: str) -> int:
    """Given a string s and a character letter, return the percentage of
    characters in s that equal letter rounded down to the nearest whole
    percent.

    Examples:
        >>> solution('jjjj', 'k')
        0
        >>> solution('sgawtb', 's')
        16
        >>> solution('foobar', 'o')
        33
    """
    return int(s.count(letter) / len(s) * 100)


if __name__ == '__main__':
    doctest.testmod()
