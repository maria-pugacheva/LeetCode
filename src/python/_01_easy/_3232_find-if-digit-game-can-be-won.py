import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> bool:
    """Alice and Bob are playing a game. In the game, Alice can choose
    either all single-digit numbers or all double-digit numbers from
    nums, and the rest of the numbers are given to Bob. Alice wins if
    the sum of her numbers is strictly greater than the sum of Bob's
    numbers. Return True if Alice can win this game; otherwise, return
    False.

    Examples:
        >>> solution_one([1, 2, 3, 4, 10])
        False
        >>> solution_one([5, 5, 5, 25])
        True
        >>> solution_one([1, 2, 3, 4, 5, 14])
        True
    """
    single_sum = double_sum = 0
    for n in nums:
        if n < 10:
            single_sum += n
        else:
            double_sum += n
    return single_sum != double_sum


if __name__ == '__main__':
    doctest.testmod()
