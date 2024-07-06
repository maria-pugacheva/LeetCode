import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(log n)                               !
# ---------------------------------------------------------------------
# Note: Recursion would take O(log n) extra space
# ---------------------------------------------------------------------
def solution_one(x: float, n: int) -> float:
    """Implement pow(x, n), which calculates x raised to the power n.

    Examples:
        # >>> solution_one(2.00000, 10)
        # 1024.00000
        >>> solution_one(2.10000, 3)
        9.26100
        >>> solution_one(2.00000, -2)
        0.25000
    """
    res = 1
    if n == 0:
        return res
    if n < 0:
        n = abs(n)
        x = 1/x
    while n != 0:
        if n % 2 == 1:
            res *= x
            n -= 1
        x *= x
        n //= 2
    return res


if __name__ == '__main__':
    doctest.testmod()
