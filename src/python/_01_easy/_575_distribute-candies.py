import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution_one(candies: List[int]) -> int:
    """Given the integer array candies of length n, return the maximum
    number of different types of candies Alice can eat if she only eats
    n / 2 of them.

    Preconditions:
        n == len(candies)
        2 <= n <= 10^4
        n is even
        -10^5 <= candies[i] <= 10^5

    Examples:
        >>> solution_one([6, 6, 6, 6])
        1
        >>> solution_one([1, 1, 2, 3])
        2
        >>> solution_one([1, 1, 2, 2, 3, 3])
        3
    """
    return min(len(set(candies)), len(candies) // 2)


if __name__ == '__main__':
    doctest.testmod()
