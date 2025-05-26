import doctest


# ---------------------------------------------------------------------
# Approach 1: Pop and Push. Time: O(log x)                          ***
# ---------------------------------------------------------------------
# Complexity Analysis: The number of iterations is proportional to the
# number of digits.
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Return x with its digits reversed.

    Examples:
        >>> solution(123)
        321
        >>> solution(-123)
        -321
        >>> solution(120)
        21
        >>> solution(1534236469)
        0
        >>> solution(2147483647)
        0
        >>> solution(-2147483648)
        0
    """
    intMax = 2**31 - 1
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        t = n % 10
        if rev > intMax // 10:
            return 0
        rev = rev * 10 + t
        n //= 10
    return rev * sign


if __name__ == '__main__':
    doctest.testmod()
