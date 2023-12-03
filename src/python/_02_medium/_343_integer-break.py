import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(n)                                      ***
# ---------------------------------------------------------------------
def solution_one(n: int) -> int:
    """Return the maximum product you can get after breaking n into
    k positive integers, where k >= 2, such that their sum equals n.

       Preconditions:
           2 <= n <= 58

       Examples:
           >>> solution_one(2)
           1
           >>> solution_one(10)
           36
           >>> solution_one(58)
           1549681956
       """
    if n == 2:
        return 1
    if n == 3:
        return 2
    res = 1
    while n > 4:
        res *= 3
        n -= 3
    return res * n


if __name__ == '__main__':
    doctest.testmod()
