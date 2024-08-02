import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(log(n base k)) = O(log n)               ***
# ---------------------------------------------------------------------
# Hint: The general steps for converting a base 10 or "normal" number
#       into another base are:
#       - First, divide the number by the base to get the remainder.
#       This remainder is the first, i.e. least significant, digit of
#       the new number in the other base.
#       - Then repeat the process by dividing the quotient of step 1,
#       by the new base. This time, the remainder is the second digit,
#       i.e. the second least significant.
#       - Repeat this process until your quotient becomes less than the
#       base. This quotient is the last digit, i.e. the most significant
#       digit.
# ---------------------------------------------------------------------
def solution_one(n: int, k: int) -> int:
    """Return the sum of the digits of n after converting n to base k.

    Preconditions:
        1 <= n <= 100
        2 <= k <= 10
        n is given in base 10

    Examples:
        >>> solution_one(10, 10)
        1
        >>> solution_one(34, 6)
        9
        >>> solution_one(93, 7)
        9
    """
    res = 0
    while n:
        res += n % k
        n //= k
    return res


if __name__ == '__main__':
    doctest.testmod()
