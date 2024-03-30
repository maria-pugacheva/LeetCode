import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(s: str) -> bool:
    """Given a binary string s without leading zeros, return True if s
    contains at most one contiguous segment of ones. Otherwise, return
    False.

    Preconditions:
        1 <= len(s) <= 100
        s[0] == '1'

    Examples:
        >>> solution('110')
        True
        >>> solution('101')
        False
        >>> solution('1001100')
        False
    """
    for i in range(len(s) - 1):
        if s[i] == '0' and s[i + 1] == '1':
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
