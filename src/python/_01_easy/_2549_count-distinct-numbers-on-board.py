import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1)                                      ***
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Given a positive integer n placed on a board, perform the
    following procedure every day for 10^9 days. For each number x
    present on the board, find all numbers 1 <= i <= n such that
    x % i == 1. Then, place those numbers on the board. Return the
    number of distinct integers present on the board after 10^9 days
    have elapsed.

    Examples:
        >>> solution(1)
        1
        >>> solution(3)
        2
        >>> solution(5)
        4
    """
    return n - 1 if n > 1 else 1


if __name__ == '__main__':
    doctest.testmod()
