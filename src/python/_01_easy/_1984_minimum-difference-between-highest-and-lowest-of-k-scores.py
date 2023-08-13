import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting + Sliding Window. Time: O(n log n)            ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], k: int) -> int:
    """Return the minimum possible difference between the highest and
    the lowest of the k scores in nums.

    Preconditions:
        1 <= k <= len(nums) <= 1000
        0 <= nums[i] <= 10^5

    Examples:
        >>> solution_one([90], 1)
        0
        >>> solution_one([9, 4, 1, 7], 2)
        2
        >>> solution_one([0, 4, 1, 7], 3)
        4
    """
    nums.sort()
    diff = nums[k-1] - nums[0]
    for i in range(1, len(nums) - k + 1):
        diff = min(diff, nums[i+k-1] - nums[i])
    return diff


if __name__ == '__main__':
    doctest.testmod()
