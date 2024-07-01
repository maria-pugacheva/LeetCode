import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                    !
# ---------------------------------------------------------------------
def solution(prices: List[int]) -> int:
    """Given an integer array prices where prices[i] is the price of a
    given stock on the ith day, return the maximum profit you can
    achieve. You can but and sell the stock multiple times.

    Examples:
        >>> solution([7, 6, 4, 3, 1])
        0
        >>> solution([1, 2, 3, 4, 5])
        4
        >>> solution([7, 1, 5, 3, 6, 4])
        7
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


if __name__ == '__main__':
    doctest.testmod()
