import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[int]:
    """Given an array of integers nums, replace each element with its
    rank. The rank represents how large the element is. The larger the
    element, the larger the rank. If two elements are equal, their rank
    must be the same.

    Examples:
        >>> solution([100, 100, 100])
        [1, 1, 1]
        >>> solution([40, 10, 20, 30])
        [4, 1, 2, 3]
        >>> solution([37, 12, 28, 9, 100, 56, 80, 5, 12])
        [5, 3, 4, 2, 8, 6, 7, 1, 3]
    """
    ranks, rank = {}, 1
    for x in sorted(nums):
        if x not in ranks:
            ranks[x] = rank
            rank += 1
    return [ranks[n] for n in nums]


if __name__ == '__main__':
    doctest.testmod()
