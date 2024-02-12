import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sort. Time: O(n log n)                                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> List[int]:
    """Every round, first Alice will remove the minimum element from
    nums, and then Bob does the same. Now, first Bob will add the
    removed element to a new array arr, and then Alice does the same.
    Return the resulting array arr.

    Examples:
        >>> solution_one([5, 4, 2, 3])
        [3, 2, 5, 4]
        >>> solution_one([2, 5])
        [5, 2]
    """
    arr = sorted(nums)
    for i in range(1, len(nums), 2):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr


if __name__ == '__main__':
    doctest.testmod()
