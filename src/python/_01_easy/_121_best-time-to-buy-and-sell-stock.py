import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dynamic Programming. Time: O(n)                       ***
# ---------------------------------------------------------------------
def solution(prices: List[int]) -> int:
    """Maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.
    Return 0 if you cannot get any profit.

    Examples:
        >>> solution([7, 6, 4, 3, 1])
        0
        >>> solution([7, 1, 5, 3, 6, 4])
        5
    """
    profit = 0
    min_price = prices[0]
    for i in range(len(prices)):
        p = prices[i]
        if p < min_price:
            min_price = p
        if p - min_price > profit:
            profit = p - min_price
    return profit


if __name__ == '__main__':
    doctest.testmod()
