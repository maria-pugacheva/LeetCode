import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(nums: List[int], k: int) -> int:
    """Iterate over the elements in nums in reverse order and return
    the minimum number of operations needed to collect elements 1, 2,
    ..., k.

    Notes:
        - nums can contain duplicate elements

    Examples:
        >>> solution([1, 2, 2], 2)
        3
        >>> solution([3, 1, 5, 4, 2], 2)
        4
        >>> solution([3, 1, 5, 4, 2], 5)
        5
    """
    cnt = 0
    seen = set()
    for i in range(len(nums) - 1, -1, -1):
        cnt += 1
        if nums[i] <= k:
            seen.add(nums[i])
        if len(seen) == k:
            break
    return cnt


if __name__ == '__main__':
    doctest.testmod()
