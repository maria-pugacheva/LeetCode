import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(n)                                      ***
# ---------------------------------------------------------------------
def solution_one(n: int) -> List[int]:
    """Return any list containing n unique integers that add up to 0.

    Preconditions:
        1 <= n <= 1000

    Examples:
        >>> solution_one(1)
        [0]
        >>> solution_one(6)
        [1, -1, 3, -3, 5, -5]
        >>> solution_one(11)
        [1, -1, 3, -3, 5, -5, 7, -7, 9, -9, 0]
    """
    nums = [0] * n
    for i in range(0, n - 1, 2):
        nums[i] = i + 1
        nums[i + 1] = -(i + 1)
    return nums


if __name__ == '__main__':
    doctest.testmod()
