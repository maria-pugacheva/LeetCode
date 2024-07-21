import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1)                                        !
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Hercy is saving money for his first car by depositing funds into
    the Leetcode bank daily. He begins with $1 on Monday, the first day,
    and each subsequent day up to Sunday sees an increase of $1 compared
    to the previous day. Each following Monday, his deposit increases by
    an additional $1 compared to the previous Monday. Given n, return
    the total amount of money he will have in the Leetcode bank at the
    end of the n-th day.

    Preconditions:
        1 <= n <= 1000

    Examples:
        >>> solution(4)
        10
        >>> solution(10)
        37
        >>> solution(20)
        96
    """
    weeks = n // 7
    first_week = 28
    last_week = first_week + (weeks - 1) * 7
    total = (first_week + last_week) * weeks / 2
    k = weeks + 1
    for day in range(n % 7):
        total += k
        k += 1
    return int(total)


if __name__ == '__main__':
    doctest.testmod()
