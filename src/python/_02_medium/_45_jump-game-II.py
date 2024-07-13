import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n)                                     !!
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """You are initially positioned at the array's first index, and each
    element in the array represents your maximum jump length at that
    position. Return the minimum number of jumps to reach the end of
    nums.

    Examples:
        >>> solution([2, 3, 1, 1, 4])
        2
        >>> solution([2, 3, 0, 1, 4])
        2
    """
    cnt = curr_far = curr_end = 0
    for i in range(len(nums) - 1):
        curr_far = max(curr_far, i + nums[i])
        if i == curr_end:
            cnt += 1
            curr_end = curr_far
    return cnt


if __name__ == '__main__':
    doctest.testmod()
