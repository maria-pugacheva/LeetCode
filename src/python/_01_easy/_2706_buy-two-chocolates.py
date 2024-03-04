import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Min1 and Min2. Time: O(n)                             ***
# ---------------------------------------------------------------------
def solution(prices: List[int], money: int) -> int:
    """Given an integer array prices representing the prices of various
    chocolates in a store. Return the amount of money you will have
    leftover after buying exactly two chocolates. If there is no way for
    you to buy two chocolates without ending up in debt, return money.
    Note that the leftover must be non-negative.

    Examples:
        >>> solution([1, 2, 2], 3)
        0
        >>> solution([3, 2, 3], 3)
        3
    """
    min1 = min2 = money
    for p in prices:
        if p < min1:
            min1, min2 = p, min1
        elif p < min2:
            min2 = p
    change = money - min1 - min2
    return change if change >= 0 else money


if __name__ == '__main__':
    doctest.testmod()
