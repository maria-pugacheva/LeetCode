import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Check All. Time: O(n)                                   !
# ---------------------------------------------------------------------
def solution_one(digits: List[int]) -> List[int]:
    """Given a large integer represented as an integer array digits,
    increment it by one and return the resulting array of digits.

    Examples:
        >>> solution_one([9])
        [1, 0]
        >>> solution_one([1, 2, 3])
        [1, 2, 4]
        >>> solution_one([4, 3, 2, 1])
        [4, 3, 2, 2]
        >>> solution_one([4, 9, 9, 9])
        [5, 0, 0, 0]
        >>> solution_one([4, 0, 0, 9])
        [4, 0, 1, 0]
    """
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


if __name__ == '__main__':
    doctest.testmod()
