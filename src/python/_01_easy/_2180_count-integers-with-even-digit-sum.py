import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(log n), n is the N of digits in num     !**
# ---------------------------------------------------------------------
def solution(num: int) -> int:
    """Given a positive integer num, return the number of positive
    integers less than or equal to num whose digit sum is even.

    Examples:
        >>> solution(4)
        2
        >>> solution(14)
        6
        >>> solution(30)
        14
        >>> solution(896)
        447
    """
    n, d_sum = num, 0
    while n:
        d_sum += n % 10
        n //= 10
    return num // 2 - 1 if not num & 1 and d_sum & 1 else num // 2


if __name__ == '__main__':
    doctest.testmod()
