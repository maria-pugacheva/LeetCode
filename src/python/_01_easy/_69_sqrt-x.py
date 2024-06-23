import doctest


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n)                           !
# ---------------------------------------------------------------------
def solution_one(x: int) -> int:
    """Given a non-negative integer x, return the square root of x
    rounded down to the nearest integer.

    Examples:
        >>> solution_one(0)
        0
        >>> solution_one(1)
        1
        >>> solution_one(3)
        1
        >>> solution_one(4)
        2
        >>> solution_one(8)
        2
        >>> solution_one(10)
        3
        >>> solution_one(12)
        3
    """
    if x * x == x:
        return x
    i, j = 1, x // 2
    while i <= j:
        mid = i + (j - i) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            i = mid + 1
        else:
            j = mid - 1
    return j


if __name__ == '__main__':
    doctest.testmod()
