import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1)                                      ***
# ---------------------------------------------------------------------
# Hint: If the range (high - low + 1) is even, the number of even and
#       odd numbers in this range will be the same.
# ---------------------------------------------------------------------
def solution_one(low: int, high: int) -> int:
    """Return the count of odd numbers between low and high (inclusive).

    Preconditions:
        0 <= low <= high <= 10^9

    Examples:
        >>> solution_one(0, 4)
        2
        >>> solution_one(3, 7)
        3
        >>> solution_one(6, 15)
        5
    """
    diff = high - low + 1
    if diff & 1 and low & 1:
        return (diff // 2) + 1
    return diff // 2


if __name__ == '__main__':
    doctest.testmod()
