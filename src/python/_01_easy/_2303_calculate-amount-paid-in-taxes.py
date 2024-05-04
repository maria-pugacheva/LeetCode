import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(n)                                      ***
# ---------------------------------------------------------------------
def solution(brackets: List[List[int]], income: int) -> float:
    """Given an integer array brackets where brackets[i] =
    [upper-i, percent-i] and an integer income representing the amount
    of money you earned, return the amount of money that you have to pay
    in taxes.

    Examples:
        >>> solution([[2, 50]], 0)
        0
        >>> solution([[1, 0], [4, 25], [5, 50]], 2)
        0.25
        >>> solution([[3, 50], [7, 10], [12, 25]], 10)
        2.65
    """
    tax = p = i = 0
    while income > 0:
        tax += min(brackets[i][0] - p, income) * (brackets[i][1] / 100)
        income -= brackets[i][0] - p
        p = brackets[i][0]
        i += 1
    return tax


if __name__ == '__main__':
    doctest.testmod()
