import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(nums: List[int], k: int) -> int:
    """Return the number of pairs (i, j) where i < j such that
    |nums[i] - nums[j]| == k.

    Preconditions:
        1 <= len(nums) <= 200
        1 <= nums[i] <= 100
        1 <= k <= 99

    Examples:
        >>> solution([1, 3], 3)
        0
        >>> solution([1, 2, 2, 1], 1)
        4
        >>> solution([3, 2, 1, 5, 4], 2)
        3
        >>> solution([3, 2, 1, 5, 4, 3], 2)
        5
    """
    pairs = 0
    cnt = {}
    for n in nums:
        if n in cnt:
            pairs += cnt[n]
        cnt[n - k] = cnt.get(n - k, 0) + 1
        cnt[n + k] = cnt.get(n + k, 0) + 1
    return pairs


if __name__ == '__main__':
    doctest.testmod()
