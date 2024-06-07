import doctest


# ---------------------------------------------------------------------
# Approach 1: Last Digit. Time: O(log n)                            ***
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Return the difference between the product of digits in n and the
    sum of its digits.

    Examples:
        >>> solution(234)
        15
        >>> solution(4421)
        21
        >>> solution(1)
        0
    """
    p = 1
    s = 0
    while n > 0:
        digit = n % 10
        p *= digit
        s += digit
        n //= 10
    return p - s


if __name__ == '__main__':
    doctest.testmod()
