import doctest


# ---------------------------------------------------------------------
# Approach 1: Recursion. Time: O(2 ^ n). Space: O(n)                ***
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Given n, calculate F(n).

    Examples:
        >>> solution(2)
        1
        >>> solution(3)
        2
        >>> solution(4)
        3
    """
    if n <= 1:
        return n
    return solution(n - 1) + solution(n - 2)


# ---------------------------------------------------------------------
# Approach 2: Iterative Bottom-Up. Time: O(n). Space: O(1)          ***
# ---------------------------------------------------------------------
def solution_two(n: int) -> int:
    """Given n, calculate F(n).

    Examples:
        >>> solution_two(2)
        1
        >>> solution_two(3)
        2
        >>> solution_two(4)
        3
    """
    a, b = 0, 1
    for i in range(2, n + 1):
        curr = a + b
        a, b = b, curr
    return b


# ---------------------------------------------------------------------
# Approach 3: Math - Binet's Formula. Time: O(log n). Space: O(1)     !
# ---------------------------------------------------------------------
def solution_three(n: int) -> int:
    """Given n, calculate F(n).

    Examples:
        >>> solution_three(2)
        1
        >>> solution_three(3)
        2
        >>> solution_three(4)
        3
    """
    golden_ratio = (1 + (5 ** 0.5)) / 2
    return int(round((golden_ratio ** n) / (5 ** 0.5)))


if __name__ == '__main__':
    doctest.testmod()
