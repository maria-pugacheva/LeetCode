import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                                !
# ---------------------------------------------------------------------
def solution_one(colors: List[int]) -> int:
    """Return the maximum distance between two houses with different
    colors.

    Preconditions:
        n == len(colors)
        2 <= n <= 100
        0 <= colors[i] <= 100

    Examples:
        >>> solution_one([0, 1])
        1
        >>> solution_one([1, 8, 3, 8, 3])
        4
        >>> solution_one([1, 1, 1, 6, 1, 1, 1])
        3
        >>> solution_one([6, 6, 6, 6, 6, 6, 6, 6, 6, 19, 19, 6, 6])
        10
    """
    i = 0
    while colors[i] == colors[-1]:
        i += 1
    j = len(colors) - 1
    while colors[j] == colors[0]:
        j -= 1
    return max(len(colors) - i - 1, j)


if __name__ == '__main__':
    doctest.testmod()
