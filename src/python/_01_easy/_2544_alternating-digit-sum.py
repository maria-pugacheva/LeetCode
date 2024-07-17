import doctest


# ---------------------------------------------------------------------
# Approach 1: Number of Digits. Time: O(log n)                      ***
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Given a positive integer n, each digit of n has a sign according
    to the following rules: the most significant digit is assigned a
    positive sign and each other digit has an opposite sign to its
    adjacent digits. Return the sum of all the digits in n.

    Examples:
        >>> solution(1)
        1
        >>> solution(521)
        4
        >>> solution(111)
        1
        >>> solution(886996)
        0
        >>> solution(886998)
        -2
    """
    res, cnt, sign = 0, 0, 1
    while n:
        res += (n % 10) * sign
        n //= 10
        sign *= -1
        cnt += 1
    return res if cnt & 1 else -res


if __name__ == '__main__':
    doctest.testmod()
