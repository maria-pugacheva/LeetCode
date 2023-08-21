import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sort. Time: O(n log n).                               ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the maximized sum obtained by grouping all the integers in
    nums into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the
    sum of min(ai, bi) for all i is maximized.

    Preconditions:
        1 <= n <= 10^4
        len(nums) == 2 * n
        -10^4 <= nums[i] <= 10^4

    Examples:
        >>> solution_one([-1, 0, 2, 4])
        1
        >>> solution_one([1, 4, 3, 2])
        4
        >>> solution_one([6, 2, 6, 5, 1, 2])
        9
    """
    nums.sort()
    res = 0
    for i in range(0, len(nums), 2):
        res += nums[i]
    return res


if __name__ == '__main__':
    doctest.testmod()
