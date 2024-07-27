import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(log n)                                  ***
# ---------------------------------------------------------------------
def solution(n: int, m: int) -> int:
    """There are n water bottles that are initially full of water. You
    can exchange m empty water bottles for one full bottle. Given the
    two integers n and m, return the maximum number of water bottles
    you can drink.

    Examples:
        >>> solution(9, 3)
        13
        >>> solution(15, 4)
        19
    """
    cnt = n
    while n >= m:
        cnt += n // m
        n = (n // m) + (n % m)
    return cnt


if __name__ == '__main__':
    doctest.testmod()
