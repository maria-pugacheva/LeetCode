import doctest


# ---------------------------------------------------------------------
# Approach 1: Fibonacci Numbers. Time: O(n)                         ***
# ---------------------------------------------------------------------
def solution_one(n: int) -> int:
    """You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct
    ways can you climb to the top?

    Preconditions:
        1 <= n <= 45

    Notes:
        If n is greater than 45, the result will exceed the
        Integer.MAX_VALUE.

    Examples:
        >>> solution_one(1)
        1
        >>> solution_one(2)
        2
        >>> solution_one(3)
        3
        >>> solution_one(4)
        5
        >>> solution_one(5)
        8
    """
    first, second = 0, 1
    for i in range(n):
        third = first + second
        first, second = second, third
    return second


# ---------------------------------------------------------------------
# Approach 2: Fibonacci (Binet's) Formula. Time: O(log n)             !
# ---------------------------------------------------------------------
# Note: Binet's formula provides an explicit expression for calculating
#       the nth Fibonacci number directly, without needing to calculate
#       previous terms in the sequence.
# Complexity Analysis: The `pow` method takes O(log n) time.
# ---------------------------------------------------------------------
def solution_two(n: int) -> int:
    """You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct
    ways can you climb to the top?

    Preconditions:
        1 <= n <= 45

    Notes:
        If n is greater than 45, the result will exceed the
        Integer.MAX_VALUE.

    Examples:
        >>> solution_two(1)
        1
        >>> solution_two(2)
        2
        >>> solution_two(3)
        3
        >>> solution_two(4)
        5
        >>> solution_two(5)
        8
    """
    sqrt_5 = 5 ** 0.5
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((phi ** (n + 1) - psi ** (n + 1)) / sqrt_5)


if __name__ == '__main__':
    doctest.testmod()
