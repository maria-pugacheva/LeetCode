import doctest


# ---------------------------------------------------------------------
# Approach 1: Modulo. Time: O(1)                                    ***
# ---------------------------------------------------------------------
def solution(num: int) -> bool:
    """Reverse num to get rev1, then reverse rev1 to get rev2. Return
    True if rev2 equals num. Otherwise, return False. Reversing 12300
    gives 321 as the leading zeros are not retained.

    Examples:
        >>> solution(0)
        True
        >>> solution(526)
        True
        >>> solution(1800)
        False
    """
    return num < 10 or num % 10 != 0


if __name__ == '__main__':
    doctest.testmod()
