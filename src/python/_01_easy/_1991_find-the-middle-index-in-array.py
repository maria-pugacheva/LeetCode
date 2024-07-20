import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Left and Right Sum. Time: O(n)                        ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Return the pivot index of nums such that nums[0] + nums[1] + ...
    + nums[i-1] == nums[i+1] + nums[i+2] + ... + nums[len(nums)-1].

    Preconditions:
        1 <= len(nums) <= 100
        -1000 <= nums[i] <= 1000

    Examples:
        >>> solution([1])
        0
        >>> solution([2, 5])
        -1
        >>> solution([2, 3, -1, 8, 4])
        3
    """
    right, left = sum(nums), 0
    for i in range(len(nums)):
        if right - left - nums[i] == left:
            return i
        left += nums[i]
    return -1


if __name__ == '__main__':
    doctest.testmod()
