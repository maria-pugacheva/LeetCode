import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two minimums. Time: O(n)                              !**
# ---------------------------------------------------------------------
def solution(nums:List[int]) -> int:
    """Divide nums into 3 disjoint contiguous sub-arrays and return the
    minimum possible sum of the cost of these sub-arrays.

    Preconditions:
        1 <= nums[i] <= 50

    Examples:
        >>> solution([1, 2, 8])
        11
        >>> solution([1, 2, 3, 4])
        6
        >>> solution([12, 2, 1, 1])
        14
    """
    cost = nums[0]
    min_1 = min_2 = 51
    for i in range(1, len(nums), 1):
        n = nums[i]
        if n < min_1:
            min_1, min_2 = n, min_1
        elif n < min_2:
            min_2 = n
    return cost + min_1 + min_2


if __name__ == '__main__':
    doctest.testmod()
