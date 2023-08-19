import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1). Space: O(1)                         ***
# ---------------------------------------------------------------------
def solution_one(n: int) -> int:
    """Return the number of matches played between n teams.

    Preconditions:
        1 <= n <= 200

    Examples:
        >>> solution_one(1)
        0
        >>> solution_one(5)
        4
        >>> solution_one(20)
        19
    """
    return n - 1


if __name__ == '__main__':
    doctest.testmod()
