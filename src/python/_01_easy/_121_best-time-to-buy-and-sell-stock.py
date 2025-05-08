import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n^2)                             ***
# ---------------------------------------------------------------------
def solution_one(prices: List[int]) -> int:
    """Maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.
    Return 0 if you cannot get any profit.

    Examples:
        >>> solution_one([7, 6, 4, 3, 1])
        0
        >>> solution_one([7, 1, 5, 3, 6, 4])
        5
    """
    profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = max(profit, prices[j] - prices[i])
    return profit


# ---------------------------------------------------------------------
# Approach 2: Dynamic Programming. Time: O(n)                       ***
# ---------------------------------------------------------------------
def solution_two(prices: List[int]) -> int:
    """Maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.
    Return 0 if you cannot get any profit.

    Examples:
        >>> solution_two([7, 6, 4, 3, 1])
        0
        >>> solution_two([7, 1, 5, 3, 6, 4])
        5
    """
    profit = 0
    p = prices[0]
    for i in range(1, len(prices)):
        if prices[i] - p > profit:
            profit = prices[i] - p
        elif prices[i] < p:
            p = prices[i]
    return profit


if __name__ == '__main__':
    doctest.testmod()
