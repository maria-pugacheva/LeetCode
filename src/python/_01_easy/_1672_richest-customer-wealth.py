import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Max. Time: O(n * m). Space: O(1)                      ***
# ---------------------------------------------------------------------
def solution_one(customers: List[List[int]]) -> int:
    """Return the wealth that the richest customer in customers has.

    Preconditions:
    1 <= len(customers), len(customers[i]) <= 50
    1 <= customers[i][j] <= 100

    Examples:
        >>> solution_one([[1]])
        1
        >>> solution_one([[1, 2, 3], [3, 2, 1]])
        6
        >>> solution_one([[2, 8, 7], [7, 1, 3], [1, 9, 5]])
        17
    """
    mx = -1
    for c in customers:
        mx = max(mx, sum(c))
    return mx


if __name__ == '__main__':
    doctest.testmod()
