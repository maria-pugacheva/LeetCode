import doctest


# ---------------------------------------------------------------------
# Approach 1: Math                                                  ***
# ---------------------------------------------------------------------
def solution_one(x: int) -> int:
    """Return x with its digits reversed.

       Examples:
           >>> solution_one(123)
           321
           >>> solution_one(-123)
           -321
           >>> solution_one(120)
           21
           >>> solution_one(1534236469)
           0
       """
    neg = False
    if x < 0:
        neg = True
        x = -x
    n = 0
    while x > 0:
        n *= 10
        n += x % 10
        x //= 10
    if neg:
        n = -n
    if abs(n) > 2 ** 31 - 1:
        return 0
    return n


if __name__ == '__main__':
    doctest.testmod()
