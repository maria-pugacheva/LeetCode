import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> List[int]:
    """Return a list that is the concatenation of two nums lists.

    Preconditions:
        1 <= len(nums) <= 1000
        1 <= nums[i] <= 1000

    Examples:
        >>> solution_one([1])
        [1, 1]
        >>> solution_one([1, 2])
        [1, 2, 1, 2]
        >>> solution_one([1, 2, 3])
        [1, 2, 3, 1, 2, 3]
    """
    n = len(nums)
    res = [0] * n * 2
    for i in range(n):
        res[i] = res[i + n] = nums[i]
    return res


if __name__ == '__main__':
    doctest.testmod()
