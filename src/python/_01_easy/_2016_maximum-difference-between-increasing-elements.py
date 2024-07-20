import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: DP. Time: O(n)                                        ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Return the maximum difference between nums[i] and nums[j].

    Notes:
        The maximum difference between nums[i] and nums[j] is the
        difference such that 0 <= i < j < n and nums[i] < nums[j].

    Preconditions:
        n == len(nums)
        2 <= n <= 1000
        1 <= nums[i] <= 10^9

    Examples:
        >>> solution([9, 4, 3, 2])
        -1
        >>> solution([7, 1, 5, 4])
        4
        >>> solution([1, 5, 2, 10])
        9
    """
    diff = -1
    curr_min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > curr_min:
            diff = max(diff, nums[i] - curr_min)
        if nums[i] < curr_min:
            curr_min = nums[i]
    return diff


if __name__ == '__main__':
    doctest.testmod()
