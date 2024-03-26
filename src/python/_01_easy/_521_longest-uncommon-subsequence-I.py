import doctest


# ---------------------------------------------------------------------
# Approach 1: Maximum Length. Time: O(n)                            ***
# ---------------------------------------------------------------------
def solution(a: str, b: str) -> int:
    """Given two strings a and b, return the length of the longest
    uncommon subsequence between a and b. If no such uncommon
    subsequence exists, return -1.

    Examples:
        >>> solution('aaa', 'aaa')
        -1
        >>> solution('aaa', 'bbb')
        3
        >>> solution('aba', 'cdc')
        3
    """
    return -1 if a == b else max(len(a), len(b))


if __name__ == '__main__':
    doctest.testmod()
