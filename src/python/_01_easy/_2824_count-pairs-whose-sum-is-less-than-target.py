import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution(nums: List[int], t: int) -> int:
    """Return the number of pairs (i, j) where 0 <= i < j < n and
    nums[i] + nums[j] < target.

    Examples:
        >>> solution([-1, 1, 2, 3, 1], 2)
        3
        >>> solution([-6, 2, 5, -2, -7, -1, 3], -2)
        10
    """
    nums.sort()
    cnt = i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] < t:
            cnt += (j - i)
            i += 1
        else:
            j -= 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
