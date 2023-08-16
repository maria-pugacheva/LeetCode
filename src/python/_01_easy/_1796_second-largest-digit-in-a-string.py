import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the second largest digit in s, or -1 if it does not exist.

    Preconditions:
        1 <= len(s) <= 500
        s consists of only lowercase English letters and/or digits

    Examples:
        >>> solution_one('abc077')
        0
        >>> solution_one('a8344')
        4
        >>> solution_one('abc11111111')
        -1
    """
    max_one = max_two = -1
    for ch in s:
        if ch.isdigit():
            n = int(ch)
            if n > max_one:
                max_one, max_two = n, max_one
            elif max_two < n < max_one:
                max_two = n
    return max_two


if __name__ == '__main__':
    doctest.testmod()
