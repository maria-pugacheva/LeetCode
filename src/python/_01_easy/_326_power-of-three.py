import doctest


# ---------------------------------------------------------------------
# Approach 1: Loop Iteration. Time: O(log3n)                          !
# ---------------------------------------------------------------------
def solution_one(n: int) -> bool:
    """Given an integer n, return True if it is a power of three.
    Otherwise, return False.

    Preconditions:
        -2^31 <= n <= 2^31 - 1

    Examples:
        >>> solution_one(27)
        True
        >>> solution_one(0)
        False
        >>> solution_one(-1)
        False
    """
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


# ---------------------------------------------------------------------
# Approach 2: Integer Limitations. Time: O(1)                         !
# ---------------------------------------------------------------------
# Knowing the limitation of n, we can now deduce that the maximum value
# of n that is also a power of three is 1,162,261,467 = 3^19.
# ---------------------------------------------------------------------
def solution_two(n: int) -> bool:
    """Given an integer n, return True if it is a power of three.
    Otherwise, return False.

    Preconditions:
        -2^31 <= n <= 2^31 - 1

    Examples:
        >>> solution_two(27)
        True
        >>> solution_two(0)
        False
        >>> solution_two(-1)
        False
    """
    return n > 0 and 3**19 % n == 0


if __name__ == '__main__':
    doctest.testmod()
