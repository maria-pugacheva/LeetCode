import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log(n))                            !**
# ---------------------------------------------------------------------
def solution_one(nums: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals and return an array of the
    non-overlapping intervals that cover all the intervals in the input.

    Examples:
        >>> solution_one([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> solution_one([[1, 4], [4, 5]])
        [[1, 5]]
        >>> solution_one([[1, 4], [2, 3]])
        [[1, 4]]
        >>> solution_one([[1, 4], [0, 0]])
        [[0, 0], [1, 4]]
    """
    nums.sort()
    res = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i][0] <= res[-1][1]:
            res[-1][0] = min(res[-1][0], nums[i][0])
            res[-1][1] = max(res[-1][1], nums[i][1])
        else:
            res.append(nums[i])
    return res


if __name__ == '__main__':
    doctest.testmod()
