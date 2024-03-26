import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution(cost: List[int]) -> int:
    """A shop is selling candies at a discount. For every two candies
    sold, the shop gives a third candy for free. The customer can choose
    any candy to take away for free as long as the cost of the chosen
    candy is less than or equal to the minimum cost of the two candies
    bought. Given a 0-indexed integer array cost, where cost[i] denotes
    the cost of the ith candy, return the minimum cost of buying all the
    candies.

    Examples:
        >>> solution([5, 5])
        10
        >>> solution([1, 2, 3])
        5
        >>> solution([6, 5, 7, 9, 2, 2])
        23
    """
    cost.sort()
    res = cnt = 0
    for i in range(len(cost) - 1, -1, -1):
        if cnt < 2:
            res += cost[i]
            cnt += 1
        else:
            cnt = 0
    return res


if __name__ == '__main__':
    doctest.testmod()
