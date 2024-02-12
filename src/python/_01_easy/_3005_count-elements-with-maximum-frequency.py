import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the total frequencies of elements in nums such that those
    elements all have the maximum frequency.

    Examples:
        >>> solution_one([1, 2, 2, 3, 1, 4])
        4
        >>> solution_one([1, 2, 3, 4, 5])
        5
        >>> solution_one([3, 3, 3, 1])
        3
    """
    d = {}
    max_f = 1
    for n in nums:
        d[n] = d.get(n, 0) + 1
        max_f = max(max_f, d[n])
    cnt = 0
    for v in d.values():
        if v == max_f:
            cnt += v
    return cnt


if __name__ == '__main__':
    doctest.testmod()
