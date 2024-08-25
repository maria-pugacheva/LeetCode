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
    minPrice = prices[0]
    for i in range(1, len(prices)):
        if prices[i] - minPrice > profit:
            profit = prices[i] - minPrice
        else:
            minPrice = min(minPrice, prices[i])
    return profit


if __name__ == '__main__':
    doctest.testmod()
