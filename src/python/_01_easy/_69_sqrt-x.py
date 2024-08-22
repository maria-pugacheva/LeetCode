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
    if x < 2:
        return x
    i, j = 2, x // 2
    while i <= j:
        mid = (i + j) // 2
        if mid ** 2 == x:
            return mid
        elif mid ** 2 < x:
            i = mid + 1
        else:
            j = mid - 1
    return j


# ---------------------------------------------------------------------
# Approach 2: Newton's Method. Time: O(log n)                         !
# ---------------------------------------------------------------------
def solution_two(x: int) -> int:
    """Given a non-negative integer x, return the square root of x
    rounded down to the nearest integer.

    Examples:
        >>> solution_two(0)
        0
        >>> solution_two(1)
        1
        >>> solution_two(3)
        1
        >>> solution_two(4)
        2
        >>> solution_two(8)
        2
        >>> solution_two(10)
        3
        >>> solution_two(12)
        3
    """
    if x < 2:
        return x

    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + float(x) / x0) / 2

    return int(x1)


if __name__ == '__main__':
    doctest.testmod()
