import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n)                                      !
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
    cnt = 0
    l = r = 0
    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
